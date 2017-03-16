import json
import os
import os.path
from sys import platform
import pandas as pd
from bokeh.layouts import row, column, widgetbox
from bokeh.models import (ColumnDataSource, Button, TextInput, DataTable, TableColumn, BoxSelectTool, TapTool,
                          HoverTool, Spacer, Div)
from bokeh.plotting import curdoc
import glob
from astropy.time import Time
import astropy.units as u
import numpy as np
from collections import OrderedDict
from suncasa.utils import DButil


__author__ = ["Sijie Yu"]
__email__ = "sijie.yu@njit.edu"

'''Prepare the ports for FSview'''
# try:
if platform == "linux" or platform == "linux2":
    print 'Runing EvtBrowser in Linux platform'
    # for ll in xrange(5010, 5010 + 10):
    #     os.system('fuser -n tcp -k {}'.format(ll))
elif platform == "darwin":
    print 'Runing EvtBrowser in OS X platform'
    # for ll in xrange(5010, 5010 + 10):
    #     os.system(
    #         'port=($(lsof -i tcp:{}|grep python2.7 |cut -f2 -d" ")); [[ -n "$port" ]] && kill -9 $port'.format(ll))
    #     os.system(
    #         'port=($(lsof -i tcp:{}|grep Google |cut -f2 -d" ")); [[ -n "$port" ]] && kill -9 $port'.format(ll))
elif platform == "win32":
    print 'Runing EvtBrowser in Windows platform'

suncasa_dir = os.path.expandvars("${SUNCASA}") + '/'
'''load config file'''
config_main = DButil.loadjsonfile(suncasa_dir + 'DataBrowser/config.json')
database_dir = os.path.expandvars(config_main['datadir']['database']) + '/'

EvtID_list = pd.read_json(database_dir + config_main['datadir']['EvtID_list'])
EvtID_list = EvtID_list.sort_values(['date'], ascending=[True])

'''
-------------------------- panel 0 --------------------------
'''
tab0_Div_title = Div(text="""
<p><b>Welcome to Event Browser. Select one solar flare event to start. Have fun!</b></p>""",
                     width=config_main['plot_config']['tab_EvtBrowser']['StrID_DataTb_wdth'])

tab0_SRC_Tb_EvtID = ColumnDataSource(EvtID_list)
tab0_TbCols2 = [TableColumn(field="event_id", title="EvtID"), TableColumn(field="timeran", title="Time Range"),
                TableColumn(field="freqran", title="Freq Range"), ]
tab0_DataTb_evt = DataTable(source=tab0_SRC_Tb_EvtID, columns=tab0_TbCols2,
                            width=config_main['plot_config']['tab_EvtBrowser']['StrID_DataTb_wdth'],
                            height=config_main['plot_config']['tab_EvtBrowser']['StrID_DataTb_hght'])  # , editable=True)
tab0_Div_Tb = Div(text=""" """, width=config_main['plot_config']['tab_QLook']['StrID_DataTb_wdth'])
tab0_Div_exit = Div(text="""
<p><b>Warning</b>: 1. Click the <b>Exit EvtBrowser</b> first before closing the tab</p>
<p><b>Warning</b>: 2. <b>QLook</b> <b>FSview</b> or <b>ToClean</b> tabs will disconnect if <b>Exit EvtBrowser is clicked</b></p>""",
                    width=150)

ports = []

tab0_selected_EvtID_entry = None


def tab0_selection_EvtID_entry(attrname, old, new):
    global tab0_selected_EvtID_entry
    tab0_selected_EvtID_entry = tab0_SRC_Tb_EvtID.selected['1d']['indices']


tab0_SRC_Tb_EvtID.on_change('selected', tab0_selection_EvtID_entry)


def tab0_EvtSel():
    global ports
    if tab0_selected_EvtID_entry:
        EvtID = EvtID_list.iloc[tab0_selected_EvtID_entry[0]]['event_id'][0]
        event_id = EvtID + '/'
        event_id_dir = database_dir + event_id
        if not os.path.exists(event_id_dir):
            os.system('mkdir {}'.format(event_id_dir))
            tab0_Div_Tb.text = """<p>Warning: No <b>dynamic spectrum</b> data found! Create a <b>dynamic spectrum</b> first.</p>"""
        else:
            event_specfile = glob.glob(event_id_dir + '*.spec.npz')
            if len(event_specfile) == 0:
                tab0_Div_Tb.text = """<p>Warning: No <b>dynamic spectrum</b> data found! Create a <b>dynamic spectrum</b> first.</p>"""
            else:
                # if not os.path.exists(event_id_dir + 'config_EvtID.json'):
                config_EvtID = {
                    "datadir": {"dspecDF": "dspecDF-save", "J2000": "J2000/", "fits_LOCL": "Synthesis_Image/local/",
                                "fits_LOCL_init": "QLook/static/Synthesis_Image_fits_LOCL_init.fits",
                                "event_specfile": event_specfile[0].split('/')[-1], "database": "${SUNCASADB}",
                                "event_id": event_id, "fits_GLOB": "Synthesis_Image/global/",
                                "fits_GLOB_init": "QLook/static/Synthesis_Image_fits_GLOB_init.fits"}}
                with open(event_id_dir + 'config_EvtID.json', 'w') as fp:
                    json.dump(config_EvtID, fp)
                os.system('cp {} {}config_EvtID_curr.json'.format(event_id_dir + 'config_EvtID.json', database_dir))
                port = DButil.getfreeport()
                print 'bokeh serve {}DataBrowser/QLook --show --port {} &'.format(suncasa_dir, port)
                os.system('bokeh serve {}DataBrowser/QLook --show --port {} &'.format(suncasa_dir, port))
                ports.append(port)
                tab0_Div_Tb.text = """<p>Event <b>""" + EvtID + """</b> selected. <p>Check the <b>QLook</b> in the <b>new tab</b>.</p>"""
    else:
        tab0_Div_Tb.text = """<p><b>Warning:</b> select a event first!!!</p>"""


tab0_BUT_EvtSel = Button(label='Select', width=150, button_type='success')
tab0_BUT_EvtSel.on_click(tab0_EvtSel)


def tab0_DDownload():
    # import drms
    # c = drms.Client()
    # c = drms.Client(email='sijie.yu@njit.edu', verbose=True)
    # k = c.query('aia.lev1_euv_12s[2012-03-10T12:00:00_TAI/10m@5m][171,94]', key='T_REC,WAVELNTH',seg='image')
    if tab0_selected_EvtID_entry:
        EvtID = EvtID_list.iloc[tab0_selected_EvtID_entry[0]]['event_id'][0]
        event_id = EvtID + '/'
        event_id_dir = database_dir + event_id
        if not os.path.exists(event_id_dir):
            os.system('mkdir {}'.format(event_id_dir))
            tab0_Div_Tb.text = """<p>Warning: No <b>dynamic spectrum</b> data found! Create a <b>dynamic spectrum</b> first.</p>"""
        else:
            event_specfile = glob.glob(event_id_dir + '*.spec.npz')
            if len(event_specfile) == 0:
                tab0_Div_Tb.text = """<p>Warning: No <b>dynamic spectrum</b> data found! Create a <b>dynamic spectrum</b> first.</p>"""
            else:
                tab0_specdata = np.load(event_specfile[0])
                tab0_tim = tab0_specdata['tim'][:]
                tstrstart = Time(tab0_tim[0] / 3600. / 24., format='mjd', scale='utc', precision=3,
                                 out_subfmt='date_hms').iso
                tstrend = Time(tab0_tim[-1] / 3600. / 24., format='mjd', scale='utc', precision=3,
                               out_subfmt='date_hms').iso
                trange = {'aiaBrowser':{'tst':tstrstart,'ted':tstrend}}
                if not os.path.exists(database_dir+'/aiaBrowserData/'):
                    os.makedirs(database_dir+'/aiaBrowserData/')
                with open(database_dir + '/aiaBrowserData/Trange_args.json', 'w') as fp:
                    json.dump(trange, fp)
                port = DButil.getfreeport()
                print 'bokeh serve {}aiaBrowser --show --port {} &'.format(suncasa_dir, port)
                os.system('bokeh serve {}aiaBrowser --show --port {} &'.format(suncasa_dir, port))
                ports.append(port)
                tab0_Div_Tb.text = """<p>Event <b>""" + EvtID + """</b> selected. <p>Check the <b>aiaBrowser</b> in the <b>new tab</b>.</p>"""
    else:
        tab0_Div_Tb.text = """<p><b>Warning:</b> select a event first!!!</p>"""


tab0_BUT_DDownload = Button(label='SDO image fetch', width=150, button_type='primary')
tab0_BUT_DDownload.on_click(tab0_DDownload)


tab0_SPCR_LFT_Div_title = Spacer(width=200, height=10)
tab0_SPCR_RGT_Div_title = Spacer(width=50, height=10)
tab0_SPCR_LFT_DataTb_dspec = Spacer(width=50, height=10)
tab0_SPCR_RGT_DataTb_dspec = Spacer(width=50, height=10)
tab0_SPCR_ABV_DataTb_dspec = Spacer(width=100, height=18)
tab0_SPCR_LFT_But = Spacer(width=10, height=25)
tab0_SPCR_LFT_DataTb_evt = Spacer(width=20, height=15)
tab0_SPCR_ABV_DataTb_evt = Spacer(width=100, height=18)


def tab0_exit():
    tab0_Div_exit.text = """<p><b>You may close the tab anytime you like.</b></p>"""
    print 'You may close the tab anytime you like.'
    for ll in ports:
        if platform == "linux" or platform == "linux2":
            os.system('fuser -n tcp -k {}'.format(ll))
        elif platform == "darwin":
            os.system(
                'port=($(lsof -i tcp:{}|grep python2.7 |cut -f2 -d" ")); [[ -n "$port" ]] && kill -9 $port'.format(
                    ll))
            os.system(
                'port=($(lsof -i tcp:{}|grep Google |cut -f2 -d" ")); [[ -n "$port" ]] && kill -9 $port'.format(ll))
        print 'port {} killed'.format(ll)
    raise SystemExit


tab0_BUT_exit = Button(label='Exit EvtBrowser', width=150, button_type='danger')
tab0_BUT_exit.on_click(tab0_exit)

panel0 = column(row(tab0_SPCR_LFT_Div_title, tab0_Div_title),
                row(tab0_SPCR_LFT_DataTb_dspec,
                    column(tab0_DataTb_evt, tab0_Div_Tb), tab0_SPCR_RGT_DataTb_dspec,
                    widgetbox(tab0_BUT_EvtSel, tab0_BUT_DDownload, tab0_BUT_exit, tab0_Div_exit, width=150)))

lout = panel0

curdoc().add_root(lout)
curdoc().title = "Event Browser"
