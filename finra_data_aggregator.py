#import needed libraries
import pandas as pd
import os

#estalish where the FINRA data is, list all files below FiNRAdata
folder = '/Users/arthurwu/Desktop/drgiedt_internship/FINRAdata'
files = os.listdir(folder)

#initialize the list where we will store our dataframes
storage = []

#initialize the error list
errors = []

#for every file listed below FINRA data, find the exact path to that file, read
#in the file in a pipe-separated values format, and add the file to the storage dataframe
for file in files:
	path = os.path.join(folder, file)

	#there are some files in the FINRA data which are not supposed to be processed
	#such as the DS_Store file.
	try:
		df = pd.read_csv(path, sep='|')
		print(len(storage))
		print(path)
		storage.append(df)
	except:
		print("")
		print("This file has a formatting error and has not been processed:")
		print(path)
		print("")
		errors.append(path)

#print the amount of formatting errors found
#if it only prints the .DS_Store file, since I stored the directory on mac
#it means it works properly
print(errors)

#aggregate each value by date and stock ticker and find the shortvolume sum,
#shortexemptvolume sum, and total volume sum. Then reset the index.
finaldf = pd.concat(storage)
print('concatenation done')
finaldf = finaldf.groupby(['Date', 'Symbol']).agg({'ShortVolume':['sum'], 
	'ShortExemptVolume':['sum'], 'TotalVolume':['sum']}).reset_index()
print('groupby done')

#output to file "aggregated_data.csv"
finaldf.to_csv('aggregated_data.csv', index=False)

