#!/usr/bin/env_python
from flask import Flask, g, jsonify
app = Flask(__name__)


def connect_to_database():
    """ method to connect to database """

    engine = create_engine("mysql+mysqldb://{}@{}:{}/{}".format(config.USER, config.PASSWORD, config.URI, config.PORT,
                                                                config.DB), echo=True)
    return engine 


def get_db():
    """ method to get database """

    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_databse()
    return db


@app.teardown_appcontext
def close_connection():
    """ method to close connection with database """

    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
# route to serve 'static/index.html'
# @app.route('/')
# def root():
#    ''' method to serve 'static/index.html' '''
#    return render_template('index.html', MAPS_APIKEY=app.config["MAPS_APIKEY"])


@app.route("/stations")
def get_station_lite():
    """ method to retrieve station data required to populate markers when app is launched """

    # create connection with database on RDS
    engine = get_db()
    
    # initialise stations list
    stations = []
    # MySQL query to retrieve data
    rows = engine.execute("SELECT number, position FROM JCD_staticdata;")
    for row in rows:
        stations.append(dict(row))

    return jsonify(stations=stations)


def get_station_info():
    """ method to retrieve a larger data set to populate additional station info & on a refresh of the app """

    # create connection with database on RDS
    engine = get_db()
    # initialise list
    info = []
    # MySQL query to retrieve data
    rows = engine.execute("SELECT number, address, banking, status, bike_stands, available_bike_stands, "
                          "available_bikes, last_update FROM JCD_dynamicdata, JCD_staticdata WHERE "
                          "number.JCD_dynamic_data = number.JCD_static_data;")
    for row in rows:
        info.append(dict(row))

    return jsonify(info=info)
    

def get_weather():
    """ method to retrieve weather data on launch of app """

    # create connection with database on RDS
    engine = get_db()
    # initialise list
    weather = []
    # MySQL query to retrieve data
    rows = engine.execute("SELECT ..... FROM .... ;")
    for row in rows:
        weather.append(dict(row))

    return jsonify(weather=weather)
    
    
if __name__ == "__main__":
    app.run(debug=True)
