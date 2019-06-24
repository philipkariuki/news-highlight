import urllib.request,json
from .models import Source,Article


# Getting api key
api_key = None
# Getting the news base url
base_url = None
article_url = None


def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url=app.config['NEWS_ARTICLE_URL']




def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)


    return sources_results





def get_articles(id):
    '''
    Function that gets the json response to url request
    '''
    get_article_news_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_article_news_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results




def process_sources_results(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        overview = source_item.get('overview')
        category = source_item.get('category')

        if name:
            sources_object = Movie(id,name,overview,category)
            sources_results.append(sources_object)

    return sources_results