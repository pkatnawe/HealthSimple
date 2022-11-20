from flask import Flask, request, jsonify 
from flask_cors import CORS
from scrape_benefits import web_scraper
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is running"

@app.route('/api/<foods>')
def get_foods(foods):
    data = foods #example this is a food string
    #turning into array cause this is scuffed
    food_array = data.split('+')
    summaries = web_scraper(food_array)
    return summaries

@app.route('/api/score/<foods>')
def get_score(foods):
    data = foods 
    food_array = data.split('+')
    
    