import csv
f1 = open('2befiltered.csv','r') # open input file for reading 
users_dict = {}
with open('out.csv', 'wb') as f: # output csv file
	writer_csv = csv.writer(f)
with open('2befiltered_out.csv','r') as csvfile: # input csv file
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
    	#city,administrative_region,store_url,country,source_url,phone_no
        print row['city'].split(','),row['administrative_region'].split(','),row['store_url'].split(','),row['country'].split(',')[7], row['source_url'].split(','), row['phone_no'].split(',')
        users_dict.update(row)
        #users_list.append(row['Address'].split(','))
        #users_list.append(row['Last Login DateTime'])
        #users_list.append(row[5].split(',')[7])

print users_dict

f1.close() 