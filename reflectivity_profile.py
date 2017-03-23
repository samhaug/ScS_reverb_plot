#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reflectivity_profile.py
Purpose : plot reflectivity profile from saved ascii made by long_migrate.py
Creation Date : 23-03-2017
Last Modified : Thu 23 Mar 2017 04:56:40 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
from scipy.ndimage.filters import gaussian_filter

def main():
    fig,ax = plt.subplots(figsize=(3,4.5))
    reflect = read_refelct('HL_NA.dat')
    ax.plot(gaussian_filter(reflect[:,0],1),reflect[:,1],color='k',lw=1.0)

    ax.set_ylim(reflect[:,1].max(),reflect[:,1].min())
    ax.set_xlim(reflect[:,0].min()-np.std(reflect[:,0]),reflect[:,0].max()+np.std(reflect[:,0]))
    ax.axhline(670,color='k',alpha=0.5,lw=0.5)
    ax.axhline(400,color='k',alpha=0.5,lw=0.5)
    ax.axhline(220,color='k',alpha=0.5,lw=0.5)
    ax.text(reflect[:,0].min(),200,"\'220\'",size=7)
    ax.text(reflect[:,0].min(),390,"\'400\'",size=7)
    ax.text(reflect[:,0].min(),650,"\'670\'",size=7)

    ax.tick_params(axis='both', which='major', labelsize=7)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    #ax.set_xlabel('R',size=7)

    plt.savefig('reflectivity_profile.pdf')
    call('evince reflectivity_profile.pdf',shell=True)

def read_refelct(fname):
    reflect = np.loadtxt('/home/samhaug/work1/ScS_reverb_sims/reflectivity_profiles/'+fname)
    return reflect

main()
