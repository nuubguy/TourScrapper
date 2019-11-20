#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup
import bs4

class TadPlace:
    def __init__(self):
      self.placeName = "null"
      self.comment = ""
      self.rating = ""     

    def get_placeName(self):
        return self.placeName
    def set_placeName(self, x):
        self.placeName = x
    def set_Comment(self, x):
        self.comment = x
    def get_Comment(self):
        return self.comment
    def set_Rating(self, x):
        self.rating = x
    def get_Rating(self):
        return self.rating
        
    def displayProp(self):
      print(self.placeName+" + "+self.comment+" + "+self.rating)





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

    # init soup for url
   def initBs4(self, url):
     return bs4.BeautifulSoup(requests.get(url).text,'lxml')

  #  add TadPlace
   def fillPlace(self, result, finalResult,soup):
     for start in result:
          currentSoup = self.initBs4("https://www.tripadvisor.co.id"+start['href'])
          currentPlace = TadPlace()
          currentPlace.set_placeName(start.text)
          currentPlace.set_Comment(self.findAllComment(currentSoup))
          currentPlace.set_Rating(self.findRating(currentSoup))
          print(currentPlace.get_placeName())
          print(currentPlace.get_Comment())
          print(currentPlace.get_Rating())
          finalResult.append(start.text)

   def findRating(self, soup):
     return soup.select('.overallRating')[0].text


   def findAllComment(self, soup):
     comments = soup.select('.noQuotes')
     result = []
     for comment in comments:
       result.append(comment.text) 
     return result




  #  def findDetailPage(self)
   def reloadNextPage(self,soup):
        secondTemp = "https://www.tripadvisor.co.id"+(soup.select('.unified > a, .pagination > a')[0])["href"]
        return self.initBs4(secondTemp)

  #  find place name      
   def findElementPlaceName(self, soup):
        return soup.select('.listing_title > a, .title_with_snippets > a')



   def initScrapper(self,surl):
       finalResult = []
       url = surl

       soup = self.initBs4(url)

      # find element inside a html tag based on class and element tag with 2 different class
       result = self.findElementPlaceName(soup)
       
       while len(finalResult) < 500:
        self.fillPlace(result,finalResult,soup)
        soup = self.reloadNextPage(soup)
        result = self.findElementPlaceName(soup)
        print(len(finalResult))

        
       print(finalResult)
        

      #  print(finalResult)
    

            

      # while len(finalResult)<500:

         
         
         
         
         
         
         


       

         

         

       
      #  print(secondTemp)
      #  print(finalResult)    
        
      




    
emp1 = Scrappering()
emp1.initScrapper("https://www.tripadvisor.co.id/Attractions-g297733-Activities-Lombok_West_Nusa_Tenggara.html")