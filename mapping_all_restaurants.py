"""
This script uses geoplotlib to produce a map of restaurant locations. Because the updated locations turned out
a lot of nonsense, this script uses the original Location column to produce lat and lon for geoplotlib.
"""

import pandas as pd
import numpy as np
import geoplotlib
from geopy.geocoders import Nominatim
geolocator = Nominatim()

df = pd.read_csv('updated_resto.csv')

location_filter = df['Location'] != "(0.000000000, 0.000000000)"
df = df[location_filter]
## making two new columns: lat and lon
lat = []
lon = []
for element in df.Location:
    lat_start = element.find('(') + 1
    lat_end = element.find(',')
    lon_start = element.find(",") + 2
    lon_end = element.find(')')
    lat.append(float(element[lat_start:lat_end]))
    lon.append(float(element[lon_start:lon_end]))
df['lat'] = lat
df['lon'] = lon

# df.to_csv("updated_resto2.csv")
# print(df.lat.describe())

# burger_king_filter = df['businessName'] == 'Burger King'
# mcdonalds_filter = df['businessName'] == "McDonald's"
# taco_bell_filter = df['businessName'] == "Taco Bell # 29265"
# no_fastfood_filter = (df['businessName'] != 'Burger King') & (df['businessName'] != "McDonald's") & (df['businessName'] != "Taco Bell # 29265")
# burger_king_df = df[burger_king_filter]
# mcdonalds_df = df[mcdonalds_filter]
# taco_bell_df = df[taco_bell_filter]
# df_loc = df[no_fastfood_filter]
#
geoplotlib.tiles_provider('toner-lite')
geoplotlib.dot(df[['lat', 'lon']], color = [15, 173, 68, 128])
# geoplotlib.dot(burger_king_df[["lat", "lon"]], color = [252, 131, 131, 255])
# geoplotlib.dot(mcdonalds_df[["lat","lon"]], color = [0,0,255,255])
# geoplotlib.dot(taco_bell_df[["lat","lon"]], color = [255,0,255,255])
geoplotlib.show()
#
# # df_grouped = df_raw.groupby(['ZIP']).count()
# # print(df_zip_02128[['businessName', 'DESCRIPT']])
#
# # df_burger_filter = df_raw['businessName'].str.contains("Burger King")
# # df_burger = df_raw[df_burger_filter]
# # df_McD_filter = df_raw['businessName'].str.contains("McDonald's")
# # df_McD = df_raw[df_McD_filter]
