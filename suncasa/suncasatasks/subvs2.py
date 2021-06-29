##################### generated by xml-casa (v2) from subvs2.xml ####################
##################### 732860b3e815b8382e2550311845c0c7 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from .private.task_subvs2 import subvs2 as _subvs2_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log

class _subvs2:
    """
    subvs2 ---- Vector-subtraction in UV using selected time ranges and spectral channels as background

    
    
    
    Split is the general purpose program to make a new data set that is a
    subset or averaged form of an existing data set.  General selection
    parameters are included, and one or all of the various data columns
    (DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
    CORRECTED_DATA) can be selected.
    
    Split is often used after the initial calibration of the data to make a
    smaller measurement set with only the data that will be used in
    further flagging, imaging and/or self-calibration.  split can
    average over frequency (channels) and time (integrations).

    --------- parameter descriptions ---------------------------------------------

    vis         Name of input measurement set
    outputvis   Name of output measurement set
    timerange   Select the time range of the input visbility to be subtracted from
    spw         Select the spectral channels of the input visibility to be subtracted from
    mode        Operation: linear, highpass
    subtime1    Select the first time range as the background for uv subtraction
    subtime2    Select the second time range as the background for uv subtraction
    smoothaxis  Select the axis along which smooth is performed
    smoothtype  Select the smooth type
    smoothwidth Select the width of the smoothing window
    splitsel    Split the selected timerange and spectral channels as outputvis
    reverse     Reverse the sign of the background-subtracted data (for absorptive structure)
    overwrite   Overwrite the already existing output measurement set

    --------- examples -----------------------------------------------------------

    
    
    Subvs is a task to do UV vector-subtraction, by selecting time ranges
    in the data as background. Subvs can be used to subtract the background
    continuum emission to separate the time-dependent emission, e.g. solar
    coherent radio bursts.
    
    Keyword arguments:
    vis -- Name of input visibility file (MS)
    default: none; example: vis='ngc5921.ms'
    outputvis -- Name of output uv-subtracted visibility file (MS)
    default: none; example: outputvis='ngc5921_src.ms'
    timerange -- Time range of performing the UV subtraction:
    default='' means all times.  examples:
    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
    timerange = 'hh:mm:ss~hh:mm:ss'
    spw -- Select spectral window/channel.
    default = '' all the spectral channels. Example: spw='0:1~20'
    mode -- operation mode
    default 'linear'
    mode = 'linear': use a linear fit for the background to be subtracted
    mode = 'lowpass': act as a lowpass filter---smooth the data using different smooth
    types and smooth window size. Can be performed along either time
    or frequency axis
    mode = 'highpass': act as a highpass filter---smooth the data first, and
    subtract the smoothed data from the original. Can be performed along either time
    or frequency axis
    mode = 'linear' expandable parameters:
    subtime1 -- Time range 1 of the background to be subtracted from the data
    default='' means all times.  format:
    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
    timerange = 'hh:mm:ss~hh:mm:ss'
    subtime2 -- Time range 2 of the backgroud to be subtracted from the data
    default='' means all times.  examples:
    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
    timerange = 'hh:mm:ss~hh:mm:ss'
    mode = 'lowpass' or 'highpass' expandable parameters:
    smoothaxis -- axis of smooth
    Default: 'time'
    smoothaxis = 'time': smooth is along the time axis
    smoothaxis = 'freq': smooth is along the frequency axis
    smoothtype -- type of the smooth depending on the convolving kernel
    Default: 'flat'
    smoothtype = 'flat': convolving kernel is a flat rectangle,
    equivalent to a boxcar moving smooth
    smoothtype = 'hanning': Hanning smooth kernel. See numpy.hanning
    smoothtype = 'hamming': Hamming smooth kernel. See numpy.hamming
    smoothtype = 'bartlett': Bartlett smooth kernel. See numpy.bartlett
    smoothtype = 'blackman': Blackman smooth kernel. See numpy.blackman
    smoothwidth -- width of the smooth kernel
    Default: 5
    Examples: smoothwidth=5, meaning the width is 5 pixels
    splitsel -- True or False. default = False. If splitsel = False, then the entire input
    measurement set is copied as the output measurement set (outputvis), with
    background subtracted at selected timerange and spectral channels.
    If splitsel = True,then only the selected timerange and spectral channels
    are copied into the output measurement set (outputvis).
    reverse -- True or False. default = False. If reverse = False, then the times indicated
    by subtime1 and/or subtime2 are treated as background and subtracted; If reverse
    = True, then reverse the sign of the background-subtracted data. The option can
    be used for mapping absorptive structure.
    overwrite -- True or False. default = False. If overwrite = True and
    outputvis already exists, the selected subtime and spw in the
    output measurment set will be replaced with background subtracted
    visibilities


    """

    _info_group_ = """misc"""
    _info_desc_ = """Vector-subtraction in UV using selected time ranges and spectral channels as background"""

    def __call__( self, vis='', outputvis='', timerange='', spw='', mode='linear', subtime1='', subtime2='', smoothaxis='time', smoothtype='flat', smoothwidth=int(5), splitsel=True, reverse=False, overwrite=False ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'outputvis': {'type': 'cPath', 'coerce': _coerce.expand_path}, 'timerange': {'type': 'cStr', 'coerce': _coerce.to_str}, 'spw': {'type': 'cStr', 'coerce': _coerce.to_str}, 'mode': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'linear', 'lowpass', 'highpass' ]}, 'subtime1': {'type': 'cStr', 'coerce': _coerce.to_str}, 'subtime2': {'type': 'cStr', 'coerce': _coerce.to_str}, 'smoothaxis': {'type': 'cStr', 'coerce': _coerce.to_str}, 'smoothtype': {'type': 'cStr', 'coerce': _coerce.to_str}, 'smoothwidth': {'type': 'cInt'}, 'splitsel': {'type': 'cBool'}, 'reverse': {'type': 'cBool'}, 'overwrite': {'type': 'cBool'}}
        doc = {'vis': vis, 'outputvis': outputvis, 'timerange': timerange, 'spw': spw, 'mode': mode, 'subtime1': subtime1, 'subtime2': subtime2, 'smoothaxis': smoothaxis, 'smoothtype': smoothtype, 'smoothwidth': smoothwidth, 'splitsel': splitsel, 'reverse': reverse, 'overwrite': overwrite}
        assert _pc.validate(doc,schema), str(_pc.errors)
        _logging_state_ = _start_log( 'subvs2', [ 'vis=' + repr(_pc.document['vis']), 'outputvis=' + repr(_pc.document['outputvis']), 'timerange=' + repr(_pc.document['timerange']), 'spw=' + repr(_pc.document['spw']), 'mode=' + repr(_pc.document['mode']), 'subtime1=' + repr(_pc.document['subtime1']), 'subtime2=' + repr(_pc.document['subtime2']), 'smoothaxis=' + repr(_pc.document['smoothaxis']), 'smoothtype=' + repr(_pc.document['smoothtype']), 'smoothwidth=' + repr(_pc.document['smoothwidth']), 'splitsel=' + repr(_pc.document['splitsel']), 'reverse=' + repr(_pc.document['reverse']), 'overwrite=' + repr(_pc.document['overwrite']) ] )
        return _end_log( _logging_state_, 'subvs2', _subvs2_t( _pc.document['vis'], _pc.document['outputvis'], _pc.document['timerange'], _pc.document['spw'], _pc.document['mode'], _pc.document['subtime1'], _pc.document['subtime2'], _pc.document['smoothaxis'], _pc.document['smoothtype'], _pc.document['smoothwidth'], _pc.document['splitsel'], _pc.document['reverse'], _pc.document['overwrite'] ) )

subvs2 = _subvs2( )

