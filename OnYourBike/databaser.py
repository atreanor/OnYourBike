import MySQLdb


# def connector():
#     db = MySQLdb.connect(host="onyourbikemysql.ccljfz7hpfu8.us-west-2.rds.amazonaws.com",    # your host, usually localhost
#                      user="Admin",         # your username
#                      passwd="UCD_2018",  # your password
#                      db="OnYourBikeMySQL")        # name of the data base
#     cur = db.cursor()

# def connector():
#     db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="root",         # your username
#                      passwd="root",  # your password
#                      db="mydb")        # name of the data base
#     cur = db.cursor()
    

db = MySQLdb.connect(host="onyourbikemysql.ccljfz7hpfu8.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                 user="Admin",         # your username
                 passwd="UCD_2018",  # your password
                 db="OnYourBikeMySQL")        # name of the data base
cur = db.cursor()



def inserter_static(a, b, c, d, e, f, g, h):
    num=a
    con=b
    name=c
    add=d
    lat=e
    lon=f
    bank=g
    bonus=h
    sql = "INSERT INTO static_test (number,\
             contract_name, name, address, lat, lng, banking, bonus) \
           VALUES ('%d', '%s', '%s', '%s', '%f', '%f', '%d', '%d' )"  % \
           (num, con, name, add, lat, lon, bank, bonus) 
    try:
       cur.execute(sql)
       db.commit()
    except:
       db.rollback()
  

def inserter_dynamic(a, b, c, d, e, f):
    num=a
    status=b
    bikestands=c
    avail=d
    availbikes=e
    last=f  
    sql = "INSERT INTO dynamic_test (number, \
             status, bike_stands, available_bike_stands, available_bikes, last_update) \
           VALUES ('%d', '%s', '%d', '%d', '%d', '%s' )" % \
           (num, status, bikestands, avail, availbikes, last)   
    try:
       cur.execute(sql)
       db.commit()
       return print("inserted 1 row of parsed json data into db")
    except:
       db.rollback()


