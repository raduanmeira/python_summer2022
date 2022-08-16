################################################################################
#
# Raduan van Velthem Meira
# Python summer course 2022 -- Homework 2
# August 17, 2022
#
################################################################################

# Libraries and imports 

from bs4 import BeautifulSoup
import urllib.request
import sys
import os
import time
import csv



# I am using the link with 60 results per page because it is easier
# and less demanding for UCSB servers

# I can use only "homework.csv" as my path because I am working on a 
# RStudio project which already have a predefined path.

with open('homework.csv', 'w', encoding="utf-8") as f: 
  w = csv.DictWriter(f, fieldnames = ("Date", "Title", "Text", "Note"))
  w.writeheader()
  web_address = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?items_per_page=60"
  web_page = urllib.request.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  breaker = False

  for main in range(1,12):
    if main > 1:
      print(f"Working on page {main}")
      main_page = soup.find('a', title = f"Go to page {main+1}")["href"]
      web_page = urllib.request.urlopen(f"https://www.presidency.ucsb.edu/{main_page}") # this open the link
      time.sleep(5)
      soup = BeautifulSoup(web_page.read())
      sub_all = soup.find_all('div', class_ = "field-title" )
      for sub in range(0,60):
        sub_page = sub_all[sub].a["href"]
        sub_web_page = urllib.request.urlopen(f"https://www.presidency.ucsb.edu/{sub_page}") 
        time.sleep(3) # To avoid taking too much time
        sub_soup = BeautifulSoup(sub_web_page.read())
        address = {}
        address["Title"] = sub_soup.find('div', class_ = 'field-ds-doc-title').text[1:-1] # dropping the /n
        address["Date"] = sub_soup.find('div', class_ = 'field-docs-start-date-time').span.text
        address["Text"] = sub_soup.find('div', class_ = 'field-docs-content').text[1:]
        try:
          address["Note"] = sub_soup.find("div", class_ = "field-docs-footnote").p.text
        except:
          address["Note"] = 'NA'
        w.writerow(address)
        if address["Date"] == 'January 20, 2021':
          breaker = True
          break
      
      if breaker == True:
          break
        
    if breaker == True:
          break  
        
    else:
      sub_all = soup.find_all('div', class_ = "field-title" )
      for sub in range(0,60):
        sub_page = sub_all[sub].a["href"]
        sub_web_page = urllib.request.urlopen(f"https://www.presidency.ucsb.edu/{sub_page}") 
        time.sleep(3) # To avoid taking too much time
        sub_soup = BeautifulSoup(sub_web_page.read())
        address = {}
        address["Title"] = sub_soup.find('div', class_ = 'field-ds-doc-title').text[1:-1] # dropping the /n
        address["Date"] = sub_soup.find('div', class_ = 'field-docs-start-date-time').span.text
        address["Text"] = sub_soup.find('div', class_ = 'field-docs-content').text[1:]
        try:
          address["Note"] = sub_soup.find("div", class_ = "field-docs-footnote").p.text
        except:
          address["Note"] = 'NA'
        w.writerow(address)

  
# Smaller chunck that I used to test the code

  
#with open('homework.csv', 'w') as f:
#  w = csv.DictWriter(f, fieldnames = ("Date", "Title", "Text", "Note"))
#  w.writeheader()
#  web_address = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?items_per_page=60"
#  web_page = urllib.request.urlopen(web_address)
#  soup = BeautifulSoup(web_page.read())
#  sub_all = soup.find_all('div', class_ = "field-title" )
#  for sub in range(0,17):
#    print(f"{sub}")
#    sub_page = sub_all[sub].a["href"]
#    sub_web_page = urllib.request.urlopen(f"https://www.presidency.ucsb.edu/{sub_page}") 
#    time.sleep(3) # To avoid taking too much time
#    sub_soup = BeautifulSoup(sub_web_page.read())
#    address = {}
#    address["Title"] = sub_soup.find('div', class_ = 'field-ds-doc-title').text[1:-1] # dropping the /n
#    address["Date"] = sub_soup.find('div', class_ = 'field-docs-start-date-time').span.text
#    address["Text"] = sub_soup.find('div', class_ = 'field-docs-content').text[1:]
#    try:
#      address["Note"] = sub_soup.find("div", class_ = "field-docs-footnote").p.text
#    except:
#      address["Note"] = 'NA'
#    w.writerow(address)

