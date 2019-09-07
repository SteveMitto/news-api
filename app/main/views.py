from . import main as news
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
    for source in sources:
        if source_id == source.id:
            title = source.name
    print(articles)
    # tite = list(id.splice("-"))
    # title= ''.join(tite)


    return r_t('news_article.html', title = title, articles = articles)
