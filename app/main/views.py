from . import main as news
import random
from flask import render_template as r_t
from ..request import get_sources,get_source_article
@news.route('/')
def main():
    sources = get_sources()
    source_len =len(sources)
    rand_source = random.randint(0,source_len-1)
    rand_source_id = sources[rand_source].id
    if rand_source_id == 'bloomberg':
        rand_source = random.randint(0,source_len-1)
        breakingNews = get_source_article(rand_source_id)[0]
        brekingSite = sources[rand_source].name
    else:
        breakingNews = get_source_article(rand_source_id)[0]
        brekingSite = sources[rand_source].name

    return r_t('index.html', sources = sources , breakingNews = breakingNews , brekingSite =brekingSite)

@news.route('/news-article/<source_id>')
def news_article(source_id):
    articles = get_source_article(source_id)
    sources = get_sources()
    title = None
    articles_len= len(articles)
    rand_article = random.randint(0,articles_len-1)
    randTop =articles[rand_article]
    for source in sources:
        if source_id == source.id:
            title = source.name
    articles.pop(rand_article)
    print(articles)
    # tite = list(id.splice("-"))
    # title= ''.join(tite)


    return r_t('news_article.html', title = title, articles = articles,randTop = randTop)
