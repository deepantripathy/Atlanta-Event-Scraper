# Web-Scrapper
Read a website to make a list of events happening on a date

The code takes date as input and filters out all the events happening on that date and creates an excel file with 2 columns
column1: title
column2: link

Library used: BeautifulSoup

We use BeautifulSoup to create a soup object and parse the entire website and pass the data collected into a dictionary object.
This dictionary object is then passed into a pandas dataframe, and then it is used to create an excel file using ExcelWriter.
