import datetime
class NewsSource:
    def __init__(self,id,name,url,description,category,language,country):
        '''This function creates an object for the news sources'''
        self.id= id
        self.name = name
        self.url = url
        self.description = description
        self.category = category.capitalize()
        self.language = language
        self.country = country

class NewsArticle:
    def __init__(self,author,title,description,url,image,published,content):
        ''' This function creates an instance of a source news '''
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.published = published
        self.content = content
