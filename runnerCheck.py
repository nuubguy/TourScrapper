#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup
import bs4

class Scrappering:
   def initScrapper(self,surl):
       url = surl
       response = requests.get(url)
      #  result =[]
       soup = bs4.BeautifulSoup(response.text,'lxml')
       result = soup.select('.listing_title')
       for start in result:
          print start.getText()


    
emp1 = Scrappering()
emp1.initScrapper("https://www.tripadvisor.com/Attractions-g297733-Activities-c57-Lombok_West_Nusa_Tenggara.html#FILTERED_LIST",)