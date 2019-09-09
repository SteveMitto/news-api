from . import main
from flask import render_template as r_t

@main.app_errorhandler(404)
def error_page(error):
    return r_t('four04.html')
