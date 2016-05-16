
##################################

#Prblem statement

##################################

#Given a dataset of transactions (100k rows) from a large retailer, 
#find groups of items that are frequently purchased together. 
#Each row is a single transaction with a '1' denoting that item was in the transaction. 
#Submit your findings along with any code/description of tools used to solve the problem.

import pandas as pd
import csv

#read the given dataset

data = pd.read_csv("data.csv")

#parse the database and extract items that purchased together in each transaction
def extract_purchased_item(data):
	total_list = []
	for ids in range(len(data)):
	    trans_row = data.iloc[ids]
	    count = -1
	    row_list = []
	    for element in trans_row:
	        if element == 1 and count != -1:
	            row_list.append("item_%s" % count)
	        count +=1
	    total_list.append(row_list) 
	return total_list


def main():

	data = pd.read_csv("data.csv")

	items_list = extract_purchased_item(data)

	with open('inputdata.txt', 'wb') as f:
		writer = csv.writer(f, delimiter = ',')
		for line in items_list:
			writer.writerow(line)


if __name__ == "__main__":
    main()


