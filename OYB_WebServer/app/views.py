from flask import render_template
from flask import Flask
from flask import jsonify
from flask import g
from app import app
from app import model
import json
import simplejson
#import sqlalchemy
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
#from instance import config

#from config import *  
USER="Admin"
PASSWORD="UCD_2018"
URI="onyourbikemysql.cquggrydnjcx.eu-west-1.rds.amazonaws.com"
PORT="3306"
DB = "onyourbikemysql"


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





