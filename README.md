# williambengtsson-python

make sure reuirements are updated:
$ pip freeze > requirements.txt

Install the libraries from a requirements file:
$ pip install -t lib -r requirements.txt

Install and add to requirements.txt
$ pip install [package] && pip freeze > requirements.txt

Run locally:
$ cd williambengtsson-python
$ virtualenv env
$ source env/Scripts/activate (Windows: env\Scripts\activate.bat)
$ pip install -r requirements.txt
$ python main.py
