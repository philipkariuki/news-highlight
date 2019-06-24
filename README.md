# News Highlights

IP for MC18 week 2 of Python that requires creating a news highlights website using thenews api and deploying it to heroku.


#### By **Philip Kariuki**
## Description
##### Week 2 independent project for Moringa Core 18.
The project requires creating a news highlights website using thenews api and deploying it to heroku.
#### User Stories
* As a user, I would like to see various news sources on the homepage of the application..
* As a user, I would also want to select a news source and see all news articles from the selected news source in the application.
* As a user, I would want to see the image, description and the time a news article was created.
* As a user, I would want to click on an article and read the full article on the source website.
## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

## Setup/Installation Requirements
* Python 3.6
* pip
* gunicorn
* UNIX based OS because of gunicorn

To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/news-highlight/

To run the Python application within the folder from your cli:
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python
        
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script
        
* Setting up the API Key
        
        To be able to gather article info from the News API you will need an API Key.
        
        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it: 
        
                export NEWS_API_KEY='<Your-Api-Key>'
                python3.6 manage.py server
                
        * Insert the API Key you received from News Api where <Your-Api-Key> is.
        
* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh
## Known Bugs
No bugs at the moment.
## Languages and dependencies used
* Python 3.6
* Flask
* pip v19
* gunicorn
## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## [License](https://github.com/philipkariuki/news-highlight/blob/master/LICENSE)
MIT © 2019 [philipkariuki](https://github.com/philipkariuki
