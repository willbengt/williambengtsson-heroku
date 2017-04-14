from flask import Flask, send_file
from monkeylearn import MonkeyLearn
import json

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("templates/index.html")

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
  #return json.dumps(parsed, indent=4, sort_keys=True)
  #return flask.jsonify(parsed)
  return json.dumps(parsed, sort_keys = True, indent = 4, separators = (',', ': '))