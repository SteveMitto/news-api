from . import main
from flask import render_template as r_t
@main.route('/')
def main():
    return "Hello world"
