from flask import Flask, request, jsonify 
from flask_cors import CORS, cross_origin
from scrape_benefits import web_scraper
from nutrition import *
app = Flask(__name__)
CORS(app)

@app.route('/',methods=["GET"])
@cross_origin()
def home():
    return "Server is running"

@app.route('/api/<foods>',methods=["GET"])
@cross_origin()
def get_foods(foods):
    data = foods #example this is a food string
    #turning into array cause this is scuffed
    food_array = data.split('+')
    summaries = web_scraper(food_array)
    return summaries

@app.route('/api/score/<foods>', methods=["GET"])
@cross_origin()
def get_score(foods):
    data = foods 
    food_array = data.split('+')
    data = grade(foods)
    return data


@app.route('/api/data/<foods>', methods=["GET"])
@cross_origin()
def get_api(foods):
    data = foods 
    food_array = data.split('+')
    data = nut_sum(food_array)
    return data