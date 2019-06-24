class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,overview,category):
        self.id =id
        self.name= name
        self.overview = overview
        self.category = category    





class Article:
    '''
    Articles class

    '''
   

    def __init__(self,id,name,description,author,url):
        self.id = id
        self.name = name
        self.description = description
        self.author = author
        self.url = url

