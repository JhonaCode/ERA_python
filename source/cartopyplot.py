###########################################
# PYTHON FILE TO 
# DEFINED MULTIPLES PLOT PROJECTION
#USING THE BASEMAP LIBRARY
###########################################

import numpy  as np 

import matplotlib as mpl

import matplotlib.pyplot as plt

import source.plotparameters as pn

import cartopy.crs as ccrs

import cartopy.feature as cfeature

from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

import datetime as dt
import pandas   as pd


#from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#used the user parameter to plot(plotparameter.py)


plotdef='mapa1'
#Latex width 
wf=1.0
hf=1.0
cmmais=0.0
#plot size of the figures
#cmmais are the cm to put the cbbar  without modified the size of the fig
projection=ccrs.PlateCarree(central_longitude=180.0, globe=None)
#############plot formated
# make the map global rather than have it zoom in to
# the extents of any plotted data
###################################3


def cartopy_plot(data,varname,date_str=[],lats=[],lons=[],lev=[],bcolor=[],lat=[],lon=[],plotname='',figname='',color='RdBu_r',out='',cbar=True):

    var=ajust_var(data,varname,date_str,lev)

    pn.plotsize(plotdef,wf,hf,cmmais)

    fig = plt.figure()
    ax  = fig.add_subplot(1, 1, 1, projection=projection)
    #ax  = plt.axes(projection=projection)

    ax=def_axis_1(ax)

    #Axis definitions
    ax,levels,latitude,longitude=axis_def(ax,var,bcolor,lats,lat,lons,lon)

    filled=ax.contourf(longitude, latitude, var[0,0,:,:], levels=levels,
                transform=ccrs.PlateCarree(),
                cmap=color,alpha=1.0,extend='both')

    lines  = ax.contour(longitude, latitude, var[0,0,:,:], levels=filled.levels,
                        colors=['black'] ,alpha=0.8,linewidths=0.5,
                        transform=ccrs.PlateCarree())


    if cbar: 
        CB=fig.colorbar(filled, orientation='vertical',shrink=0.5)
        CB.set_ticks(levels)

        # Add a colorbar for the filled contour.
        #fig.colorbar(filled, orientation='horizontal',shrink=0.5)

    ax.set_title("%s"%(plotname),fontsize=8)

    fig.savefig('%s%s.pdf'%(out,figname),bbox_inches='tight', format='pdf', dpi=200)

               
    return fig     

def cartopy_qflux(u,v,data=[0],date_str=[],lev=[],scale=1, width=0.4,lats=[],lons=[],bcolor=[],lat=[],lon=[],plotname='',figname='',color='RdBu_r',out='',cbar=True):

    u=u[0,:,:]
    v=v[0,:,:]
    #u=ajust_var(u,'p71.162',date_str,lev)
    #v=ajust_var(v,'p72.162',date_str,lev)

    pn.plotsize(plotdef,wf,hf,cmmais)

    fig = plt.figure()
    ax  = plt.axes(projection=projection)

    ax  = def_axis_states(ax)

    ax,levels,latitude,longitude=axis_def(ax,u,bcolor,lats,lat,lons,lon)

    if(len(data)==1):

        data = np.sqrt(u**2 + v**2)


    filled=ax.contourf(longitude, latitude, data[:,:], levels=levels,
                transform=ccrs.PlateCarree(),
                #cmap='coolwarm',alpha=1.0)
                #cmap='Spectral_r',alpha=1.0)
                #cmap='RdYlBu_r',alpha=1.0)
                cmap=color,alpha=1.0,extend='both')
    #
    #qv = ax.quiver(lons, lats ,datau.values, datav.values, transform=ccrs.PlateCarree(),color='black',scale=800, width=0.002)

    #qv = ax.quiver(lons, lats ,datau.values, datav.values, transform=ccrs.PlateCarree(),color='black',scale=250, width=0.0035)#,headlength=0.05)

    npp=10

    qv = ax.quiver(longitude[::npp], latitude[::npp] ,u[::npp,::npp].values, v[::npp,::npp].values, transform=ccrs.PlateCarree(),color='black',scale=scale, width=width)#,headlength=0.05)

    #ax.quiverkey(qv, X=1.00, Y=1.10, U=100,label=r'100[kgkg$^{-1}$ms$^{-1}$Pa]', labelpos='E',fontproperties={'size':5})
    ax.quiverkey(qv, X=1.05, Y=1.02, U=10,label=r'10', labelpos='E',fontproperties={'size':5}, labelsep=0.01)
    
    #qv = ax.quiver(lons, lats ,datau.values, datav.values, transform=ccrs.PlateCarree(),color='black',scale=1, width=0.0015)#,headlength=0.05)

    if cbar:
    # Add a colorbar for the filled contour.
        CB=fig.colorbar(filled, orientation='vertical',shrink=0.5)
        CB.set_ticks(levels)

    ax.set_title("%s"%(plotname),fontsize=6)

    fig.savefig('%s%s.pdf'%(out,figname),bbox_inches='tight', format='pdf', dpi=200)
               
    return fig,qv     

def cartopy_vector(u,v,data=[0],date_str=[],lev=[],scale=1, width=0.4,lats=[],lons=[],bcolor=[],lat=[],lon=[],plotname='',figname='',color='RdBu_r',out='',cbar=True):

    u=ajust_var(u,'u',date_str,lev)
    v=ajust_var(v,'v',date_str,lev)

    pn.plotsize(plotdef,wf,hf,cmmais)

    fig = plt.figure()
    ax  = plt.axes(projection=projection)

    ax  = def_axis_states(ax)

    ax,levels,latitude,longitude=axis_def(ax,u,bcolor,lats,lat,lons,lon)

    if(len(data)==1):

        data = np.sqrt(u**2 + v**2)

    filled=ax.contourf(longitude, latitude, data[0,0,:,:], levels=levels,
                transform=ccrs.PlateCarree(),
                #cmap='coolwarm',alpha=1.0)
                #cmap='Spectral_r',alpha=1.0)
                #cmap='RdYlBu_r',alpha=1.0)
                cmap=color,alpha=1.0,extend='both')
    #
    #qv = ax.quiver(lons, lats ,datau.values, datav.values, transform=ccrs.PlateCarree(),color='black',scale=800, width=0.002)

    #qv = ax.quiver(lons, lats ,datau.values, datav.values, transform=ccrs.PlateCarree(),color='black',scale=250, width=0.0035)#,headlength=0.05)

    npp=10

    qv = ax.quiver(longitude[::npp], latitude[::npp] ,u[0,0,::npp,::npp].values, v[0,0,::npp,::npp].values, transform=ccrs.PlateCarree(),color='black',scale=scale, width=width)#,headlength=0.05)

    #ax.quiverkey(qv, X=1.00, Y=1.10, U=100,label=r'100[kgkg$^{-1}$ms$^{-1}$Pa]', labelpos='E',fontproperties={'size':5})
    ax.quiverkey(qv, X=1.05, Y=1.02, U=10,label=r'10', labelpos='E',fontproperties={'size':5}, labelsep=0.01)
    
    #qv = ax.quiver(lons, lats ,datau.values, datav.values, transform=ccrs.PlateCarree(),color='black',scale=1, width=0.0015)#,headlength=0.05)

    if cbar:
    # Add a colorbar for the filled contour.
        CB=fig.colorbar(filled, orientation='vertical',shrink=0.5)
        CB.set_ticks(levels)

    ax.set_title("%s"%(plotname),fontsize=6)

    fig.savefig('%s%s.pdf'%(out,figname),bbox_inches='tight', format='pdf', dpi=200)
               
    return fig,qv     

def barra(color='RdBu_r',b1=100,b2=100,nn=10,plotname='',figname='',out='',label=''):

    if b1==b2 and b1==100:

        b1=np.min(data[:].values)
        b2=np.max(data[:].values)

    levels= np.linspace(b1,b2,nn,endpoint=True)

    fig,ax = plt.subplots(figsize=(4,0.5))
    fig.subplots_adjust(bottom=0.5)

    cmap = color
    norm = mpl.colors.Normalize(vmin=b1, vmax=b2)
    CB=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),cax=ax, orientation='horizontal',shrink=1.0,extend='both',label=label)
    cbarlabels = np.linspace(b1,b2,11,endpoint=True)

    #CB.set_ticks(cbarlabels[::3])
    #CB.ax.set_title(r'%s'%clabel,fontsize=6)

    #ax.quiverkey(q, X=0.25, Y=0.45, U=500,label=r'[kgkg$^{-1}$ms$^{-1}$Pa]', labelpos='E')


    fig.savefig('%s%s.pdf'%(out,figname),bbox_inches='tight', format='pdf', dpi=100)

def narrow_q(q,plotname='',figname='',out='',label=''):


    fig,ax = plt.subplots(figsize=(8,0.5))
    #fig.subplots_adjust(bottom=0.5)

    ax.quiverkey(q, X=0.25, Y=0.45, U=500,label=r'[kgkg$^{-1}$ms$^{-1}$Pa]', labelpos='E')


    fig.savefig('%s%s.pdf'%(out,figname),bbox_inches='tight', format='pdf', dpi=100)
               
    return fig     

def ajust_var(data,varname,date_str=[],lev=[]):

    #var=getattr(data,varname)
    var=data[varname]

    if lev: 
        var= var.sel(level=var.level.isin([lev]))
    else: 
        var=var 

    if date_str: 

        #2014-02-01T00:00:00.00000000
        date_format = '%Y-%m-%dT%H:%M'##+':00.00000000'

        date_obj=dt.datetime.strptime(date_str, date_format)

        var= var.sel(time=[date_obj])

    else:

        var= var.isel( time=[0])

    return var

def def_axis_1(ax):

    #ax.set_global()
    #ax.stock_img()
    ax.coastlines()
    ax.gridlines(draw_labels=False)

    #MOMO STATES
    #ax.add_feature(cfeature.STATES.with_scale('50m'))



    return ax

def def_axis_states(ax):

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    #ax.set_global()
    #ax.stock_img()
    
    ax.coastlines( linestyle='-', alpha=1.00,linewidth=1)

    #grid
    ax.gridlines(draw_labels=False)


    #ax.add_feature(cfeature.LAND)

    #Contries
    ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=1.00,facecolor='none',linewidth=0.5)

    ax.add_feature(cfeature.LAKES, edgecolor='navy',alpha=1.00,facecolor='none',linewidth=0.5)

    ax.add_feature(cfeature.RIVERS, edgecolor='navy',alpha=1.00,facecolor='none',linewidth=0.5)


    #MOMO STATES
    #ax.add_feature(cfeature.STATES.with_scale('50m'))

    states = cfeature.NaturalEarthFeature(category='cultural', scale='50m', facecolor='none', name='admin_1_states_provinces_lines')

    ax.add_feature(states, edgecolor='black',alpha=1.0,linewidth=0.5)

    #resol = '50m'
    #bodr = cfeature.NaturalEarthFeature(category='cultural', 
    #name='admin_0_boundary_lines_land', scale=resol, facecolor='none', alpha=0.7)
    #ax.add_feature(bodr, linestyle='--', edgecolor='k', alpha=1)
    #plt.show()
    #exit()

    return ax

def axis_def(ax,var,bcolor,lats,lat,lons,lon):

    if lats:
        latitude =lats
    else:
        latitude =var.latitude

    if lons:
        longitude=lons
    else:
        longitude=var.longitude


    if bcolor:
        b1=bcolor[0]
        b2=bcolor[1]
        bn=bcolor[2]
    else: 
        b1=np.min(var[:])
        b2=np.max(var[:])
        bn=5

    levels= np.linspace(b1,b2,bn,endpoint=True)

    if(lat):
        maxlat= lat[0]
        minlat= lat[1]
        nlat  = lat[2] 
        levels_lat= np.linspace(minlat,maxlat,nlat,endpoint=True)
        
    else:

        maxlat= np.max(var.latitude)
        minlat= np.min(var.latitude)
        levels_lat= np.linspace(minlat,maxlat,5,endpoint=True)

    if(lon):

        maxlon= lon[0]
        minlon= lon[1]
        nlon  = lon[2] 

        levels_lon= np.linspace(minlon,maxlon,nlon,endpoint=True)

    else:
        maxlon= max(var.longitude)
        minlon= min(var.longitude)
        levels_lon= np.linspace(minlon,maxlon,5,endpoint=True)

    #ax.set_xlim([minlon, maxlon])
    #ax.set_ylim([minlat ,maxlat])
    ax.set_extent([minlon, maxlon, minlat,maxlat],crs=ccrs.PlateCarree())

    ax.set_xticks(levels_lon, crs=ccrs.PlateCarree())
    ax.set_yticks(levels_lat, crs=ccrs.PlateCarree())

    lon_formatter = LongitudeFormatter(number_format='.1f',
                                       degree_symbol='',
                                       dateline_direction_label=True)
    lat_formatter = LatitudeFormatter(number_format='.1f',
                                      degree_symbol='')

    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

    #ax.xlabel_style = {'size': 6, 'color': 'red'}
    #xlabel_style = {'color': 'red', 'weight': 'bold'}
    #ax.tick_params(axis='both', labelsize=8)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)


    # Use the line contours to place contour labels.
    #ax.clabel(
    #    lines,  # Typically best results when labelling line contours.
    #    colors=['black'],
    #    manual=False,  # Automatic placement vs manual placement.
    #    inline=True,  # Cut the line where the label will be placed.
    #    fmt=' {:.0f} '.format,  # Labes as integers, with some extra space.
    #)

    return ax,levels,latitude,longitude
