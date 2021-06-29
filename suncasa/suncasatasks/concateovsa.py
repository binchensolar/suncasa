##################### generated by xml-casa (v2) from concateovsa.xml ###############
##################### 954e1152e2b92508e6b19a5f6d392669 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from .private.task_concateovsa import concateovsa as _concateovsa_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log

class _concateovsa:
    """
    concateovsa ---- Concatenate several EOVSA visibility data sets.

    
    This is a EOVSA version of CASA concat task.
    
    The list of data sets given in the vis argument are chronologically concatenated
    into an output data set in concatvis, i.e. the data sets in vis are first ordered
    by the time of their earliest integration and then concatenated.
    
    If there are fields whose direction agrees within the direction tolerance
    (parameter dirtol), the actual direction in the resulting, merged output field
    will be the one from the chronologically first input MS.
    
    If concatvis already exists (e.g., it is the same as the first input data set),
    then the other input data sets will be appended to the concatvis data set.
    There is no limit to the number of input data sets.
    
    If none of the input data sets have any scratch columns (model and corrected
    columns), none are created in the concatvis. Otherwise these columns are
    created on output and initialized to their default value (1 in model column,
    data in corrected column) for those data with no input columns.
    
    Spectral windows for each data set with the same chanelization, and within a
    specified frequency tolerance of another data set will be combined into one
    spectral window.
    
    A field position in one data set that is within a specified direction tolerance
    of another field position in any other data set will be combined into one
    field. The field names need not be the same---only their position is used.
    
    Each appended dataset is assigned a new observation id (provided the entries
    in the observation table are indeed different).
    
    Keyword arguments:
    vis -- Name of input visibility files to be combined
    default: none; example: vis = ['src2.ms','ngc5921.ms','ngc315.ms']
    concatvis -- Name of visibility file that will contain the concatenated data
    note: if this file exits on disk then the input files are
    added to this file. Otherwise the new file contains
    the concatenated data. Be careful here when concatenating to
    an existing file.
    default: none; example: concatvis='src2.ms'
    example: concatvis='outvis.ms'
    
    datacolumn -- Which data column to use for processing (case-insensitive).
    default: 'corrected'; example: datacolumn='data'
    options: 'data', 'corrected'.
    
    freqtol -- Frequency shift tolerance for considering data to be in the same
    spwid. The number of channels must also be the same.
    default: '' == 1 Hz
    example: freqtol='10MHz' will not combine spwid unless they are
    within 10 MHz.
    Note: This option is useful to combine spectral windows with very slight
    frequency differences caused by Doppler tracking, for example.
    
    dirtol -- Direction shift tolerance for considering data as the same field
    default: '' == 1 mas (milliarcsec)
    example: dirtol='1arcsec' will not combine data for a field unless
    their phase center differ by less than 1 arcsec. If the field names
    are different in the input data sets, the name in the output data
    set will be the first relevant data set in the list.
    
    respectname -- If true, fields with a different name are not merged even if their
    direction agrees (within dirtol)
    default: False
    
    timesort -- If true, the output visibility table will be sorted in time.
    default: false. Data in order as read in.
    example: timesort=true
    Note: There is no constraint on data that is simultaneously observed for
    more than one field; for example multi-source correlation of VLBA data.
    
    copypointing -- Make a proper copy of the POINTING subtable (can be time consuming).
    If False, the result is an empty POINTING table.
    default: True
    
    visweightscale -- The weights of the individual MSs will be scaled in the concatenated
    output MS by the factors in this list. SIGMA will be scaled by 1/sqrt(factor).
    Useful for handling heterogeneous arrays.
    Use plotms to inspect the "Wt" column as a reference for determining the scaling
    factors. See the cookbook for more details.
    example: [1.,3.,3.] - scale the weights of the second and third MS by a factor 3
    and the SIGMA column of these MS by a factor 1/sqrt(3).
    default: [] (empty list) - no scaling
    
    forcesingleephemfield -- By default, concat will only merge two ephemeris fields if
    the first ephemeris covers the time range of the second. Otherwise, two separate
    fields with separate ephemerides are placed in the output MS.
    In order to override this behaviour and make concat merge the non-overlapping
    or only partially overlapping input ephemerides, the name or id of the field
    in question needs to be placed into the list in parameter 'forcesingleephemfield'.
    example: ['Neptune'] - will make sure that there is only one joint ephemeris for
    field Neptune in the output MS
    default: '' - standard treatment of all ephemeris fields
    
    

    --------- parameter descriptions ---------------------------------------------

    vis                   Name of input visibility files to be concatenated
    concatvis             Name of output visibility file
    datacolumn            Which data column(s) to concatenate
    keep_orig_ms          If false, input vis files will be removed
    cols2rm               Columns in concatvis to be removed to slim the concatvis
    freqtol               Frequency shift tolerance for considering data as the same spwid
    dirtol                Direction shift tolerance for considering data as the same field
    respectname           If true, fields with a different name are not merged even if their direction agrees
    timesort              If true, sort by TIME in ascending order
    copypointing          Copy all rows of the POINTING table.
    visweightscale        List of the weight scaling factors to be applied to the individual MSs
    forcesingleephemfield make sure that there is only one joint ephemeris for every field in this list

    --------- examples -----------------------------------------------------------

    
    concateovsa(vis=['UDB20180102161402.ms','UDB20180102173518.ms'], concatvis='UDB20180102_allday.ms')
    will concatenate 'UDB20180102161402.ms' and 'UDB20180102173518.ms' into 'UDB20180102_allday.ms'
    


    """

    _info_group_ = """utility, manipulation"""
    _info_desc_ = """Concatenate several EOVSA visibility data sets."""

    def __call__( self, vis='', concatvis='', datacolumn='corrected', keep_orig_ms=True, cols2rm='model,corrected', freqtol='', dirtol='', respectname=False, timesort=True, copypointing=True, visweightscale=[  ], forcesingleephemfield='' ):
        schema = {'vis': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'concatvis': {'type': 'cStr', 'coerce': _coerce.to_str}, 'datacolumn': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'corrected', 'data', 'CORRECTED', 'DATA' ]}, 'keep_orig_ms': {'type': 'cBool'}, 'cols2rm': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'model', 'corrected', 'CORRECTED', 'MODEL,CORRECTED', 'model,corrected', 'MODEL' ]}, 'freqtol': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'dirtol': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'respectname': {'type': 'cBool'}, 'timesort': {'type': 'cBool'}, 'copypointing': {'type': 'cBool'}, 'visweightscale': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'forcesingleephemfield': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}}
        doc = {'vis': vis, 'concatvis': concatvis, 'datacolumn': datacolumn, 'keep_orig_ms': keep_orig_ms, 'cols2rm': cols2rm, 'freqtol': freqtol, 'dirtol': dirtol, 'respectname': respectname, 'timesort': timesort, 'copypointing': copypointing, 'visweightscale': visweightscale, 'forcesingleephemfield': forcesingleephemfield}
        assert _pc.validate(doc,schema), str(_pc.errors)
        _logging_state_ = _start_log( 'concateovsa', [ 'vis=' + repr(_pc.document['vis']), 'concatvis=' + repr(_pc.document['concatvis']), 'datacolumn=' + repr(_pc.document['datacolumn']), 'keep_orig_ms=' + repr(_pc.document['keep_orig_ms']), 'cols2rm=' + repr(_pc.document['cols2rm']), 'freqtol=' + repr(_pc.document['freqtol']), 'dirtol=' + repr(_pc.document['dirtol']), 'respectname=' + repr(_pc.document['respectname']), 'timesort=' + repr(_pc.document['timesort']), 'copypointing=' + repr(_pc.document['copypointing']), 'visweightscale=' + repr(_pc.document['visweightscale']), 'forcesingleephemfield=' + repr(_pc.document['forcesingleephemfield']) ] )
        return _end_log( _logging_state_, 'concateovsa', _concateovsa_t( _pc.document['vis'], _pc.document['concatvis'], _pc.document['datacolumn'], _pc.document['keep_orig_ms'], _pc.document['cols2rm'], _pc.document['freqtol'], _pc.document['dirtol'], _pc.document['respectname'], _pc.document['timesort'], _pc.document['copypointing'], _pc.document['visweightscale'], _pc.document['forcesingleephemfield'] ) )

concateovsa = _concateovsa( )

