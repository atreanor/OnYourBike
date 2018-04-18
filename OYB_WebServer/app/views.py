from flask import Flask, render_template, jsonify, g 
from app import app, model
import json
import simplejson
#import sqlalchemy
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
#from instance import config

#from config import *  



# three database connect/close connection functions:
def connect_to_database():
    ''' method to connect to database ''' 
    #return engine = create_engine("mysql+mysqldb://{}@{}:{}/{}".format(config.USER, config.PASSWORD, config.URI, config.PORT, config.DB), echo=True)
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)
    return engine 

def get_db():
    ''' method to get database '''
    db = getattr(g, 'onyourbikemysql', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    ''' method to close connection with database '''
    db = getattr(g, 'onyourbikemysql', None)
    if db is not None:
        db.close()


#Flask functions to query DB and return jsonified version of query results
@app.route('/')
def index():
    a = {}
    a['title'] = 'OnYourBike with DublinBikes'
    jsonify(a=a)
    return render_template("index.html", **a)

@app.route('/getStations')
def getStations():
    engine = get_db()
    info = []
    rows = engine.execute("SELECT name, number, available_bike_stands, available_bikes, lat, lng FROM JCD_flask")
    for row in rows:
        info.append(dict(row))
    return jsonify(info=info)

@app.route('/getweather')
def getweather():
    engine = get_db()
    weather = []
    rows = engine.execute("SELECT w_d_main, w_description, temp, temp_min, OYB_timestamp FROM OpenWeatherMap.OWM_current WHERE OYB_timestamp =(SELECT MAX(OYB_timestamp) FROM OpenWeatherMap.OWM_current);")
    for row in rows:
        weather.append(dict(row))
    return jsonify(weather=weather)


@app.route("/available/<int:number>")
def getGraphData(number):
    ''' method to retrieve station data specific to the selected on map, station number will be 
    passed as an argument into SQL statement to retrieve data specific to that station '''
    engine = get_db()
    data = []
    rows = engine.execute("SELECT available_bikes, available_bike_stands, OYB_timestamp FROM JCD_dynamic_data, WHERE number={};".format(number))
    for row in rows:
        graphData.append(dict(row))
    return jsonify(available = data)
        
        
        



