import requests
from config import Config
from .models import NewsSource

api_key =Config.API_KEY
source_url =f'https://newsapi.org/v2/sources?apiKey={api_key}'


def get_sources():
    response = requests.get(source_url)

    sources_list = []
    if response.status_code == 200:
        json_response = response.json()
        sources = json_response['sources']

        for source in sources:
            id= source.get('id')
            name = source.get('name')
            descreption = source.get('description')
            url = source.get('url')
            category = source.get('category')
            language = source.get('language')
            country = source.get('country')

            source_object = NewsSource(id,name,descreption,url,category,language,country)
            source_list.append(source_object)
        return sources_list

    else:
        return None
