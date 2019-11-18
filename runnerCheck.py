#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup
import bs4

class Scrappering:
   'Common base class for all employees'
   empCount = 0  
   

   def initScrapper(self,surl):
       url = surl
       response = requests.get(url)
       soup = bs4.BeautifulSoup(response.text,'lxml')
       print type(soup)
       result = soup.select('.listing_title > a, .title_with_snippets > a')
       
       for start in result:
          print start.getText()


    
emp1 = Scrappering()
emp1.initScrapper("https://www.tripadvisor.co.id/Attractions-g297733-Activities-Lombok_West_Nusa_Tenggara.html",)