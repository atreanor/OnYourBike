# coding=utf-8
import MySQLdb
from time import sleep
import mysql.connector

def connector():
    global cnx

    while True:
        try:
            cnx = mysql.connector.connect(user='', password='', host="")

            print("Connected to Database Server (AWS RDS)")
            global cur
            cur = cnx.cursor()
            break

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print("Connection to the AWS RDS MYSQL database has failed. Will retry in 30 seconds.")
            print("Error details are below:")
            print(e)
            sleep(30)
            pass
        except Exception as e:
            print(e)
            sleep(30)
            pass


def inserter_dynamic(a, b, c, d, e, f):
    num=a
    status=b
    bikestands=c
    avail=d
    availbikes=e
    last=f
    sql = ('INSERT INTO onyourbikemysql.JCD_dynamic_data'
           '(number, status, bike_stands, available_bike_stands, available_bikes, last_update)'
           'VALUES ("%d", "%s", "%d", "%d", "%d", "%s" )' %
           (num, status, bikestands, avail, availbikes, last))
    try:
        cur.execute(sql)
        cnx.commit()
        # print("Dynamic data - SQL statement executed")
    except:
        cnx.rollback()
        pass


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


def truncate_JCD_Flask_table():

    try:
        cur.execute('TRUNCATE TABLE onyourbikemysql.JCD_flask')
        cnx.commit()
        print("Table truncated")

    except Exception as e:
        # logf.write(str(e))
        cnx.rollback()
        print("Exception - Truncate JCD Flask table: ", e)
        pass

def insert_jdc_flask(number, name, contract_name, status, bike_stands, available_bike_stands, available_bikes, last_update, address, lat, lng, banking, bonus):
    sql_flask = ('INSERT INTO onyourbikemysql.JCD_flask'
                   '(number, name, contract_name, status, bike_stands, available_bike_stands,available_bikes, last_update, address, lat, lng, banking, bonus)'
                   'VALUES ("%d", "%s", "%s", "%s", "%d",'
                   '"%d", "%s", "%s", "%s",'
                   '"%f", "%f", "%d", "%d")' %
                   (number, name, contract_name, status, bike_stands, available_bike_stands, available_bikes, last_update, address, lat, lng, banking, bonus))

    try:
        cur.execute(sql_flask)
        cnx.commit()
        #print("insert_JCD_flask - SQL statement executed")

    except Exception as e:
        # logf.write(str(e))
        cnx.rollback()
        print("Exception - Insert_JCD_flask: ", e)
        pass

