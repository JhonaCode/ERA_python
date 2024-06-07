#!/usr/bin/python
# -*- coding: UTF-8 -*-

#################################
#PYTHON CODE TO PLOT DIFFERENS 
#MPAS DATA USING CARTOPY AND XARRAY. 
#################################
#PYTHON CODE TO PLOT DIFFERENS 
# Data:01/11/23
#################################
# By: Jhonatan A. A Manco
#################################

# Function to load the ncfiles
import xarray as xr

import  os,sys



#Path to the files 
path1='/dados/bamc/jhonatan.aguirre/DATA/ERA5/goamazon_south_america' 

# Out figure folder
out_fig='/dados/bamc/jhonatan.aguirre/git_repositories/goamazon_large_scale'

#out python nc files
out_files= path1+'/python_nc'

# TO open  a unique file
temp_f1 = path1+'/era5.temperature.goamazon_south_america_2014020100-2014033023.nc'
geo_f1 = path1+'/era5.geopotential.goamazon_south_america_2014020100-2014033023.nc'
q_f1 = path1+'/era5.specific_humidity.goamazon_south_america_2014020100-2014033023.nc'
rh_f1 = path1+'/era5.relative_humidity.goamazon_south_america_2014020100-2014033023.nc'
u_f1    = path1+'/era5.u_component_of_wind.goamazon_south_america_2014020100-2014033023.nc'
v_f1    = path1+'/era5.v_component_of_wind.goamazon_south_america_2014020100-2014033023.nc'
w_f1    = path1+'/era5.vertical_velocity.goamazon_south_america_2014020100-2014033023.nc'
cf_f1   = path1+'/era5.fraction_of_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
md_f1   = path1+'/era5.vertically_integrated_moisture_divergence.goamazon_south_america_2014020100-2014033023.nc'
tprec_f1= path1+'/era5.total_precipitation.goamazon_south_america_2014020100-2014033023.nc'
cprec_f1= path1+'/era5.convective_precipitation.goamazon_south_america_2014020100-2014033023.nc'
lcld_f1= path1+'/era5.low_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
mcld_f1= path1+'/era5.medium_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
hcld_f1= path1+'/era5.high_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
shf_f1= path1+'/era5.surface_sensible_heat_flux.goamazon_south_america_2014020100-2014033023.nc'
lhf_f1= path1+'/era5.surface_latent_heat_flux.goamazon_south_america_2014020100-2014033023.nc'
qu_f1= path1+'/era5.vertical_integral_of_eastward_water_vapour_flux.goamazon_south_america_2014020100-2014033023.nc'
qv_f1= path1+'/era5.vertical_integral_of_northward_water_vapour_flux.goamazon_south_america_2014020100-2014033023.nc'

#iop1
temp1  =  xr.open_dataset(temp_f1  )
cf1    =  xr.open_dataset(cf_f1    )
z1     =  xr.open_dataset(geo_f1   )
q1     =  xr.open_dataset(q_f1     )
rh1    =  xr.open_dataset(rh_f1    )
u1     =  xr.open_dataset(u_f1     )
v1     =  xr.open_dataset(v_f1     )
w1     =  xr.open_dataset(w_f1     )
md1    =  xr.open_dataset(md_f1    )
tprec1 =  xr.open_dataset(tprec_f1 )
cprec1 =  xr.open_dataset(cprec_f1 )
lcld1  =  xr.open_dataset(lcld_f1  )
mcld1  =  xr.open_dataset(mcld_f1  )
hcld1  =  xr.open_dataset(hcld_f1  )
shf1   =  xr.open_dataset(shf_f1   )
lhf1   =  xr.open_dataset(lhf_f1   )
qu1    =  xr.open_dataset(qu_f1    )
qv1    =  xr.open_dataset(qv_f1    )


#IOP2

file2  = '.goamazon_south_america_2014081500-2014103123.nc'

# TO open  a unique file
temp_f2 = path1+'/era5.temperature' +file2
geo_f2  = path1+'/era5.geopotential'+file2
q_f2    = path1+'/era5.specific_humidity'+file2
rh_f2   = path1+'/era5.relative_humidity'+file2
u_f2    = path1+'/era5.u_component_of_wind'+file2
v_f2    = path1+'/era5.v_component_of_wind'+file2
w_f2    = path1+'/era5.vertical_velocity'+file2
cf_f2   = path1+'/era5.fraction_of_cloud_cover'+file2
md_f2   = path1+'/era5.vertically_integrated_moisture_divergence'+file2
tprec_f2= path1+'/era5.total_precipitation'+file2
cprec_f2= path1+'/era5.convective_precipitation'+file2
lcld_f2 = path1+'/era5.low_cloud_cover'+file2
mcld_f2 = path1+'/era5.medium_cloud_cover'+file2
hcld_f2 = path1+'/era5.high_cloud_cover'+file2
shf_f2  = path1+'/era5.surface_sensible_heat_flux'+file2
lhf_f2  = path1+'/era5.surface_latent_heat_flux'+file2
qu_f2   = path1+'/era5.vertical_integral_of_eastward_water_vapour_flux'+file2
qv_f2   = path1+'/era5.vertical_integral_of_northward_water_vapour_flux'+file2

#iop2
temp2  =  xr.open_dataset(temp_f2  )
cf2    =  xr.open_dataset(cf_f2    )
z2     =  xr.open_dataset(geo_f2   )
q2     =  xr.open_dataset(q_f2     )
rh2    =  xr.open_dataset(rh_f2    )
u2     =  xr.open_dataset(u_f2     )
v2     =  xr.open_dataset(v_f2     )
w2     =  xr.open_dataset(w_f2     )
md2    =  xr.open_dataset(md_f2    )
tprec2 =  xr.open_dataset(tprec_f2 )
cprec2 =  xr.open_dataset(cprec_f2 )
lcld2  =  xr.open_dataset(lcld_f2  )
mcld2  =  xr.open_dataset(mcld_f2  )
hcld2  =  xr.open_dataset(hcld_f2  )
shf2   =  xr.open_dataset(shf_f2   )
lhf2   =  xr.open_dataset(lhf_f2   )
qu2    =  xr.open_dataset(qu_f2   )
qv2    =  xr.open_dataset(qv_f2   )


# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)



