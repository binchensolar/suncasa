import numpy as np
import numpy.ma as ma
import os, struct
from time import time
from taskinit import casalog
import multiprocessing as mp
from suncasa.utils import DButil


def maxfit_iter(imgfiles, box, imidx):
    from taskinit import ia,rg
    try:
        from astropy.io import fits as pyfits
    except:
        try:
            import pyfits
        except ImportError:
            raise ImportError('Neither astropy nor pyfits exists in this CASA installation')
    img = imgfiles[imidx]

    try:
        if (not ia.open(img)):
            raise Exception, "Cannot create image analysis tool using " + img
        print('Processing image: '+img)
        hdr = pyfits.getheader(img)
        pols = DButil.polsfromfitsheader(hdr)
        freqs = DButil.freqsfromfitsheader(hdr)
        ndx, ndy, nchans, npols = ia.shape()
        blc, trc = [0, 0], [ndx, ndy]
        if 'box' in locals():
            if box != '':
                blc[0], blc[1], trc[0], trc[1] = [int(ll) for ll in box.split(',')]
        results = {}
        for itpp in pols:
            results[itpp] = {'results':{},'converged':[]}
        for ll in range(nchans):
            for pp,itpp in enumerate(pols):
                comp = 'component{}'.format(ll)
                r = rg.box(blc=[blc[0], blc[1], ll, pp], trc=[trc[0], trc[1], ll, pp])
                iachan = ia.subimage(region=r, dropdeg=True)
                try:
                    result_dict = iachan.maxfit(point=True,negfind=False)
                    result_dict['component0']['converged'] = True
                    result_dict['component0']['flux']['polarisation'] = itpp
                    result_dict['component0']['spectrum']['frequency']['m0']['value'] = float(freqs[ll])
                    results[itpp]['results'][comp] = result_dict['component0']
                    results[itpp]['converged'].append(True)
                except:
                    results[itpp]['converged'].append(False)
        results[itpp]['results']['nelements'] = results[itpp]['results'].keys()
        # update timestamp
        timstr = hdr['date-obs']
        return [True, timstr, img, results]
    except Exception, instance:
        casalog.post(str('*** Error in imfit ***') + str(instance))
        # raise instance
        return [False, timstr, img, {}]
    finally:
        ia.done()


def pmaxfit(imagefiles, ncpu, box):
    from functools import partial
    # check if imagefiles is a single file or a list of files

    if isinstance(imagefiles, str):
        imagefiles = [imagefiles]
    if (not isinstance(imagefiles, list)):
        print 'input "imagefiles" is not a list. Abort...'

    # check file existence
    imgfiles = []
    for i, img in enumerate(imagefiles):
        if os.path.exists(img):
            imgfiles.append(img)
        else:
            casalog.post(img + 'does not exist. Skipping this one...')

    iterable = range(len(imgfiles))
    res = []

    if not (type(ncpu) is int):
        casalog.post('ncpu should be an integer')
        ncpu = 8

    # partition
    maxfit_part = partial(maxfit_iter, imgfiles, box)

    # parallelization
    para = 1
    timelapse = 0
    t0 = time()
    if para:
        casalog.post('Perform imfit in parallel ...')
        pool = mp.Pool(ncpu)
        # res = pool.map_async(maxfit_part, iterable)
        res = pool.map(maxfit_part, iterable)
        pool.close()
        pool.join()
    else:
        for i in iterable:
            res.append(maxfit_part(i))

    t1 = time()
    timelapse = t1 - t0
    print 'It took %f secs to complete' % timelapse
    # repackage this into a single dictionary
    results = {'succeeded': [], 'timestamps': [], 'imagenames': [], 'outputs': []}
    for r in res:
        results['succeeded'].append(r[0])
        results['timestamps'].append(r[1])
        results['imagenames'].append(r[2])
        results['outputs'].append(r[3])

    return results
