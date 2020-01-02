#!/usr/bin/python
import requests
# from beautifulsoup4 import beautifulsoup4
import bs4
import xlsxwriter

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

  

    # init soup for url
   def initBs4(self, url):
     return bs4.BeautifulSoup(requests.get(url).text,'lxml')

  #  add TadPlace
   def fillPlace(self, result, finalResult, soup, index, sheet):
     indexStart = index
     
     for start in result:
          currentSoup = self.initBs4("https://www.tripadvisor.co.id"+start['href'])
          sheet.write(indexStart,0,start.text)
          sheet.write(indexStart,1,''.join(self.findAllComment(currentSoup)))
          sheet.write(indexStart,2,self.findRating(currentSoup))
          sheet.write(indexStart,3,self.findImage(currentSoup))
          sheet.write(indexStart,4,self.findLocation(currentSoup))
          sheet.write(indexStart,5,self.openingHour(currentSoup))
          indexStart+=1
          print(start.text)
     return indexStart        

   def findRating(self, soup):
     return soup.select('.overallRating')[0].text
   
   def findLocation(self, soup):
     if len(soup.select('.locality'))==0:
       return "TBA"

     return soup.select('.locality')[0].text

   def findImage(self, soup):
     images = soup.select('div > .basicImg')
     result = ""
     for image in images:
       result+= "["+image['data-lazyurl']+"]"
     return result    

   def openingHour(self,soup):
      if len(soup.select('.public-location-hours-LocationHours__bold--2oLr-, .public-location-hours-LocationHours__green--2VoIr'))==0:
        return "TBA"
      return soup.select('.public-location-hours-LocationHours__bold--2oLr-, .public-location-hours-LocationHours__green--2VoIr')[0].find_next_sibling().text
   
   def recommendationHourToStay(self,soup):
     return soup.select('.attractions-attraction-detail-about-card-AboutSection__sectionWrapper--3PMQg')[0].text

   def findAllComment(self, soup):
     comments = soup.select('.location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT > span')
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
       
       workbook = xlsxwriter.Workbook('BaliScrapper.xlsx')
       worksheet = workbook.add_worksheet()
       worksheet.write(0,0,"Place")
       worksheet.write(0,1,"Comment")
       worksheet.write(0,2,"Rating")
       worksheet.write(0,3,"Image")
       worksheet.write(0,4,"Location")
       worksheet.write(0,5,"Opening Hour")
       
    

       soup = self.initBs4(url)

      # find element inside a html tag based on class and element tag with 2 different class
       result = self.findElementPlaceName(soup)
       index =1
       while index < 800:
        index = self.fillPlace(result,finalResult,soup,index,worksheet)
        print(index)
        soup = self.reloadNextPage(soup)
        result = self.findElementPlaceName(soup)
        

       workbook.close() 
           
        
    




    
emp1 = Scrappering()
emp1.initScrapper("https://www.tripadvisor.co.id/Attractions-g294226-Activities-Bali.html")