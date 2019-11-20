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


   def initBs4(self, url):
     return bs4.BeautifulSoup(requests.get(url).text,'lxml')

   def fillPlace(self, result, finalResult):
     for start in result:
          finalResult.append(start.getText())



   def initScrapper(self,surl):
       finalResult = []
       url = surl

       soup = self.initBs4(url)

      # find element inside a html tag based on class and element tag with 2 different class
       result = soup.select('.listing_title > a, .title_with_snippets > a')
       
       while len(finalResult) < 500:
        self.fillPlace(result,finalResult)
        secondTemp = "https://www.tripadvisor.co.id"+(soup.select('.unified > a, .pagination > a')[0])["href"]
        result = self.initBs4(secondTemp).select('.listing_title > a, .title_with_snippets > a')
        print(len(finalResult))

        
        print(finalResult)       
        

      #  print(finalResult)
    

            

      # while len(finalResult)<500:

         
         
         
         
         
         
         


       

         

         

       
      #  print(secondTemp)
      #  print(finalResult)    
        
      




    
emp1 = Scrappering()
emp1.initScrapper("https://www.tripadvisor.co.id/Attractions-g297733-Activities-Lombok_West_Nusa_Tenggara.html")