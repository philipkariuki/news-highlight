   
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
    world_sources = get_sources('world')
    sports_sources = get_sources('sports')
    business_sources = get_sources('business')
    buzz_sources = get_sources('buzz')
    tech_sources = get_sources('tech')

    title = 'Home - 👀 News Watch - Only the real(not fake) news.'

    return render_template('index.html', title=title,world=world_sources,sports=sports_sources,business=business_sources,buzz=buzz_sources,tech=tech_sources)

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