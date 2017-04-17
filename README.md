# williambengtsson-heroku

## Development
#### Update requirements.txt
`$ pip freeze > requirements.txt`

#### Install the libraries from a requirements file
`$ pip install -t lib -r requirements.txt`

#### Install and add package to requirements.txt
`$ pip install [package] && pip freeze > requirements.txt`

#### Run locally
`$ cd williambengtsson`  
`$ virtualenv venv`  
`$ source venv/Scripts/activate`
In Windows use *venv\Scripts\activate.bat* instead  
`$ pip install -r requirements.txt` 
`$ python main.py`  

## Deployment

#### Deploy on Google App Engine
In Google Cloud SKD Shell:  
`> gcloud app deploy`  
Use *app.yaml* for configuration  

#### Deploy on Heroku
`$ git push heroku master`  
`$ heroku open`  
Use *Procfile* for configuration  

## Notes
Heroku-Flask skeleton created with http://www.gtlambert.com/blog/deploy-flask-app-to-heroku
