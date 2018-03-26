"""
This is a script to evaluate the success of the location updater.
To implement: some way of checking how much junk the updater produced.
"""
import pandas as pd
import numpy as np



df = pd.read_csv("updated_resto.csv")

missing_location_filter = df['Location'] == "(0.000000000, 0.000000000)"
missing_location_filter_2 = df['UpdatedLocation'] == "(0.000000000, 0.000000000)"

missing_original_locations = df[missing_location_filter]
missing_new_locations = df[missing_location_filter_2]
n_missing_original = missing_original_locations.shape[0]
n_missing_new = missing_new_locations.shape[0]
print("There are {} missing locations in the original. The updated data has {} missing locations.".format(n_missing_original, n_missing_new))
