## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization 
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoyâs research is motivated by an interest in comparative political institutions and political violence. 
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page

# import the necessary packages

from bs4 import BeautifulSoup
import urllib.request
import csv 

# Defining the webpage

web_address = 'https://polisci.wustl.edu/people/88/all'

# Opening the webpage

web_page = urllib.request.urlopen(web_address)

# Scapping the webpage

soup = BeautifulSoup(web_page.read())

# Getting the wanted information

fields.find_all("span")[0].string

all_a_tags = soup.find_all('a')

fields = soup.find_all('h3') # list of html entries

all_a_tags[0].attrs





# Generating the csv

my_csv = {}  
for i in range(all_a_tags):
  my_csv["last name"] = 
  all_a_tags.div
