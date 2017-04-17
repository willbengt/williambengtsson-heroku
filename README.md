# williambengtsson-heroku

Heroku-Flask skeleton created with http://www.gtlambert.com/blog/deploy-flask-app-to-heroku

Run locally:
$ cd williambengtsson
$ virtualenv venv
$ source venv/Scripts/activate (Windows: venv\Scripts\activate.bat)
$ pip install -r requirements.txt
$ python main.py

Deploy:
$ git push heroku master
$ heroku open
