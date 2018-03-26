This directory contains data from data.cityofboston.gov and scripts for analysis.

#### Scripts in this directory:
* location_updater.py - updates missing elements in the "Location" column of the data using the geopy module. Takes licenses.csv and creates updated_resto.csv. 
* location_updater_evaluator.py - performs tests on updated_resto.csv to evaluate the success of location_updater. Currently only tests for 0,0 values in each column.
* mapping_all_restaurants.py - constructs lat and lon from a given column in a dataset and uses geoplotlib to create a map of all locations. Contains code for filtering different restaurants.

The original data is contained in licenses.csv. It contains the following variables for
more than 2000 restaurants in Boston:

* 'businessName' - The name of the business
* 'DBAName' - "doing business as." largely empty
* 'Address' - The street address
* 'CITY' - The subdivision of Boston that this restaurant is in (e.g. West Roxbury)
* 'STATE' - MA
* 'ZIP' - The zipcode of the restaurant
* 'LICSTATUS'
* 'LICENSECAT'
* 'DESCRIPT'
* 'licenseadddttm'
* 'dayphn' - Phone number
* 'Property_ID'
* 'Location' - formatted (lat, lon)

