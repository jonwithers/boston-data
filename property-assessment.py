import pandas as pd
import numpy as np
import os
import urllib.request

file = "assessment_data.csv"
url = "https://data.boston.gov/dataset/e02c44d2-3c64-459c-8fe2-e1ce5f38a035/resource/fd351943-c2c6-4630-992d-3f895360febd/download/ast2018full.csv"
if (os.path.isfile(file) == False):
    urllib.request.urlretrieve(url, file)

df = pd.read_csv(file, nrows = 100)

tax_col = df['GROSS_TAX'] / 1000
print(tax_col.describe())
