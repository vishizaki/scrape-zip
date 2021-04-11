# Importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()
import os
import time
import csv

# Setting variables
zipList = [33426,94521,29492,33472,30071,11545,45241,73055,20747,16503,10710,84096,73505,29506,93551,29501,15317,47720,48625,\
            60612,90701,43623,93063,56082,56082,55119,34232,28152,97504,77520,85353,11366,55101,43623,29556,78211,77346,64079,\
            15223,43302,43314,48183,34293,37412,92801,78209,80601,57656,89801,18504,11214,97838,11358,31326,60565,14617,48367,\
            45030,72916,12189,21218,59718,55401,56342,71106,74948,46202,45426,77498,93063,93063]
zipCityStateHash = {}
zipCityStateList = []
url = "https://tools.usps.com/zip-code-lookup.htm?citybyzipcode"

options = Options()
options.headless = True
driver = webdriver.Chrome(os.getenv("MY_PATH"), options=options)

# Defining functions:
def getCityState(zip):
  driver.get(url)
  inputElement = driver.find_element_by_id("tZip")
  inputElement.send_keys(zip)
  searchButton = driver.find_element_by_id("cities-by-zip-code")
  searchButton.click()

  time.sleep(3)
  results = driver.find_element_by_class_name('row-detail-wrapper').text
  # Append to list
  zipCityStateList.append([zip, results, results[-2:]])

def saveZipHash(list):
  for zip in list:
    getCityState(zip)

def writeCsv(zip_writer, list):
  for zipState in list:
    zip_writer.writerow(zipState)

print("Browsing zipcodes")

# Running functions
saveZipHash(zipList)

print("Saving information to csv")

# Saving to CSV 
with open('zip_state_list.csv', mode='w') as zip_file:
  zip_writer = csv.writer(zip_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  writeCsv(zip_writer, zipCityStateList)

print("Process complete!")
