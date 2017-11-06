# Setting Up Flask
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
server = Flask(__name__)

import os
import sqlite3 as sql

# Importing Other Modules
import requests
import datetime

# Importing Custom Modules
from app import main

@server.route('/hello')
def hello():
    return 'Hello World!'

# Serving HTML Pages/Templates

@server.route('/')
def home():
    return render_template('index.html', name='Visitor')
    
@server.route('/name/<name>')
def name(name=None):
    return render_template('index.html', name=name)
    
@server.route('/sample')
def sample():
    return render_template('map.html')
    
@server.route('/locations')
def locations():
    return render_template('locations.html') 

@server.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Responding to Requests with Data

@server.route('/reflect/<name>')
def reflect(name=None):
    r = {'name': name}
    return jsonify(r)
    
@server.route('/weather')
def weather():
    w = main.get_weather()
    return jsonify(w)
    
@server.route('/location_image/<search>')
def location_image(search):
    geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
    geo_query = {
        "address": search
    }
    geo_res = requests.request("GET", geo_url, params=geo_query);
    geo_data = geo_res.json();
    loc = geo_data['results'][0]['geometry']['location'];
    url = "https://maps.googleapis.com/maps/api/streetview"
    querystring = {
        "size": "600x600",
        "location": str(loc['lat']) + "," + str(loc['lng']),
        "heading": "90",
        "pitch": "0"
    }
    response = requests.request("GET", url, params=querystring)
    return response.url;
    
    
@server.route('/rate')
def new_student():
   return render_template('rating.html')
   
@server.route('/rate',methods = ['POST', 'GET'])
def rate():
   if request.method == 'POST':
      
      try:
         title = request.form['title']
         review = request.form['review']
         rating = request.form['rating']
         name = request.form['name']
         date = datetime.datetime.now()
         msg = " "
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO ratings (title,review,rating,name,date) VALUES (?,?,?,?,?)",(title,review,rating,name,date) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg=msg)
         con.close()