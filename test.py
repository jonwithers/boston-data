"""
This is the testing script.
"""

test1 = [1,2,3,4]
def fun1(st):
    for itme in test1:
        print(str(itme) + st)

fun1('hi')
# s = "(0.000000000, 0.000000000)"
# lat_start = s.find('(')+1
# lat_end = s.find(',')
# lon_start = s.find(',')+2
# lon_end = s.find(')')
# print("lat = {}, lon = {}.".format(s[lat_start:lat_end], s[lon_start:lon_end]))

# import pandas as pd
# import numpy as np
# import geoplotlib
# from geopy.geocoders import Nominatim
# geolocator = Nominatim()
#
# df_raw = pd.read_csv("licenses.csv", nrows = 100)
# df_raw['FullAddress'] = df_raw['Address'] + ", " + 'Boston' + " " + df_raw['STATE']
# # updated_location_column = []
# # for index, line in df_raw.iterrows():
# #     if df_raw['Location'][index] == "(0.000000000, 0.000000000)":
# #         loc = geolocator.geocode(df_raw['FullAddress'][index])
# #         lat0 = loc.latitude
# #         lon0 = loc.longitude
# #         updated_location_column.append((lat0, lon0))
# #     else:
# #         updated_location_column.append(df_raw['Location'][index])
# # print(updated_location_column[:30])
#
# address = df_raw["FullAddress"][0]
# output = geolocator.geocode(address)
# print(address, output)
