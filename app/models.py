class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,category,url):
        self.id =id
        self.name= name
        self.description = description
        self.category = category 
        self.url = url   





class Article:
    '''
    Articles class

    '''
   

    def __init__(self,title,description,author,url,publishedAt,urlToImage,content):
        
        
        self.title = title
        self.description = description
        self.author = author
        self.url = url
        self.publishedAt = publishedAt
        self.urlToImageImage = urlToImage
        self.content = content




