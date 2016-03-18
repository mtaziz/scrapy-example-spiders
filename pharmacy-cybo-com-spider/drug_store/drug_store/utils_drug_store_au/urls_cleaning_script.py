#!/usr/bin/env python 
import os
import sys 
# from utils_drug_store_au  import urls
import csv 

import csv


with open('urls-cleaned.csv','w') as csvfile:
    csvReaderData = csv.reader(csvfile)
    header = csvReaderData.next()
    linkIndex = header.index("store_url")
empty_list = []
for row in csvReaderData:
	store_url = row[linkIndex]
	empty_list.append([store_url])
print empty_list

with open('input.csv', 'rb') as infile, open('output.csv', 'wb') as outfile:
  incsv = csv.reader(infile, delimiter=',', quotechar='"')
  outcsv = csv.writer(outfile, delimiter=',', quotechar='"')
  incsv.read() # skip first line
  for line in incsv:
    if line[3] != '':
      outcsv.write(ProcessLine(line))

    # list_data = list(data)
    # print list_data 

    # This script reads a GPS track in CSV format and
#  prints a list of coordinate pairs
# import csv
 
# # Set up input and output variables for the script
# gpsTrack = open("C:\\data\\Geog485\\gps_track.txt", "r")
 
# # Set up CSV reader and process the header
# csvReader = csv.reader(gpsTrack)
# header = csvReader.next()
# latIndex = header.index("lat")
# lonIndex = header.index("long")
 
# # Make an empty list
# coordList = []
 
# # Loop through the lines in the file and get each coordinate
# for row in csvReader:
#     lat = row[latIndex]
#     lon = row[lonIndex]
#     coordList.append([lat,lon])
 
# # Print the coordinate list
# print coordList
    # row_count = sum(1 for row in data)
    # print row_count
    # r = 1
    # for row in data:
    #     print r
#  >>> import csv
#    >>> csvFile = open('example.tsv', 'w', newline='')
# ➊ >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
#    >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
#    24
#    >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
#    17
#    >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
#    32
#    >>> csvFile.close()
# data = ['a,x', 'b,y', 'c,z']
# f = open('urls_cleaning_script.csv', 'wb')
# w = csv.writer(f, delimiter = ',')
# w.writerows([x.split(',') for x in data])
# f.close()

# URLS = ../drug_store/urls.clean.csv

# def def parse parse(raw_file, delimiter):
#  """Parses a raw CSV file to a JSON-like object"""
#  # Open CSV file
# 	opened_file = open(raw_file)
#  # Read the CSV data
#  	csv_data = csv.reader(opened_file, delimiter=delimiter)
#  # Setup an empty list
#  	parsed_data = []
#  # Skip over the first line of the file for the headers
#  	fields = csv_data.next()
#  # Iterate over each row of the csv file, zip together field -> value
#  	for for row inin csv_data:
#  		parsed_data.append(dict(zip(fields, row)))
#  # Close the CSV file
#  	opened_file.close()
#  	return parsed_data

# def main()

# new_data = parse(URLS, ',')
# # with open('/utils_drug_store_au/urls.txt','rw')
# # read_lines = file_data.readlines()
# # print readlines

# # def function(file_data):
#     lines = []
#     for line in f:
#         lines.append(line)
#     return lines 
# def filter(txt, oldfile, newfile):
#     '''\
#     Read a list of names from a file line by line into an output file.
#     If a line begins with a particular name, insert a string of text
#     after the name before appending the line to the output file.
#     '''
#     with open(newfile, 'w') as outfile, open(oldfile, 'r', encoding='utf-8') as infile:
#         for line in infile:
#             if line.startswith(txt):
#                 line = line[0:len(txt)] + ' - Truly a great person!\n'
#             outfile.write(line)

# # input the name you want to check against
# text = input('Please enter the name of a great person: ')    
# letsgo = filter(text,'Spanish', 'Spanish2')
