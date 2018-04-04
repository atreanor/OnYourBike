# coding=utf-8
import MySQLdb
from time import sleep

def connector():
    global db

    while True:
        try:
            db = MySQLdb.connect(
                host="onyourbikemysql.cquggrydnjcx.eu-west-1.rds.amazonaws.com",    # your host, usually localhost
                user="Admin",         # your username
                passwd="UCD_2018",  # your password
                )
            #db = "onyourbikemysql"
            print("Connected to Database Server (AWS RDS)")
            global cur
            cur = db.cursor()
            break

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print("Connection to the AWS RDS MYSQL database has failed. Will retry in 30 seconds.")
            print("Error details are below:")
            print(e)
            sleep(30)
        except Exception:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(Exception).__name__, ex.args)
            print(message)
            print(Exception)
            exit()

def inserter_static(a, b, c, d, e, f, g, h):
    num=a
    con=b
    name=c
    add=d
    lat=e
    lon=f
    bank=g
    bonus=h
    sql = "INSERT INTO onyourbikemysql.JCD_static_data (number,\
             contract_name, name, address, lat, lng, banking, bonus) \
           VALUES ('%d', '%s', '%s', '%s', '%f', '%f', '%d', '%d' )"  % \
           (num, con, name, add, lat, lon, bank, bonus)
    try:
       cur.execute(sql)
       db.commit()
       print("Static data - SQL statement executed")
    except:
       db.rollback()


def inserter_dynamic(a, b, c, d, e, f):
    num=a
    status=b
    bikestands=c
    avail=d
    availbikes=e
    last=f  
    sql = "INSERT INTO onyourbikemysql.JCD_dynamic_data (number, \
             status, bike_stands, available_bike_stands, available_bikes, last_update) \
           VALUES ('%d', '%s', '%d', '%d', '%d', '%s' )" % \
           (num, status, bikestands, avail, availbikes, last)
    try:
        cur.execute(sql)
        db.commit()
        #print("Dynamic data - SQL statement executed")
    except:
        db.rollback()


def insert_owm_current(clouds, cod, coord_lat, coord_long, date_dt, id, humidity, pressure, temp, temp_min, temp_max, city, country, sys_id, sys_message, sunrise_dt, sunset_dt):
    sql = "INSERT INTO OpenWeatherMap.OWM_current (clouds, cod, coord_lat, coord_long," \
          "date_dt, id, humidity, pressure, temp, temp_min," \
          "temp_max, city, country, sys_id, sys_message," \
          " sunrise_dt, sunset_dt) \
        VALUES ('%d', '%d', '%f', '%f', '%s', '%d', '%d', '%d', '%d','%d','%d', '%s', '%s', '%d', '%s', '%s', '%s')" % \
        (clouds, cod, coord_lat, coord_long, date_dt, id, humidity, pressure, temp, temp_min, temp_max, city, country, sys_id, sys_message, sunrise_dt, sunset_dt)

    cur.execute(sql)
    db.commit()
    print("Open Weather Map - Current - SQL statement executed")
