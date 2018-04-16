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

@app.route('/getjson')
def getjson():
    engine = get_db()
    info = []
    rows = engine.execute("SELECT name, number, available_bike_stands, available_bikes, lat, lng FROM JCD_flask")
    for row in rows:
        info.append(dict(row))
    return jsonify(info=info)




@app.route('/getweather')
def getweather():
    w = {}
    w['description'] = {"main":"clouds","description":"overcast clouds","icon":"04n"} 
    w['temp']= 12
    w['tempmin'] = 7
    return jsonify(w=w)





# 
# @app.route("/stations")            
# def getStationLite():
#     ''' method to retrieve station data required to populate markers when app is launched '''
#     #create connection with database on RDS
#     engine = get_db()
#     
#     # initialise stations list
#     stations = []
#     # MySQL query to retrieve data
#     rows = engine.execute("SELECT number, position FROM JCD_staticdata;")
#     for row in rows:
#         stations.append(dict(row))
#     return jsonify(stations=stations)


# def getStationInfo():
#     ''' method to retrieve a larger data set to populate additional station info & on a refresh of the app '''
#     #create connection with database on RDS
#     engine = get_db()
#     
#     # initialise list
#     info = []
#     # MySQL query to retrieve data
#     rows = engine.execute("SELECT number, address, banking, status, bike_stands, available_bike_stands, available_bikes, last_update FROM JCD_dynamicdata, JCD_staticdata WHERE number.JCD_dynamic_data = number.JCD_static_data;")
#     for row in rows:
#         info.append(dict(row))
#     return jsonify(info=info)
#     
# 
# def getWeather():
#     ''' method to retrieve weather data on launch of app  '''
#     #create connection with database on RDS
#     engine = get_db()
#      
#     # initialise list
#     weather = []
#     # MySQL query to retrieve data
#     rows = engine.execute("SELECT ..... FROM .... ;")
#     for row in rows:
#         weather.append(dict(row))
#     return jsonify(weather=weather)

    
# @app.route('/getjson')
# def getjson():
#     c = {}
#     c['name'] = 'Thomas Street', 'James Street', 'Stephens Green', 'Christchurch Place', 'Excise Walk', 'Fownes Street Upper', 'Custom House'  
#     c['number']= 1,2,3,4,5,6,7
#     c['available_bikes'] = '20','26','29','0','15','21','11'
#     c['free_stands'] = '13','14','15', '0','10','16','8'
#     c['lat'] = 53.3496, 53.3535, 53.336, 53.3434, 53.3478, 53.3446, 53.3483
#     c['lng'] = -6.2782, -6.26531,-6.26298, -6.27012, -6.24424, -6.26337, -6.25466
#     return jsonify(c=c)
