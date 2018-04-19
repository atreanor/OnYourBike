import json
import simplejson
import sqlalchemy

from sqlalchemy import create_engine

def connect_to_database():
    ''' method to connect to database ''' 
    #return engine = create_engine("mysql+mysqldb://{}@{}:{}/{}".format(config.USER, config.PASSWORD, config.URI, config.PORT, config.DB), echo=True)
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format("Admin", "UCD_2018", "onyourbikemysql.cquggrydnjcx.eu-west-1.rds.amazonaws.com", 3306, "JCD_flask"), echo=True)
    return engine

def getGraphData(number,engine):
    ''' method to retrieve station data specific to the selected on map, station number will be 
    passed as an argument into SQL statement to retrieve data specific to that station '''
    engine = get_db()
    data = []
    rows = engine.execute("SELECT available_bikes, available_bike_stands, OYB_timestamp FROM JCD_dynamic_data, WHERE number={};".format(number))
    for row in rows:
        data.append(dict(row))
    print(data)
    
def get_db():
    ''' method to get database '''
    db = getattr(g, 'onyourbikemysql', None)
    if db is None:
        db = g._database = connect_to_database()
    return db
 
if __name__ == "__main__":
    engine= connect_to_database()
    getGraphData(1,engine)  