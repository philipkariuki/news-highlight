   
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles


# Views
@main.route('/')
def index():
    '''
    View Function that returns the index page and its data
    '''
    # Getting sources according to category
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')

    title = '👀 News Watch 👀 : Only the real(not fake) news.'

    return render_template('index.html', title=title,general=general_sources,sports=sports_sources,business=business_sources,entertainment=entertainment_sources,technology=technology_sources)






@main.route('/source/<id>')
def source(id):
    '''
    View Function that returns the source page and its data
    '''
    # Getting articles according to source chosen
    articles = get_articles(id)
    source_id = id.upper()
    title = f'{source_id} - Top Articles'

    return render_template('news.html',title=title,id=source_id, articles=articles)