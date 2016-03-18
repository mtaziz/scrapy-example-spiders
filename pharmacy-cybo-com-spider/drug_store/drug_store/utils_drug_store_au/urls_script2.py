import csv

f1 = open ("urls-cleaned.csv","r") # open input file for reading 
users_dict = {}
with open('after_clean.csv', 'wb') as f: # output csv file
	writer = csv.writer(f)
with open('urls-cleaned.csv','r') as csvfile: # input csv file
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print row['store_url'].split(',')
        # row['Last Login DateTime'],row['Address'].split(',')[7]
        users_dict.update(row)
out = csv.writer(f)
        #users_list.append(row['Address'].split(','))
        #users_list.append(row['Last Login DateTime'])
        #users_list.append(row[5].split(',')[7])

print users_dict

f1.close() 