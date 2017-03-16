#
# This file was generated using xslt from its XML file
#
# Copyright 2014, Associated Universities Inc., Washington DC
#
import sys
import os
#from casac import *
import casac
import string
import time
import inspect
import gc
import numpy
from odict import odict
from types import * 
from task_ptclean import ptclean
class ptclean_cli_:
    __name__ = "ptclean"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (ptclean_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'imageprefix':None, 'ncpu':None, 'twidth':None, 'doreg':None, 'overwrite':None, 'ephemfile':None, 'msinfofile':None, 'outlierfile':None, 'field':None, 'spw':None, 'selectdata':None, 'timerange':None, 'uvrange':None, 'antenna':None, 'scan':None, 'observation':None, 'intent':None, 'mode':None, 'resmooth':None, 'gridmode':None, 'wprojplanes':None, 'facets':None, 'cfcache':None, 'rotpainc':None, 'painc':None, 'aterm':None, 'psterm':None, 'mterm':None, 'wbawp':None, 'conjbeams':None, 'epjtable':None, 'interpolation':None, 'niter':None, 'gain':None, 'threshold':None, 'psfmode':None, 'imagermode':None, 'ftmachine':None, 'mosweight':None, 'scaletype':None, 'multiscale':None, 'negcomponent':None, 'smallscalebias':None, 'interactive':None, 'mask':None, 'nchan':None, 'start':None, 'width':None, 'outframe':None, 'veltype':None, 'imsize':None, 'cell':None, 'phasecenter':None, 'restfreq':None, 'stokes':None, 'weighting':None, 'robust':None, 'uvtaper':None, 'outertaper':None, 'innertaper':None, 'modelimage':None, 'restoringbeam':None, 'pbcor':None, 'minpb':None, 'usescratch':None, 'noise':None, 'npixels':None, 'npercycle':None, 'cyclefactor':None, 'cyclespeedup':None, 'nterms':None, 'reffreq':None, 'chaniter':None, 'flatnoise':None, 'allowchunk':None, }


    def result(self, key=None):
	    #### and add any that have completed...
	    return None


    def __call__(self, vis=None, imageprefix=None, ncpu=None, twidth=None, doreg=None, overwrite=None, ephemfile=None, msinfofile=None, outlierfile=None, field=None, spw=None, selectdata=None, timerange=None, uvrange=None, antenna=None, scan=None, observation=None, intent=None, mode=None, resmooth=None, gridmode=None, wprojplanes=None, facets=None, cfcache=None, rotpainc=None, painc=None, aterm=None, psterm=None, mterm=None, wbawp=None, conjbeams=None, epjtable=None, interpolation=None, niter=None, gain=None, threshold=None, psfmode=None, imagermode=None, ftmachine=None, mosweight=None, scaletype=None, multiscale=None, negcomponent=None, smallscalebias=None, interactive=None, mask=None, nchan=None, start=None, width=None, outframe=None, veltype=None, imsize=None, cell=None, phasecenter=None, restfreq=None, stokes=None, weighting=None, robust=None, uvtaper=None, outertaper=None, innertaper=None, modelimage=None, restoringbeam=None, pbcor=None, minpb=None, usescratch=None, noise=None, npixels=None, npercycle=None, cyclefactor=None, cyclespeedup=None, nterms=None, reffreq=None, chaniter=None, flatnoise=None, allowchunk=None, ):

        """Parallelized clean in consecutive time steps

	Detailed Description: 
Parallelized clean in consecutive time steps. Packed over CASA clean.
	Arguments :
		vis:	Name of input visibility file
		   Default Value: 

		imageprefix:	Prefix of image names (may include the path)
		   Default Value: 

		ncpu:	Number of cpu cores to use
		   Default Value: 8

		twidth:	Number of time pixels to average
		   Default Value: 1

		doreg:	True if use vla_prep to register the image
		   Default Value: False

		overwrite:	True if overwrite the image
		   Default Value: False

		ephemfile:	emphemeris file generated from vla_prep.read_horizons()
		   Default Value: 

		msinfofile:	time-dependent phase center information generated from vla_prep.read_msinfo()
		   Default Value: 

		outlierfile:	Text file with image names, sizes, centers for outliers
		   Default Value: 

		field:	Field Name or id
		   Default Value: 

		spw:	Spectral windows e.g. \'0~3\', \'\' is all
		   Default Value: 

		selectdata:	Other data selection parameters
		   Default Value: True

		timerange:	Range of time to select from data
		   Default Value: 

		uvrange:	Select data within uvrange 
		   Default Value: 

		antenna:	Select data based on antenna/baseline
		   Default Value: 

		scan:	Scan number range
		   Default Value: 

		observation:	Observation ID range
		   Default Value: 

		intent:	Scan Intent(s)
		   Default Value: 

		mode:	Spectral gridding type (mfs, channel, velocity, frequency)
		   Default Value: mfs
		   Allowed Values:
				mfs
				channel
				velocity
				frequency

		resmooth:	Re-restore the cube image to a common beam when True
		   Default Value: False

		gridmode:	Gridding kernel for FFT-based transforms, default=\'\' None
		   Default Value: 
		   Allowed Values:
				
				widefield
				aprojection
				advancedaprojection

		wprojplanes:	Number of w-projection planes for convolution; -1 =&gt; automatic determination 
		   Default Value: -1

		facets:	Number of facets along each axis (main image only)
		   Default Value: 1

		cfcache:	Convolution function cache directory
		   Default Value: cfcache.dir

		rotpainc:	Parallactic angle increment (degrees) for OTF A-term rotation
		   Default Value: 5.0

		painc:	Parallactic angle increment (degrees) for computing A-term
		   Default Value: 360.0

		aterm:	Switch-on the A-Term?
		   Default Value: True

		psterm:	Switch-on the PS-Term?
		   Default Value: False

		mterm:	Switch-on the M-Term?
		   Default Value: True

		wbawp:	Trigger the wide-band A-Projection algorithm?
		   Default Value: False

		conjbeams:	Use frequency conjugate beams in WB A-Projection algorithm?
		   Default Value: True

		epjtable:	Table of EP-Jones parameters
		   Default Value: 

		interpolation:	Spectral interpolation (nearest, linear, cubic). 
		   Default Value: linear
		   Allowed Values:
				nearest
				linear
				cubic
				spline

		niter:	Maximum number of iterations
		   Default Value: 500

		gain:	Loop gain for cleaning
		   Default Value: 0.1

		threshold:	Flux level to stop cleaning, must include units: \'1.0mJy\'
		   Default Value: 0.0

		psfmode:	Method of PSF calculation to use during minor cycles
		   Default Value: clark
		   Allowed Values:
				clark
				clarkstokes
				hogbom

		imagermode:	Options: \'csclean\' or \'mosaic\', \'\', uses psfmode
		   Default Value: csclean
		   Allowed Values:
				
				csclean
				mosaic
				

		ftmachine:	Gridding method for the image
		   Default Value: mosaic
		   Allowed Values:
				ft
				mosaic
				sd
				both
				awproject

		mosweight:	Individually weight the fields of the mosaic
		   Default Value: False

		scaletype:	Controls scaling of pixels in the image plane. default=\'SAULT\'; example: scaletype=\'PBCOR\' Options: \'PBCOR\',\'SAULT\'
		   Default Value: SAULT
		   Allowed Values:
				SAULT
				PBCOR

		multiscale:	Deconvolution scales (pixels); [] = standard clean
		   Default Value: 
	0
      

		negcomponent:	Stop cleaning if the largest scale finds this number of neg components
		   Default Value: -1

		smallscalebias:	a bias to give more weight toward smaller scales
		   Default Value: 0.6

		interactive:	Use interactive clean (with GUI viewer)
		   Default Value: False

		mask:	Cleanbox(es), mask image(s), region(s), or a level
		   Default Value: 

		nchan:	Number of channels (planes) in output image; -1 = all
		   Default Value: -1

		start:	start of output spectral dimension
		   Default Value: 0

		width:	width of output spectral channels
		   Default Value: 1

		outframe:	default spectral frame of output image 
		   Default Value: 
		   Allowed Values:
				lsrk
				lsrd
				bary
				geo
				topo
				galacto
				lgroup
				cmb
				

		veltype:	velocity definition (radio, optical, true) 
		   Default Value: radio
		   Allowed Values:
				radio
				optical
				true
				relativistic

		imsize:	x and y image size in pixels.  Single value: same for both
		   Default Value: 
    256256
    

		cell:	x and y cell size(s). Default unit arcsec.
		   Default Value: 1.0

		phasecenter:	Image center: direction or field index
		   Default Value: 

		restfreq:	Rest frequency to assign to image (see help)
		   Default Value: 

		stokes:	Stokes params to image (eg I,IV,IQ,IQUV)
		   Default Value: I
		   Allowed Values:
				I
				Q
				U
				V
				IV
				IQ
				QU
				UV
				IQU
				IUV
				IQUV
				RR
				LL
				RRLL
				XX
				YY
				XXYY

		weighting:	Weighting of uv (natural, uniform, briggs, ...)
		   Default Value: natural
		   Allowed Values:
				natural
				uniform
				briggs
				briggsabs
				radial
				superuniform

		robust:	Briggs robustness parameter
		   Default Value: 0.0
		   Allowed Values:
				-2.0
				2.0

		uvtaper:	Apply additional uv tapering of visibilities
		   Default Value: False

		outertaper:	uv-taper on outer baselines in uv-plane
		   Default Value: 
	      
	    

		innertaper:	uv-taper in center of uv-plane (not implemented)
		   Default Value: 1.0

		modelimage:	Name of model image(s) to initialize cleaning
		   Default Value: 

		restoringbeam:	Output Gaussian restoring beam for CLEAN image
		   Default Value: 

		pbcor:	Output primary beam-corrected image
		   Default Value: False

		minpb:	Minimum PB level to use
		   Default Value: 0.2

		usescratch:	True if to save model visibilities in MODEL_DATA column
		   Default Value: False

		noise:	noise parameter for briggs abs mode weighting
		   Default Value: 1.0Jy

		npixels:	number of pixels for superuniform or briggs weighting
		   Default Value: 0

		npercycle:	Clean iterations before interactive prompt (can be changed)
		   Default Value: 100

		cyclefactor:	Controls how often major cycles are done. (e.g. 5 for frequently)
		   Default Value: 1.5

		cyclespeedup:	Cycle threshold doubles in this number of iterations
		   Default Value: -1

		nterms:	Number of Taylor coefficients to model the sky frequency dependence 
		   Default Value: 1

		reffreq:	Reference frequency (nterms &gt; 1),\'\' uses central data-frequency
		   Default Value: 

		chaniter:	Clean each channel to completion (True), or all channels each cycle (False)
		   Default Value: False

		flatnoise:	Controls whether searching for clean components is done in a constant noise residual image (True) or in an optimal signal-to-noise residual image (False) 
		   Default Value: True

		allowchunk:	Divide large image cubes into channel chunks for deconvolution 
		   Default Value: False

	Returns: void

	Example :

  
        """
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals
	#casac = self.__globals__['casac']
	casalog = self.__globals__['casalog']
	casa = self.__globals__['casa']
	#casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'ptclean'
        self.__globals__['taskname'] = 'ptclean'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
        if type(self.__call__.func_defaults) is NoneType:
            function_signature_defaults={}
	else:
	    function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames[1:],self.__call__.func_defaults))
	useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
			if (key != 'self') :
			   useLocalDefaults = True

	myparams = {}
	if useLocalDefaults :
	   for item in function_signature_defaults.iteritems():
	       key,val = item
	       keyVal = eval(key)
	       exec('myparams[key] = keyVal')
	       self.parameters[key] = keyVal
	       if (keyVal == None):
	           exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
		   keyVal = eval(key)
		   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
		         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
		      else :
		         exec('myparams[key] = ' + key + ' = {}')
	 
        else :
            print ''

            myparams['vis'] = vis = self.parameters['vis']
            myparams['imageprefix'] = imageprefix = self.parameters['imageprefix']
            myparams['ncpu'] = ncpu = self.parameters['ncpu']
            myparams['twidth'] = twidth = self.parameters['twidth']
            myparams['doreg'] = doreg = self.parameters['doreg']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['ephemfile'] = ephemfile = self.parameters['ephemfile']
            myparams['msinfofile'] = msinfofile = self.parameters['msinfofile']
            myparams['outlierfile'] = outlierfile = self.parameters['outlierfile']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['mode'] = mode = self.parameters['mode']
            myparams['resmooth'] = resmooth = self.parameters['resmooth']
            myparams['gridmode'] = gridmode = self.parameters['gridmode']
            myparams['wprojplanes'] = wprojplanes = self.parameters['wprojplanes']
            myparams['facets'] = facets = self.parameters['facets']
            myparams['cfcache'] = cfcache = self.parameters['cfcache']
            myparams['rotpainc'] = rotpainc = self.parameters['rotpainc']
            myparams['painc'] = painc = self.parameters['painc']
            myparams['aterm'] = aterm = self.parameters['aterm']
            myparams['psterm'] = psterm = self.parameters['psterm']
            myparams['mterm'] = mterm = self.parameters['mterm']
            myparams['wbawp'] = wbawp = self.parameters['wbawp']
            myparams['conjbeams'] = conjbeams = self.parameters['conjbeams']
            myparams['epjtable'] = epjtable = self.parameters['epjtable']
            myparams['interpolation'] = interpolation = self.parameters['interpolation']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['gain'] = gain = self.parameters['gain']
            myparams['threshold'] = threshold = self.parameters['threshold']
            myparams['psfmode'] = psfmode = self.parameters['psfmode']
            myparams['imagermode'] = imagermode = self.parameters['imagermode']
            myparams['ftmachine'] = ftmachine = self.parameters['ftmachine']
            myparams['mosweight'] = mosweight = self.parameters['mosweight']
            myparams['scaletype'] = scaletype = self.parameters['scaletype']
            myparams['multiscale'] = multiscale = self.parameters['multiscale']
            myparams['negcomponent'] = negcomponent = self.parameters['negcomponent']
            myparams['smallscalebias'] = smallscalebias = self.parameters['smallscalebias']
            myparams['interactive'] = interactive = self.parameters['interactive']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['nchan'] = nchan = self.parameters['nchan']
            myparams['start'] = start = self.parameters['start']
            myparams['width'] = width = self.parameters['width']
            myparams['outframe'] = outframe = self.parameters['outframe']
            myparams['veltype'] = veltype = self.parameters['veltype']
            myparams['imsize'] = imsize = self.parameters['imsize']
            myparams['cell'] = cell = self.parameters['cell']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['weighting'] = weighting = self.parameters['weighting']
            myparams['robust'] = robust = self.parameters['robust']
            myparams['uvtaper'] = uvtaper = self.parameters['uvtaper']
            myparams['outertaper'] = outertaper = self.parameters['outertaper']
            myparams['innertaper'] = innertaper = self.parameters['innertaper']
            myparams['modelimage'] = modelimage = self.parameters['modelimage']
            myparams['restoringbeam'] = restoringbeam = self.parameters['restoringbeam']
            myparams['pbcor'] = pbcor = self.parameters['pbcor']
            myparams['minpb'] = minpb = self.parameters['minpb']
            myparams['usescratch'] = usescratch = self.parameters['usescratch']
            myparams['noise'] = noise = self.parameters['noise']
            myparams['npixels'] = npixels = self.parameters['npixels']
            myparams['npercycle'] = npercycle = self.parameters['npercycle']
            myparams['cyclefactor'] = cyclefactor = self.parameters['cyclefactor']
            myparams['cyclespeedup'] = cyclespeedup = self.parameters['cyclespeedup']
            myparams['nterms'] = nterms = self.parameters['nterms']
            myparams['reffreq'] = reffreq = self.parameters['reffreq']
            myparams['chaniter'] = chaniter = self.parameters['chaniter']
            myparams['flatnoise'] = flatnoise = self.parameters['flatnoise']
            myparams['allowchunk'] = allowchunk = self.parameters['allowchunk']

        if type(multiscale)==int: multiscale=[multiscale]
        if type(imsize)==int: imsize=[imsize]
        if type(cell)==float: cell=[cell]
        if type(outertaper)==str: outertaper=[outertaper]
        if type(innertaper)==str: innertaper=[innertaper]
        if type(restoringbeam)==str: restoringbeam=[restoringbeam]

	result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['imageprefix'] = imageprefix
        mytmp['ncpu'] = ncpu
        mytmp['twidth'] = twidth
        mytmp['doreg'] = doreg
        mytmp['overwrite'] = overwrite
        mytmp['ephemfile'] = ephemfile
        mytmp['msinfofile'] = msinfofile
        mytmp['outlierfile'] = outlierfile
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['mode'] = mode
        mytmp['resmooth'] = resmooth
        mytmp['gridmode'] = gridmode
        mytmp['wprojplanes'] = wprojplanes
        mytmp['facets'] = facets
        mytmp['cfcache'] = cfcache
        mytmp['rotpainc'] = rotpainc
        mytmp['painc'] = painc
        mytmp['aterm'] = aterm
        mytmp['psterm'] = psterm
        mytmp['mterm'] = mterm
        mytmp['wbawp'] = wbawp
        mytmp['conjbeams'] = conjbeams
        mytmp['epjtable'] = epjtable
        mytmp['interpolation'] = interpolation
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        if type(threshold) == str :
           mytmp['threshold'] = casac.casac.qa.quantity(threshold)
        else :
           mytmp['threshold'] = threshold
        mytmp['psfmode'] = psfmode
        mytmp['imagermode'] = imagermode
        mytmp['ftmachine'] = ftmachine
        mytmp['mosweight'] = mosweight
        mytmp['scaletype'] = scaletype
        mytmp['multiscale'] = multiscale
        mytmp['negcomponent'] = negcomponent
        mytmp['smallscalebias'] = smallscalebias
        mytmp['interactive'] = interactive
        mytmp['mask'] = mask
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['imsize'] = imsize
        if type(cell) == str :
           mytmp['cell'] = casac.casac.qa.quantity(cell)
        else :
           mytmp['cell'] = cell
        mytmp['phasecenter'] = phasecenter
        mytmp['restfreq'] = restfreq
        mytmp['stokes'] = stokes
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['uvtaper'] = uvtaper
        mytmp['outertaper'] = outertaper
        mytmp['innertaper'] = innertaper
        mytmp['modelimage'] = modelimage
        mytmp['restoringbeam'] = restoringbeam
        mytmp['pbcor'] = pbcor
        mytmp['minpb'] = minpb
        mytmp['usescratch'] = usescratch
        mytmp['noise'] = noise
        mytmp['npixels'] = npixels
        mytmp['npercycle'] = npercycle
        mytmp['cyclefactor'] = cyclefactor
        mytmp['cyclespeedup'] = cyclespeedup
        mytmp['nterms'] = nterms
        mytmp['reffreq'] = reffreq
        mytmp['chaniter'] = chaniter
        mytmp['flatnoise'] = flatnoise
        mytmp['allowchunk'] = allowchunk
	pathname="file:///Users/fisher/PycharmProjects/suncasa/tasks/"
	trec = casac.casac.utils().torecord(pathname+'ptclean.xml')

        casalog.origin('ptclean')
	try :
          #if not trec.has_key('ptclean') or not casac.casac.utils().verify(mytmp, trec['ptclean']) :
	    #return False

          casac.casac.utils().verify(mytmp, trec['ptclean'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('ptclean', 'ptclean.last', myparams, self.__globals__,scriptstr=scriptstr)
          tname = 'ptclean'
          spaces = ' '*(18-len(tname))
          casalog.post('\n##########################################'+
                       '\n##### Begin Task: ' + tname + spaces + ' #####')
          if type(self.__call__.func_defaults) is NoneType:
              casalog.post(scriptstr[0]+'\n', 'INFO')
          else :
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')
          result = ptclean(vis, imageprefix, ncpu, twidth, doreg, overwrite, ephemfile, msinfofile, outlierfile, field, spw, selectdata, timerange, uvrange, antenna, scan, observation, intent, mode, resmooth, gridmode, wprojplanes, facets, cfcache, rotpainc, painc, aterm, psterm, mterm, wbawp, conjbeams, epjtable, interpolation, niter, gain, threshold, psfmode, imagermode, ftmachine, mosweight, scaletype, multiscale, negcomponent, smallscalebias, interactive, mask, nchan, start, width, outframe, veltype, imsize, cell, phasecenter, restfreq, stokes, weighting, robust, uvtaper, outertaper, innertaper, modelimage, restoringbeam, pbcor, minpb, usescratch, noise, npixels, npercycle, cyclefactor, cyclespeedup, nterms, reffreq, chaniter, flatnoise, allowchunk)
          casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                       '\n##########################################')

	except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
	     tname = 'ptclean'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass

        gc.collect()
        return result
#
#
#
    def paramgui(self, useGlobals=True, ipython_globals=None):
        """
        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
        """
        import paramgui
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals

        if useGlobals:
	    if ipython_globals == None:
                myf=self.__globals__
            else:
                myf=ipython_globals

            paramgui.setGlobals(myf)
        else:
            paramgui.setGlobals({})

        paramgui.runTask('ptclean', myf['_ip'])
        paramgui.setGlobals({})

#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['vis']  = ''
        a['imageprefix']  = ''
        a['ncpu']  = 8
        a['twidth']  = 1
        a['doreg']  = False
        a['overwrite']  = False
        a['outlierfile']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['selectdata']  = True
        a['mode']  = 'mfs'
        a['gridmode']  = ''
        a['niter']  = 500
        a['gain']  = 0.1
        a['threshold']  = '0.0mJy'
        a['psfmode']  = 'clark'
        a['imagermode']  = 'csclean'
        a['multiscale']  = [0]
        a['interactive']  = False
        a['mask']  = []
        a['imsize']  = [256, 256]
        a['cell']  = ['1.0arcsec']
        a['phasecenter']  = ''
        a['restfreq']  = ''
        a['stokes']  = 'I'
        a['weighting']  = 'natural'
        a['uvtaper']  = False
        a['modelimage']  = ''
        a['restoringbeam']  = ['']
        a['pbcor']  = False
        a['minpb']  = 0.2
        a['usescratch']  = False
        a['allowchunk']  = False

        a['doreg'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'ephemfile':''}, {'msinfofile':''}])}
        a['selectdata'] = {
                    0:odict([{'value':True}, {'timerange':''}, {'uvrange':''}, {'antenna':''}, {'scan':''}, {'observation':''}, {'intent':''}]), 
                    1:{'value':False}}
        a['multiscale'] = {
                    0:odict([{'notvalue':[]}, {'negcomponent':-1}, {'smallscalebias':0.6}])}
        a['gridmode'] = {
                    0:{'value':''}, 
                    1:odict([{'value':'widefield'}, {'wprojplanes':-1}, {'facets':1}]), 
                    2:odict([{'value':'aprojection'}, {'wprojplanes':1}, {'cfcache':'cfcache.dir'}, {'rotpainc':5.0}, {'painc':360.0}]), 
                    3:odict([{'value':'advancedaprojection'}, {'wprojplanes':1}, {'cfcache':'cfcache.dir'}, {'rotpainc':5.0}, {'painc':360.0}, {'wbawp':False}, {'conjbeams':True}, {'aterm':True}, {'psterm':True}, {'mterm':True}, {'epjtable':''}])}
        a['mode'] = {
                    0:odict([{'value':'mfs'}, {'nterms':1}, {'reffreq':''}]), 
                    1:odict([{'value':'channel'}, {'nchan':-1}, {'start':''}, {'width':1}, {'interpolation':'linear'}, {'resmooth':False}, {'chaniter':False}, {'outframe':''}]), 
                    2:odict([{'value':'velocity'}, {'nchan':-1}, {'start':''}, {'width':''}, {'interpolation':'linear'}, {'resmooth':False}, {'chaniter':False}, {'outframe':''}, {'veltype':'radio'}]), 
                    3:odict([{'value':'frequency'}, {'nchan':-1}, {'start':''}, {'width':''}, {'interpolation':'linear'}, {'resmooth':False}, {'chaniter':False}, {'outframe':''}])}
        a['weighting'] = {
                    0:{'value':'natural'}, 
                    1:{'value':'uniform'}, 
                    2:odict([{'value':'briggs'}, {'robust':0.0}, {'npixels':0}]), 
                    3:odict([{'value':'briggsabs'}, {'robust':0.0}, {'noise':'1.0Jy'}, {'npixels':0}]), 
                    4:odict([{'value':'superuniform'}, {'npixels':0}])}
        a['uvtaper'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'outertaper':[]}, {'innertaper':[]}])}
        a['interactive'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'npercycle':100}])}
        a['imagermode'] = {
                    0:odict([{'value':'csclean'}, {'cyclefactor':1.5}, {'cyclespeedup':-1}]), 
                    1:odict([{'value':'mosaic'}, {'mosweight':False}, {'ftmachine':'mosaic'}, {'scaletype':'SAULT'}, {'cyclefactor':1.5}, {'cyclespeedup':-1}, {'flatnoise':True}]), 
                    2:{'value':''}}

### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
		     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='ptclean', subkey=None):
        desc={'ptclean': 'Parallelized clean in consecutive time steps',
               'vis': 'Name of input visibility file',
               'imageprefix': 'Prefix of image names (may include the path)',
               'ncpu': 'Number of cpu cores to use',
               'twidth': 'Number of time pixels to average',
               'doreg': 'True if use vla_prep to register the image',
               'overwrite': 'True if overwrite the image',
               'ephemfile': 'emphemeris file generated from vla_prep.read_horizons()',
               'msinfofile': 'time-dependent phase center information generated from vla_prep.read_msinfo()',
               'outlierfile': 'Text file with image names, sizes, centers for outliers',
               'field': 'Field Name or id',
               'spw': 'Spectral windows e.g. \'0~3\', \'\' is all',
               'selectdata': 'Other data selection parameters',
               'timerange': 'Range of time to select from data',
               'uvrange': 'Select data within uvrange ',
               'antenna': 'Select data based on antenna/baseline',
               'scan': 'Scan number range',
               'observation': 'Observation ID range',
               'intent': 'Scan Intent(s)',
               'mode': 'Spectral gridding type (mfs, channel, velocity, frequency)',
               'resmooth': 'Re-restore the cube image to a common beam when True',
               'gridmode': 'Gridding kernel for FFT-based transforms, default=\'\' None',
               'wprojplanes': 'Number of w-projection planes for convolution; -1 => automatic determination ',
               'facets': 'Number of facets along each axis (main image only)',
               'cfcache': 'Convolution function cache directory',
               'rotpainc': 'Parallactic angle increment (degrees) for OTF A-term rotation',
               'painc': 'Parallactic angle increment (degrees) for computing A-term',
               'aterm': 'Switch-on the A-Term?',
               'psterm': 'Switch-on the PS-Term?',
               'mterm': 'Switch-on the M-Term?',
               'wbawp': 'Trigger the wide-band A-Projection algorithm?',
               'conjbeams': 'Use frequency conjugate beams in WB A-Projection algorithm?',
               'epjtable': 'Table of EP-Jones parameters',
               'interpolation': 'Spectral interpolation (nearest, linear, cubic). ',
               'niter': 'Maximum number of iterations',
               'gain': 'Loop gain for cleaning',
               'threshold': 'Flux level to stop cleaning, must include units: \'1.0mJy\'',
               'psfmode': 'Method of PSF calculation to use during minor cycles',
               'imagermode': 'Options: \'csclean\' or \'mosaic\', \'\', uses psfmode',
               'ftmachine': 'Gridding method for the image',
               'mosweight': 'Individually weight the fields of the mosaic',
               'scaletype': 'Controls scaling of pixels in the image plane. default=\'SAULT\'; example: scaletype=\'PBCOR\' Options: \'PBCOR\',\'SAULT\'',
               'multiscale': 'Deconvolution scales (pixels); [] = standard clean',
               'negcomponent': 'Stop cleaning if the largest scale finds this number of neg components',
               'smallscalebias': 'a bias to give more weight toward smaller scales',
               'interactive': 'Use interactive clean (with GUI viewer)',
               'mask': 'Cleanbox(es), mask image(s), region(s), or a level',
               'nchan': 'Number of channels (planes) in output image; -1 = all',
               'start': 'start of output spectral dimension',
               'width': 'width of output spectral channels',
               'outframe': 'default spectral frame of output image ',
               'veltype': 'velocity definition (radio, optical, true) ',
               'imsize': 'x and y image size in pixels.  Single value: same for both',
               'cell': 'x and y cell size(s). Default unit arcsec.',
               'phasecenter': 'Image center: direction or field index',
               'restfreq': 'Rest frequency to assign to image (see help)',
               'stokes': 'Stokes params to image (eg I,IV,IQ,IQUV)',
               'weighting': 'Weighting of uv (natural, uniform, briggs, ...)',
               'robust': 'Briggs robustness parameter',
               'uvtaper': 'Apply additional uv tapering of visibilities',
               'outertaper': 'uv-taper on outer baselines in uv-plane',
               'innertaper': 'uv-taper in center of uv-plane (not implemented)',
               'modelimage': 'Name of model image(s) to initialize cleaning',
               'restoringbeam': 'Output Gaussian restoring beam for CLEAN image',
               'pbcor': 'Output primary beam-corrected image',
               'minpb': 'Minimum PB level to use',
               'usescratch': 'True if to save model visibilities in MODEL_DATA column',
               'noise': 'noise parameter for briggs abs mode weighting',
               'npixels': 'number of pixels for superuniform or briggs weighting',
               'npercycle': 'Clean iterations before interactive prompt (can be changed)',
               'cyclefactor': 'Controls how often major cycles are done. (e.g. 5 for frequently)',
               'cyclespeedup': 'Cycle threshold doubles in this number of iterations',
               'nterms': 'Number of Taylor coefficients to model the sky frequency dependence ',
               'reffreq': 'Reference frequency (nterms > 1),\'\' uses central data-frequency',
               'chaniter': 'Clean each channel to completion (True), or all channels each cycle (False)',
               'flatnoise': 'Controls whether searching for clean components is done in a constant noise residual image (True) or in an optimal signal-to-noise residual image (False) ',
               'allowchunk': 'Divide large image cubes into channel chunks for deconvolution ',

              }

#
# Set subfields defaults if needed
#
        if(subkey == 'channel'):
          desc['start'] = 'Begin the output cube at the frequency of this channel in the MS'
        if(subkey == 'channel'):
          desc['width'] = 'Width of output channel relative to MS channel (# to average)'
        if(subkey == 'velocity'):
          desc['start'] = 'Velocity of first channel: e.g \'0.0km/s\'(\'\'=first channel in first SpW of MS)'
        if(subkey == 'velocity'):
          desc['width'] = 'Channel width e.g \'-1.0km/s\' (\'\'=width of first channel in first SpW of MS)'
        if(subkey == 'velocity'):
          desc['outframe'] = 'spectral reference frame of output image; \'\' =input'
        if(subkey == 'velocity'):
          desc['veltype'] = 'Velocity definition of output image'
        if(subkey == 'frequency'):
          desc['start'] = 'Frequency of first channel: e.g. \'1.4GHz\' (\'\'= first channel in first SpW of MS)'
        if(subkey == 'frequency'):
          desc['width'] = 'Channel width: e.g \'1.0kHz\'(\'\'=width of first channel in first SpW of MS)'
        if(subkey == 'briggs'):
          desc['npixels'] = 'number of pixels to determine uv-cell size 0=> field of view'
        if(subkey == 'briggsabs'):
          desc['npixels'] = 'number of pixels to determine uv-cell size 0=> field of view'
        if(subkey == 'superuniform'):
          desc['npixels'] = 'number of pixels to determine uv-cell size 0=> +/-3pixels'

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['imageprefix']  = ''
        a['ncpu']  = 8
        a['twidth']  = 1
        a['doreg']  = False
        a['overwrite']  = False
        a['ephemfile']  = ''
        a['msinfofile']  = ''
        a['outlierfile']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['selectdata']  = True
        a['timerange']  = ''
        a['uvrange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['observation']  = ''
        a['intent']  = ''
        a['mode']  = 'mfs'
        a['resmooth']  = False
        a['gridmode']  = ''
        a['wprojplanes']  = -1
        a['facets']  = 1
        a['cfcache']  = 'cfcache.dir'
        a['rotpainc']  = 5.0
        a['painc']  = 360.0
        a['aterm']  = True
        a['psterm']  = False
        a['mterm']  = True
        a['wbawp']  = False
        a['conjbeams']  = True
        a['epjtable']  = ''
        a['interpolation']  = 'linear'
        a['niter']  = 500
        a['gain']  = 0.1
        a['threshold']  = '0.0mJy'
        a['psfmode']  = 'clark'
        a['imagermode']  = 'csclean'
        a['ftmachine']  = 'mosaic'
        a['mosweight']  = False
        a['scaletype']  = 'SAULT'
        a['multiscale']  = [0]
        a['negcomponent']  = -1
        a['smallscalebias']  = 0.6
        a['interactive']  = False
        a['mask']  = []
        a['nchan']  = -1
        a['start']  = 0
        a['width']  = 1
        a['outframe']  = ''
        a['veltype']  = 'radio'
        a['imsize']  = [256, 256]
        a['cell']  = ['1.0arcsec']
        a['phasecenter']  = ''
        a['restfreq']  = ''
        a['stokes']  = 'I'
        a['weighting']  = 'natural'
        a['robust']  = 0.0
        a['uvtaper']  = False
        a['outertaper']  = ['']
        a['innertaper']  = ['1.0']
        a['modelimage']  = ''
        a['restoringbeam']  = ['']
        a['pbcor']  = False
        a['minpb']  = 0.2
        a['usescratch']  = False
        a['noise']  = '1.0Jy'
        a['npixels']  = 0
        a['npercycle']  = 100
        a['cyclefactor']  = 1.5
        a['cyclespeedup']  = -1
        a['nterms']  = 1
        a['reffreq']  = ''
        a['chaniter']  = False
        a['flatnoise']  = True
        a['allowchunk']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['doreg']  == True:
            a['ephemfile'] = ''
            a['msinfofile'] = ''

        if self.parameters['selectdata']  == True:
            a['timerange'] = ''
            a['uvrange'] = ''
            a['antenna'] = ''
            a['scan'] = ''
            a['observation'] = ''
            a['intent'] = ''

        if self.parameters['multiscale']  != []:
            a['negcomponent'] = -1
            a['smallscalebias'] = 0.6

        if self.parameters['gridmode']  == 'widefield':
            a['wprojplanes'] = -1
            a['facets'] = 1

        if self.parameters['gridmode']  == 'aprojection':
            a['wprojplanes'] = 1
            a['cfcache'] = 'cfcache.dir'
            a['rotpainc'] = 5.0
            a['painc'] = 360.0

        if self.parameters['gridmode']  == 'advancedaprojection':
            a['wprojplanes'] = 1
            a['cfcache'] = 'cfcache.dir'
            a['rotpainc'] = 5.0
            a['painc'] = 360.0
            a['wbawp'] = False
            a['conjbeams'] = True
            a['aterm'] = True
            a['psterm'] = True
            a['mterm'] = True
            a['epjtable'] = ''

        if self.parameters['mode']  == 'mfs':
            a['nterms'] = 1
            a['reffreq'] = ''

        if self.parameters['mode']  == 'channel':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = 1
            a['interpolation'] = 'linear'
            a['resmooth'] = False
            a['chaniter'] = False
            a['outframe'] = ''

        if self.parameters['mode']  == 'velocity':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['interpolation'] = 'linear'
            a['resmooth'] = False
            a['chaniter'] = False
            a['outframe'] = ''
            a['veltype'] = 'radio'

        if self.parameters['mode']  == 'frequency':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['interpolation'] = 'linear'
            a['resmooth'] = False
            a['chaniter'] = False
            a['outframe'] = ''

        if self.parameters['weighting']  == 'briggs':
            a['robust'] = 0.0
            a['npixels'] = 0

        if self.parameters['weighting']  == 'briggsabs':
            a['robust'] = 0.0
            a['noise'] = '1.0Jy'
            a['npixels'] = 0

        if self.parameters['weighting']  == 'superuniform':
            a['npixels'] = 0

        if self.parameters['uvtaper']  == True:
            a['outertaper'] = []
            a['innertaper'] = []

        if self.parameters['interactive']  == True:
            a['npercycle'] = 100

        if self.parameters['imagermode']  == 'csclean':
            a['cyclefactor'] = 1.5
            a['cyclespeedup'] = -1

        if self.parameters['imagermode']  == 'mosaic':
            a['mosweight'] = False
            a['ftmachine'] = 'mosaic'
            a['scaletype'] = 'SAULT'
            a['cyclefactor'] = 1.5
            a['cyclespeedup'] = -1
            a['flatnoise'] = True

        if a.has_key(paramname) :
	      return a[paramname]
ptclean_cli = ptclean_cli_()
