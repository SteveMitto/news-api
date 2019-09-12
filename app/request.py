import requests
from config import Config
from .models import NewsSource,NewsArticle

api_key =Config.API_KEY
source_url =f'https://newsapi.org/v2/sources?language=en&apiKey={api_key} '

def get_sources():
    response = requests.get(source_url)

    sources_list = []
    if response.status_code == 200:
        json_response = response.json()
        sources = json_response['sources']

        for source in sources:
            id= source.get('id')
            name = source.get('name')
            description = source.get('description')
            url = source.get('url')
            category = source.get('category')
            language = source.get('language')
            country = source.get('country')

            source_object = NewsSource(id,name,url,description,category,language,country)
            sources_list.append(source_object)
        return sources_list

    else:
        return None
def get_source_article(source_id):
    ''' This function gets articles of a certain news source '''
    source_articles_url = f'https://newsapi.org/v2/top-headlines?sources={source_id}&apiKey={api_key}'

    response = requests.get(source_articles_url)
    articles_list=[]
    if response.status_code == 200:
        response_json = response.json()
        articles = response_json['articles']

        for article in articles:
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            image = article.get('urlToImage')
            published = article.get('publishedAt')
            content = article.get('content')

            if image:
                if description == 'None':
                    description = content
                    article_object = NewsArticle(author,title,description,url,image,published,content)
                    articles_list.append(article_object)
                else:
                    article_object = NewsArticle(author,title,description,url,image,published,content)
                    articles_list.append(article_object)
            elif image == '':
                image ='../static/images/news.jpg'
                if description == 'None':
                    description = content
                    article_objectw = NewsArticle(author,title,description,url,image,published,content)
                    articles_list.append(article_object)
                else:
                    article_object = NewsArticle(author,title,description,url,image,published,content)
                    articles_list.append(article_object)

    return articles_list
