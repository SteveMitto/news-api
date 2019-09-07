class NewsSource:
    def __init__(self,id,name,url,category,language,country):
        '''This function creates an object for the news sources'''
        self.id= id
        self.name = name
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class NewsArticle:
    def __init__(self,author,title,description,image,published,content):
        ''' This function creates an instance of a source news '''
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.published = published
        self.content = content
