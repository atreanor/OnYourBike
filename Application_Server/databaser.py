# coding=utf-8
import MySQLdb
from time import sleep
import mysql.connector

def connector():
    global cnx

    while True:
        try:
            cnx = mysql.connector.connect(user='Admin', password='UCD_2018', host="onyourbikemysql.cquggrydnjcx.eu-west-1.rds.amazonaws.com")
            '''db = MySQLdb.connect(
                host="onyourbikemysql.cquggrydnjcx.eu-west-1.rds.amazonaws.com",    # your host, usually localhost
                user="Admin",         # your username
                passwd="UCD_2018",  # your password
                )'''
            #db = "onyourbikemysql"
            print("Connected to Database Server (AWS RDS)")
            global cur
            cur = cnx.cursor()
            break

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print("Connection to the AWS RDS MYSQL database has failed. Will retry in 30 seconds.")
            print("Error details are below:")
            print(e)
            sleep(30)
        except Exception as e:
            print(e)
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
        cnx.commit()
        print("Static data - SQL statement executed")
    except:
        cnx.rollback()


def inserter_dynamic(a, b, c, d, e, f):
    num=a
    status=b
    bikestands=c
    avail=d
    availbikes=e
    last=f
    sql = ("INSERT INTO onyourbikemysql.JCD_dynamic_data"
           "(number, status, bike_stands, available_bike_stands, available_bikes, last_update)"
           "VALUES ('%d', '%s', '%d', '%d', '%d', '%s' )" %
           (num, status, bikestands, avail, availbikes, last))
    try:
        cur.execute(sql)
        cnx.commit()
        # print("Dynamic data - SQL statement executed")
    except:
        cnx.rollback()


def insert_owm_current(clouds, name, visibility, w_d_main, w_d_id, w_d_icon, w_description, coord_lat, coord_long, owm_dt, id, humidity, pressure, temp, temp_min, temp_max, city, sys_country, sys_id, sys_message, sys_sunrise_dt, sys_sunset_dt, cod):

    sql_weather = ("INSERT INTO OpenWeatherMap.OWM_current"
                   "(clouds, name, visibility, w_d_main, w_d_id, w_d_icon, w_description, coord_lat, coord_long, owm_dt, id, humidity, pressure, temp, temp_min, temp_max, city, sys_country, sys_id, sys_message, sys_sunrise_dt, sys_sunset_dt, cod)"
                   "VALUES ('%d', '%s', '%s', '%s', '%s',"
                   "'%s', '%s', '%f', '%f', '%s',"
                   "'%s', '%s', '%s', '%s', '%s',"
                   "'%s', '%s', '%s', '%f', '%s',"
                   "'%s', '%s', '%s')" %
                   (clouds, name, visibility, w_d_main, w_d_id,
                    w_d_icon, w_description, coord_lat, coord_long, owm_dt,
                    id, humidity, pressure, temp, temp_min,
                    temp_max, city, sys_country, sys_id, sys_message,
                    sys_sunrise_dt, sys_sunset_dt, cod))

    try:
        cur.execute(sql_weather)

        cnx.commit()
        print("Dynamic data - SQL statement executed")

    except Exception as e:
        # logf.write(str(e))
        cnx.rollback()
        print("Exception - Insert_owm__current: ", e)
    pass


