import sys
from unittest import result
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

if len(sys.argv) < 3:
    print("Usage: python3 scrape.py <date> <xslx>")
    exit(1)

desired_date = sys.argv[1]
outpath = sys.argv[2]

url = 'https://discoveratlanta.com/events/all/'

## Your code here
web_page = rq.get(url)

#setup dictionary for dataframe
excel_data = {
    'title':[],
    'links':[]
}

#setup soup object
soup_obj = bs(web_page.content, 'html.parser')

#get all article tags
all_event_list = soup_obj.find_all('article', class_ = 'listing')

#loop through all articles to get titles and links if date is present in
#date-eventdates. If found then get titles from h4 tag and links from a tag
for event in all_event_list:
    if event['data-eventdates'].find(desired_date) != -1:
        excel_data['title'].append(event.find('h4', class_ = 'listing-title').getText())
        excel_data['links'].append(event.find('h4', class_ = 'listing-title').find('a').attrs['href'])

#create excel file
df = pd.DataFrame(excel_data)
write_excel = pd.ExcelWriter(outpath)
sheetname = 'Events'
df.to_excel(write_excel, sheet_name= sheetname, index=False)

#adjust columns of file dynamically
for column in df:
    col_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    write_excel.sheets[sheetname].set_column(col_idx, col_idx, col_width)
write_excel.save()
