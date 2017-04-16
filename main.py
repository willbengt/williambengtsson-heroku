from flask import Flask, send_file, request, jsonify, render_template
#from flask_cors import CORS
from monkeylearn import MonkeyLearn
from flask_api import FlaskAPI
import json

app = FlaskAPI(__name__)
#app = Flask(__name__)
#CORS(app)

@app.route("/")
def index():
    return send_file('templates/index.html')

@app.route('/getData/')
def getData():
  return {'name':'roy'}

# @app.route('/Authenticate',methods=['POST'])
# def Authenticate():
#     content = request.json
#     return jsonify({'username':content['username'],'password':content['password']})

# @app.route('/home')
# def home():
#   bla = 'blah..blah...'
#   return render_template('home.html', bla=bla)

@app.route("/ml")
def ml():
  ml = MonkeyLearn("f0662751f5792b646356ec5516580c239b71aefb")
  text_list = ["Disney Pixar Cars Toon: Mater's Tall tales - Walmart (Wii) Cars Toon: Mater's Tall Tales [Disney Pixar], a Nintendo console exclusive, is a comedy themed mini-game(s) / party game with action racing elements."]
  module_id = 'cl_oFKL5wft'
  res = ml.classifiers.classify(module_id, text_list, sandbox=True)
  list1 = res.result
  str1 = ''.join(str(e) for e in list1)
  str2 = str1.rstrip('\n')
  str3 = str2.replace("u'", "'")
  str4 = str3.replace("'", '"')
  parsed = json.loads(str4)
  return parsed


if __name__=="__main__":
  app.run(debug=True)