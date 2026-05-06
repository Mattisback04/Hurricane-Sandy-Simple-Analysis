# GR4553 Group 3 Final Project: Hurricane Sandy Analysis
*Project Overview*: This project examines the devastating nature and unique characteristics of Hurricane Sandy. This repository includes radar imagery, soundings and meteograms, mean sea level pressure (MSLP) and wind maps, as well as 500mb geopotential height and relative humidity charts to illustrate the meteorological evolution leading up to and during the event.

*Radar Plots and Code* Radar data was sourced from Amazon Web Services' open NEXRAD Level II archive. The Python scripts in this directory generate radar base reflectivity plots illustrating the structure and intensity of Hurricane Sandy. To use a different radar file, you can replace the filename in the script. For example: f = Level2File('KxxxYYYYMMDD_HHMMSS_V06').

*Soundings and Meteogram Code*: The soundings for this project were generated using the sounderpy Python library. This requires no external downloadable content; users simply need to specify the time of the event within the script to automatically retrieve and plot the upper-air data.

*Buoy Data*: To analyze surface-level changes, buoy data was retrieved from the National Data Buoy Center (NDBC). Specifically, we used data from Station ACYN4 to highlight the significant pressure drop and subsequent rise before and after Sandy's passing.

*500mb Geopotential Height & RH and MSLP & Wind*s: The maps displaying 500mb geopotential height with relative humidity, as well as MSLP with surface winds, were created using GFS analysis data. This data was sourced from the NCEI NOAA archive. To replicate or adjust this data, you can navigate to the link and select the specific time of interest (e.g., October 29th for the peak time of Hurricane Sandy).
