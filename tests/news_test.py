    
import unittest
from app.models import Source, Article


class SourceTest(unittest.TestCase) :
  '''
  Test class to test the behaviour of the ources class
  '''

  def setUp(self) :
    '''
    Set up method that will run before every test 
    '''
    self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

  def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_source,Source))




class ArticleTest(unittest.TestCase) :
  '''
  Test class to test the behaviour of the ources class
  '''

  def setUp(self) :
    '''
    Set up method that will run before every test 
    '''
    self.new_article = Article("null", "YG, DJ Khaled & Marsha Ambrosius & John Legend Perform Tribute to Nipsey Hussle | BET Awards 2019 - BETNetworks", "null", "https://www.youtube.com/watch?v=ILMeLOkDxfk", "null", "2019-06-24T08:00:03Z", "[[getSimpleString(data.title)]]\r\n[[getSimpleString(data.description)]]\r\n[[getSimpleString(data.videoCountText)]]")

  def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_article,Article))





if __name__ == '__main__' :
  unittest.main()