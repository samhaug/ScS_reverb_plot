#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : plot_bounce_points.py
Purpose : plot bounce points from bounce_points.h5 file
Creation Date : 15-06-2017
Last Modified : Thu 15 Jun 2017 11:35:06 AM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
import h5py
import obspy
import seispy
from mpl_toolkits.basemap import Basemap
from matplotlib import rcParams
rcParams['axes.color_cycle'] = ['#1f77b4','#ff7f0e','#2ca02c',
                                '#d62728','#9467bd','#8c564b',
                                '#e377c2','#7f7f7f','#bcbd22','#17becf']

def main():
    cl = ['#1f77b4','#ff7f0e','#2ca02c',
          '#d62728','#9467bd','#8c564b',
          '#e377c2','#7f7f7f','#bcbd22','#17becf']
    dirname = '/home/samhaug/work1/ScS_reverb_data/obspyDMT/mag_7.0_8.0/20030620_061938.a/processed/'

    f = h5py.File(dirname+'bounce_points.h5','r')
    st = obspy.read(dirname+'st_T.pk')
    stat_list = []
    for tr in st:
        stat_list.append([tr.stats.sac['stlo'],tr.stats.sac['stla']])
    c = np.array(stat_list)

    full_fig,full_ax,m = setup_fig()
    stx,sty = m(c[:,0],c[:,1])
    full_ax.scatter(stx,sty,
                   marker='v',s=5,color='k',alpha=0.5)
    for idx,i in enumerate(f):
        fig,ax,m = setup_fig()
        ax.scatter(stx,sty,
                   marker='v',s=5,color='k',alpha=0.5)
        for jdx,j in enumerate(f[i]):
            lat = f[i+'/'+j][:,0]
            lon = f[i+'/'+j][:,1]
            x,y = m(lon,lat)
            ax.scatter(x,y,marker='+',alpha=0.5,s=40,c=cl[jdx])
            full_ax.scatter(x,y,marker='+',alpha=0.5,s=40,c=cl[int((idx+1)*jdx/2.)])
    plt.show()

def setup_fig():
    fig,ax = plt.subplots(figsize=(8,5))
    m = Basemap(llcrnrlon=-138,llcrnrlat=-29.5,urcrnrlon=-17,urcrnrlat=60.0,
                        resolution='c',projection='cass',lon_0=-76,lat_0=15)
    m.drawcoastlines()
    return fig,ax,m

main()
