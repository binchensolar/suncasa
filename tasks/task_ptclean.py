import os
from taskinit import * 
import numpy as np
from suncasa.vla import vla_prep
import shutil
import multiprocessing as mp
from functools import partial
from time import time
import pdb

def clean_iter(tim, freq, vis, imageprefix, 
            ncpu, twidth, doreg, ephemfile, ephem, msinfofile,
            outlierfile, field, spw, selectdata, 
            uvrange, antenna, scan, observation, intent, mode, resmooth,gridmode,
            wprojplanes, facets, cfcache, rotpainc, painc, aterm, psterm, mterm, wbawp, conjbeams,
            epjtable, interpolation,
            niter, gain, threshold, psfmode, imagermode, ftmachine, mosweight,
            scaletype, multiscale, negcomponent, smallscalebias,
            interactive, mask, nchan, start, width, outframe,
            veltype, imsize, cell, phasecenter, restfreq, stokes, weighting,
            robust, uvtaper, outertaper, innertaper, modelimage, restoringbeam,
            pbcor, minpb, usescratch, noise, npixels, npercycle, cyclefactor,
            cyclespeedup, nterms, reffreq, chaniter, flatnoise, allowchunk, btidx):
    from taskinit import ms
    from taskinit import qa
    #from  __casac__.quanta import quanta as qa 
    from __main__ import default, inp
    from clean import clean    
    bt = btidx #0 
    if bt+twidth < len(tim)-1:
        et = btidx+twidth-1  
    else:
        et = len(tim)-1

    #tim_d = tim/3600./24.-np.fix(tim/3600./24.) 

    if bt == 0:
        bt_d=tim[bt]-((tim[bt+1]-tim[bt])/2)
    else:
        bt_d=tim[bt]-((tim[bt]-tim[bt-1])/2)
    if et == (len(tim)-1) or et == -1:
        et_d=tim[et]+((tim[et]-tim[et-1])/2)
    else:
        et_d=tim[et]+((tim[et+1]-tim[et])/2)

    #
    # bt_d=tim[bt]
    # et_d=tim[et]+0.005

    timerange = qa.time(qa.quantity(bt_d,'s'),prec=9)[0] + '~' + \
                qa.time(qa.quantity(et_d,'s'),prec=9)[0]
    tmid = (bt_d + et_d)/2. 
    btstr=qa.time(qa.quantity(bt_d,'s'),prec=9,form='fits')[0]
    print 'cleaning timerange: ' + timerange

    try:
        image0=btstr.replace(':','').replace('-','')
        imname=imageprefix+image0
        if not os.path.exists(imname):
            #inp(taskname = 'clean')
            clean(vis=vis,imagename=imname,outlierfile=outlierfile,field=field,
                  spw=spw,selectdata=selectdata,timerange=timerange,uvrange=uvrange,
                  antenna=antenna,scan=scan, observation=str(observation),intent=intent,
                  mode=mode, resmooth=resmooth, gridmode=gridmode, 
                  wprojplanes=wprojplanes,facets=facets,cfcache=cfcache,rotpainc=rotpainc, painc=painc,
                  psterm=psterm,aterm=aterm,mterm=mterm,wbawp=wbawp,conjbeams=conjbeams,
                  epjtable=epjtable,interpolation=interpolation,niter=niter,
                  gain=gain,
                  threshold=threshold,psfmode=psfmode,imagermode=imagermode, 
                  ftmachine=ftmachine,mosweight=mosweight,scaletype=scaletype,
                  multiscale=multiscale,negcomponent=negcomponent,
                  smallscalebias=smallscalebias,interactive=interactive,
                  mask=mask,nchan=nchan,start=start,width=width,outframe=outframe,
                  veltype=veltype,imsize=imsize,cell=cell,phasecenter=phasecenter,
                  restfreq=restfreq,stokes=stokes,weighting=weighting,
                  robust=robust,uvtaper=uvtaper,outertaper=outertaper,
                  innertaper=innertaper,modelimage=modelimage,
                  restoringbeam=restoringbeam,pbcor=pbcor,minpb=minpb,
                  usescratch=usescratch,noise=noise,npixels=npixels,npercycle=npercycle,
                  cyclefactor=cyclefactor,cyclespeedup=cyclespeedup,nterms=nterms,
                  reffreq=reffreq,chaniter=chaniter,flatnoise=flatnoise,
                  allowchunk=False)
            clnjunks=['.flux','.mask','.model','.psf','.residual']
            for clnjunk in clnjunks:
                if os.path.exists(imname+clnjunk):
                    shutil.rmtree(imname+clnjunk)

        if doreg: 
            # check if ephemfile and msinfofile exist
            if not ephem:
                print("ephemeris info does not exist!")
                return
            reftime = [timerange] 
            helio=vla_prep.ephem_to_helio(msinfo = msinfofile, ephem = ephem, reftime = reftime)
            imagefile=[imname+'.image']
            fitsfile=[imname+'.fits']
            vla_prep.imreg(imagefile = imagefile, fitsfile = fitsfile, helio = helio, toTb = False, scl100 = True)
            if os.path.exists(imname+'.fits'):
                return [True, btstr, imname+'.fits']
            else:
                return [False, btstr, '']
        else:
            if os.path.exists(imname+'.image'):
                return [True, btstr, imname+'.image']
            else:
                return [False, btstr, '']
    except:
        print('error in processing image: '+btstr)
        return [False, btstr, '']

def ptclean(vis, imageprefix, ncpu, twidth, doreg, ephemfile, msinfofile,
            outlierfile, field, spw, selectdata, timerange,
            uvrange, antenna, scan, observation, intent, mode, resmooth,gridmode,
            wprojplanes, facets, cfcache, rotpainc, painc, aterm, psterm, mterm, wbawp, conjbeams,
            epjtable, interpolation,
            niter, gain, threshold, psfmode, imagermode, ftmachine, mosweight,
            scaletype, multiscale, negcomponent, smallscalebias,
            interactive, mask, nchan, start, width, outframe,
            veltype, imsize, cell, phasecenter, restfreq, stokes, weighting,
            robust, uvtaper, outertaper, innertaper, modelimage, restoringbeam,
            pbcor, minpb, usescratch, noise, npixels, npercycle, cyclefactor,
            cyclespeedup, nterms, reffreq, chaniter, flatnoise, allowchunk):

    if not (type(ncpu) is int):
        casalog.post('ncpu should be an integer')
        ncpu = 8

    if doreg: 
        # check if ephemfile and msinfofile exist
        try:
            ephem=vla_prep.read_horizons(ephemfile = ephemfile)
        except ValueError:
            print("error in reading ephemeris file")
        if not os.path.isfile(msinfofile):
            print("msinfofile does not exist!")
    else:
        ephem=None

    # get number of time pixels
    ms.open(vis)
    ms.selectinit()
    timfreq = ms.getdata(['time', 'axis_info'], ifraxis = True)
    tim = timfreq['time']
    #dt = tim[1]-tim[0] #need to change to median of all time intervals
    dt = np.median(np.diff(tim))
    freq = timfreq['axis_info']['freq_axis']['chan_freq'].flatten()
    ms.close()

    if twidth < 1 or twidth > len(tim):
        casalog.post('twidth not between 1 and # of time pixels in the dataset. Change to 1')
        twidth = 1

    # find out the start and end time index according to the parameter timerange
    # if not defined (empty string), use start and end from the entire time of the ms
    if not timerange:
        btidx = 0
        etidx = len(tim)-1 
    else:
        try:
            (tstart, tend)=timerange.split('~')
            bt_s = qa.convert(qa.quantity(tstart,'s'),'s')['value']
            et_s = qa.convert(qa.quantity(tend,'s'),'s')['value']
            # only time is given but not date, add the date (at 0 UT) from the first record
            if bt_s < 86400. or et_s < 86400.:
                bt_s += np.fix(qa.convert(qa.quantity(tim[0],'s'),'d')['value'])*86400.
                et_s += np.fix(qa.convert(qa.quantity(tim[0],'s'),'d')['value'])*86400.
            btidx = np.argmin(np.abs(tim-bt_s))
            etidx = np.argmin(np.abs(tim-et_s))
            # make the indice back to those bracket by the timerange
            if tim[btidx] < bt_s:
                btidx += 1
            if tim[etidx] > et_s:
                etidx -= 1
            if etidx <= btidx:
                print "ending time must be greater than starting time"
                print "reinitiating to the entire time range"
                btidx = 0
                etidx = len(tim)-1
        except ValueError:
            print "keyword 'timerange' has a wrong format"
    
    btstr=qa.time(qa.quantity(tim[btidx],'s'),prec=9,form='fits')[0]
    etstr=qa.time(qa.quantity(tim[etidx],'s'),prec=9,form='fits')[0]
    
    iterable = range(btidx, etidx+1, twidth)
    print 'First time pixel: '+btstr
    print 'Last time pixel: '+etstr 
    print str(len(iterable))+' images to clean...'

    res = []
    # partition
    clnpart = partial(clean_iter, tim, freq, vis, 
            imageprefix, ncpu, twidth, doreg, ephemfile, ephem, msinfofile,
            outlierfile, field, spw, selectdata,
            uvrange, antenna, scan, observation, intent, mode, resmooth,gridmode,
            wprojplanes, facets, cfcache, rotpainc, painc, aterm, psterm, mterm, wbawp, conjbeams,
            epjtable, interpolation,
            niter, gain, threshold, psfmode, imagermode, ftmachine, mosweight,
            scaletype, multiscale, negcomponent, smallscalebias,
            interactive, mask, nchan, start, width, outframe,
            veltype, imsize, cell, phasecenter, restfreq, stokes, weighting,
            robust, uvtaper, outertaper, innertaper, modelimage, restoringbeam,
            pbcor, minpb, usescratch, noise, npixels, npercycle, cyclefactor,
            cyclespeedup, nterms, reffreq, chaniter, flatnoise, allowchunk)
    timelapse = 0
    t0 = time()
    # parallelization
    para=1
    if para:
        casalog.post('Perform clean in parallel ...')
        pool = mp.Pool(ncpu)
        #res = pool.map_async(clnpart, iterable)
        res = pool.map(clnpart, iterable)
        pool.close()
        pool.join()
    else:
        for i in iterable:
            res.append(clnpart(i))

    t1 = time()
    timelapse = t1 - t0
    print 'It took %f secs to complete' % timelapse
    # repackage this into a single dictionary
    results={'succeeded':[], 'timestamps':[], 'imagenames':[]}
    for r in res:
        results['succeeded'].append(r[0])
        results['timestamps'].append(r[1])
        results['imagenames'].append(r[2])

    return results




