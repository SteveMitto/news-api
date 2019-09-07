from . import main
from flask import render_template as r_t
from ..request import get_sources
@main.route('/')
def main():
    sources = get_sources()
    return r_t('index.html', sources = sources)
