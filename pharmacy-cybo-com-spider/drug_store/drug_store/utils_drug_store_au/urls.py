import sys, os
import itertools 
# Read in the file
filedata = None
with open('urls.txt', 'r') as file_open_for_read:
	filedata = file_open_for_read.read()

# for line in itertools.islice(filedata, '//', ','): # 3 and 5 are the start and stop points
# 	return line 


# Replace the target string
filedata_after_replaced = filedata.replace('//', 'https://')
#filedata_after_replaced_split = filedata_after_replaced.split(',')
# filedata_after_replaced_read_again = filedata_after_replaced.read()
#filedata_after_replaced_read_again_stripped = [s.strip() for s in filedata_after_replaced.splitlines()]
# Write the file out again
with open('urls_after_clean_newline.txt', 'w') as file_open_for_write:
	file_open_for_write.write(str(filedata_after_replaced))

file_open_for_read.close()
file_open_for_write.close()
