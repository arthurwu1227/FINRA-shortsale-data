#this script took around 53 minutes to run
#import needed libraries
import requests
import pandas as pd
import os

#indicate the start and end dates. "date" indicates start date for now, but it is simply
#referred to as "date" since it is also the variable that will be incremented.
#The chicagoStart variable is the variable at when collecting data from the chicago
#exchange should start. If the date the script is on is greater than or equal
#to this variable, it will also collect data on the chicago exchange.
date = pd.to_datetime('2009-08-01')
end = pd.to_datetime('2023-05-19')
chicagoStart = pd.to_datetime('2018-08-01')

#directory (folder) I want it saved. Update this with your own folder.
save_directory = '/Users/arthurwu/Desktop/FINRAdata'

#while the script has not reached the end, print the date we are on, and for each
#URL of the exchanges we want to collect (ADF=FNRA, NASDAQ=FNSQ, ORF=FORF, NYSE=FNYX
#as well as FNQC for chicago during and after 8/01/18, make a HTTP request for that
#link and save the link's file text inside my folder.
while date <= end:
    print(f"On:{date}")
    datestr = date.strftime('%Y%m%d')
    urls = [
        f'https://cdn.finra.org/equity/regsho/daily/FNSQshvol{datestr}.txt', 
        f'https://cdn.finra.org/equity/regsho/daily/FNYXshvol{datestr}.txt', 
        f'https://cdn.finra.org/equity/regsho/daily/FNRAshvol{datestr}.txt', 
        f'https://cdn.finra.org/equity/regsho/daily/FORFshvol{datestr}.txt'
    ]

    if date >= chicagoStart:
        urls.append(f'https://cdn.finra.org/equity/regsho/daily/FNQCshvol{datestr}.txt')
    	
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(save_directory, url[42:]), 'w') as file:
                file.write(response.text)

    date += pd.Timedelta(days=1)
