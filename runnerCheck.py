#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup
import bs4

class Scrappering:
   'Common base class for all employees'
   empCount = 0  
   
   def detailPlace(self, url):
      response = requests.get("https://www.tripadvisor.co.id"+url)
      soup = bs4.BeautifulSoup(response.text,'lxml')
      result = soup.select('.noQuotes')
      if len(result)==0:
        return

      for start in result:
        print start.getText()  




   def initScrapper(self,surl):
       url = surl
       response = requests.get(url)
       soup = bs4.BeautifulSoup(response.text,'lxml')

      # find element inside a html tag based on class and element tag with 2 different class
       result = soup.select('.listing_title > a, .title_with_snippets > a')

       
       for start in result:
         #  text for place name
          print start.getText()
          self.detailPlace(start['href'])
          print('------------------------------------------')
          
         #  link for detail page
         #  print start["href"]




    
emp1 = Scrappering()
emp1.initScrapper("https://www.tripadvisor.co.id/Attractions-g297733-Activities-Lombok_West_Nusa_Tenggara.html")