# williambengtsson-heroku

## Development
### Update requirements.txt:
`$ pip freeze > requirements.txt`

Install the libraries from a requirements file:
$ pip install -t lib -r requirements.txt

Install and add to requirements.txt:
$ pip install [package] && pip freeze > requirements.txt


Run locally:
$ cd williambengtsson
$ virtualenv venv
$ source venv/Scripts/activate (Windows: venv\Scripts\activate.bat)
$ pip install -r requirements.txt
$ python main.py

Deploy:
$ git push heroku master
$ heroku open

## Notes
Heroku-Flask skeleton created with http://www.gtlambert.com/blog/deploy-flask-app-to-heroku
