"""
This was an attempt to use the geopy module to update as many of the locations as I could.
However, the module seems to have returned a lot of garbage.
Looking through the output data, most of the corrected values are way off.
"""

import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim()

# def null_calculations(col, s):
#     print("{} is {}% missing values.".format(s, np.around(np.mean(pd.isnull(col)) * 100, 2)))

"""
 Reading in the data and reducing the number of unknown locations
"""

df_raw = pd.read_csv("licenses.csv")
df_raw['FullAddress'] = df_raw['Address'] + ", Boston MA"
updated_location_column = []
for index, line in df_raw.iterrows():
    if df_raw['Location'][index] == "(0.000000000, 0.000000000)":
        loc = geolocator.geocode(df_raw['FullAddress'][index])
        if loc == None:
            updated_location_column.append("(0.000000000, 0.000000000)")
            continue
        lat0 = loc.latitude
        lon0 = loc.longitude
        updated_location_column.append((lat0, lon0))
    else:
        updated_location_column.append(df_raw['Location'][index])
df_updated = df_raw
df_updated['UpdatedLocation'] = updated_location_column

df_updated.to_csv("updated_resto.csv")
