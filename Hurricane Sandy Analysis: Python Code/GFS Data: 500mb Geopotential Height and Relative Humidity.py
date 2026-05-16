"""
Created on Wed Apr 22 15:09:48 2026

@author: Matthew Lentz
"""

# 500mb Geopotential Height and Relative Humidity
import pygrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Update the string below with the path to your GRIB data file.
grbs = pygrib.open('gfs_4_20121029_0600_027.grb2')

""" Uncomment the loop below to find the specific meteorological variable of your choice."""
#for msg in grbs:
#     print(msg)

hgtMSG = grbs[103]

# Divide the 500mb Geopotential height by 10 since the meteorological charts display heights in decameters (dm) rather than meters.
hgt = hgtMSG.values/10.0 
[lats, lons] = hgtMSG.latlons()

# Subtract by 273 (or 273.15) since we want to use Celsius and not Kelvin
tempMSG= grbs[104]
temp = tempMSG.values - 273 

rhMSG = grbs[105]
rh = rhMSG.values

# Define the coordinates for the specific region of interest
domain = (lons >= 270) & (lons <= 305) & (lats >= 20) & (lats <= 55)

# Find the row and column edges of this region
rows = np.where(np.any(domain, axis=1))[0]
cols = np.where(np.any(domain, axis=0))[0]

row1 = rows.min()
row2 = rows.max() + 1
col1 = cols.min()
col2 = cols.max() + 1

# Crop all the data arrays down to that smaller enclosure
lats = lats[row1:row2, col1:col2]
lons = lons[row1:row2, col1:col2]
hgt = hgt[row1:row2, col1:col2]
temp = temp[row1:row2, col1:col2]
rh = rh[row1:row2, col1:col2]

# Convert longitude from a 0-360 scale to a standard -180 to 180 scale
lons = lons - 360


fig = plt.figure(figsize=(8, 8))

proj = ccrs.LambertConformal(central_longitude=-90.0, central_latitude=35.0)
ax = plt.axes(projection=proj)
ax.set_extent([-90, -65, 30, 50], crs=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND, facecolor='wheat')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.LAKES, facecolor='lightblue')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')

# Gridlines 
glx = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=['bottom'], x_inline=False,y_inline=False,rotate_labels=True,color='white', linestyle='--', xlocs=np.arange(-90, -65, 5),ylocs=[]) 
gly = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=['right'], x_inline=False,y_inline=False,color='white', linestyle='--', xlocs=[],ylocs=np.arange(30, 50, 4)) 
glx.xpadding=10
glx.xlabel_style={'rotation':385}
 
rhFILL = ax.contourf(lons, lats, rh, levels=[70, 80, 90, 100], cmap='Greens', transform=ccrs.PlateCarree())

hgtLEVELS = np.arange(520, 585, 5)

hgtCONTOURS = ax.contour(lons, lats, hgt, levels=hgtLEVELS, colors='black', linewidths=2, transform=ccrs.PlateCarree())

ax.clabel(hgtCONTOURS, levels=hgtLEVELS, inline=True, fontsize=10, fmt='%d')

""" Uncomment the series of code below if you want to use temperature readings as well."""
#tempMIN = np.min(temp)
#tempMAX = np.max(temp)
#tempLEVELS = np.arange(tempMIN, tempMAX, 3)
#tempCONTOURS = ax.contour(lons, lats, temp, levels=tempLEVELS, cmap='cool_r', linestyles='dotted', transform=ccrs.PlateCarree())
#cbar = plt.colorbar(tempCONTOURS, orientation='horizontal')
cbar = plt.colorbar(rhFILL, orientation='horizontal')
cbar.set_label('Relative Humidity (%)')
cbar.ax.xaxis.set_label_position('top')

# Extract the analysis (run) time and valid forecast time directly from the PyGrib message
run_time = sfcMSLPMSG.analDate.strftime('%Y-%m-%d %H:%M UTC')
valid_time = sfcMSLPMSG.validDate.strftime('%Y-%m-%d %H:%M UTC')

# The main bold header
plt.suptitle('500mb Heights (dm) / Humidity (%)', fontweight='bold', fontsize=13, color='black', y=0.95)

# The normal weight subtitle
plt.title(f'GFS Model Run: {run_time} | Valid: {valid_time}', fontsize=11, color='black')

plt.show()
