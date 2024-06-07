#!/usr/bin/python
# -*- coding: UTF-8 -*-


#################################
#PYTHON CODE TO PLOT DIFFERENS 
#MAPS PROJECTION USING THE 
#LIBRARY BASEMAP. 
#################################
#PYTHON CODE TO PLOT DIFFERENS 
# Data:13/04/22
#################################
# By: Jhonatan A. A Manco
#################################

import matplotlib.pyplot as plt
####################################################

import  Parameters_era5  as de

import source.functions as fnc

# Function with the definition of differents projetions
import   source.cartopyplot   as ma 

# Function to load the ncfiles
import xarray as xr

days  =   [
            '02-27', '03-06', '03-09',
            '03-10', '03-15', '03-16',
            '03-17', '03-18'
           ]

T1    =fnc.shallow_xarray(de.temp1  ,days)
cf1   =fnc.shallow_xarray(de.cf1    ,days)
u1    =fnc.shallow_xarray(de.u1     ,days)
v1    =fnc.shallow_xarray(de.v1     ,days)
w1    =fnc.shallow_xarray(de.w1     ,days)
q1    =fnc.shallow_xarray(de.q1     ,days)
rh1   =fnc.shallow_xarray(de.rh1    ,days)
md1   =fnc.shallow_xarray(de.md1    ,days)
tprec1=fnc.shallow_xarray(de.tprec1 ,days)
cprec1=fnc.shallow_xarray(de.cprec1 ,days)
lcld1 =fnc.shallow_xarray(de.lcld1  ,days)
mcld1 =fnc.shallow_xarray(de.mcld1  ,days)
hcld1 =fnc.shallow_xarray(de.hcld1  ,days)
shf1  =fnc.shallow_xarray(de.shf1   ,days)
lhf1  =fnc.shallow_xarray(de.lhf1   ,days)
qu1   =fnc.shallow_xarray(de.qu1    ,days)
qv1   =fnc.shallow_xarray(de.qv1    ,days)

iop1 = xr.merge([
                    T1,cf1,u1,v1,w1,
                    q1,rh1,md1,tprec1,cprec1,
                    lcld1,mcld1,hcld1,shf1,lhf1,
                    qu1,qv1
                    ])
name='shallow_iop1'
print('creating %s.nc ........... '%(name))
iop1.to_netcdf('%s/%s.nc'%(de.out_files,name))


days  =   [ 
          '09-02','09-03','09-04','09-09','11-09', 
          '09-14','09-15','09-16','09-19','09-20', 
          '09-21','09-22','09-23','09-26','09-27', 
          '09-29','10-01','10-03','10-05','10-07', 
           ]

T2    =fnc.shallow_xarray(de.temp2  ,days)
cf2   =fnc.shallow_xarray(de.cf2    ,days)
u2    =fnc.shallow_xarray(de.u2     ,days)
v2    =fnc.shallow_xarray(de.v2     ,days)
w2    =fnc.shallow_xarray(de.w2     ,days)
q2    =fnc.shallow_xarray(de.q2     ,days)
rh2   =fnc.shallow_xarray(de.rh2    ,days)
md2   =fnc.shallow_xarray(de.md2    ,days)
tprec2=fnc.shallow_xarray(de.tprec2 ,days)
cprec2=fnc.shallow_xarray(de.cprec2 ,days)
lcld2 =fnc.shallow_xarray(de.lcld2  ,days)
mcld2 =fnc.shallow_xarray(de.mcld2  ,days)
hcld2 =fnc.shallow_xarray(de.hcld2  ,days)
shf2  =fnc.shallow_xarray(de.shf2   ,days)
lhf2  =fnc.shallow_xarray(de.lhf2   ,days)
qu2   =fnc.shallow_xarray(de.qu2    ,days)
qv2   =fnc.shallow_xarray(de.qv2    ,days)

iop2 = xr.merge([
                    T2,cf2,u2,v2,w2,
                    q2,rh2,md2,tprec2,cprec2,
                    lcld2,mcld2,hcld2,shf2,lhf2,
                    qu2,qv2
                    ])
name='shallow_iop2'
print('creating %s.nc ........... '%(name))
iop2.to_netcdf('%s/%s.nc'%(de.out_files,name))
plt.show()
