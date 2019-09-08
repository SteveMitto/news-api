from . import main as news
import random
from flask import render_template as r_t
from ..request import get_sources,get_source_article
@news.route('/')
def main():
    sources = get_sources()
    return r_t('index.html', sources = sources)

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
