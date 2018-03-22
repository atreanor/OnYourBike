import MySQLdb
import scraper
import time
import datetime

def main():
    x = Databaser()
    x.db.close()


class Databaser:
    
    def __init__(self):
        self.db = MySQLdb.connect(host="onyourbikemysql.ccljfz7hpfu8.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                         user="Admin",         # your username
                         passwd="UCD_2018",  # your password
                         db="OnYourBikeMySQL")        # name of the data base
        self.cur = self.db.cursor()
        
    def createstatictable(self):
        self.cur.execute("DROP TABLE IF EXISTS static")
        self.sql = """CREATE TABLE static (number INT,
        contract_name CHAR(20),
        name CHAR(20),
        address CHAR(20),
        lat FLOAT,
        lng FLOAT,
        banking CHAR(20),
        bonus CHAR(20)        )"""
        self.cur.execute(self.sql) 

        
    def inserter_static(self, a, b, c, d, e, f, g, h):
        self.num=a
        self.con=b
        self.name=c
        self.add=d
        self.lat=e
        self.lon=f
        self.bank=g
        self.bonus=h
        self.sql = "INSERT INTO static_test (number,\
                 contract_name, name, address, lat, lng, banking, bonus) \
               VALUES ('%d', '%s', '%s', '%s', '%f', '%f', '%d', '%d' )"  % \
               (self.num, self.con, self.name, self.add, self.lat, self.lon, self.bank, self.bonus) 
        try:
           self.cur.execute(self.sql)
           self.db.commit()
        except:
           self.db.rollback()
      
    
        
    def createdynamictable(self):
        self.cur.execute("DROP TABLE IF EXISTS dynamic")
        self.sql = """CREATE TABLE dynamic (
        number INT NOT NULL,
        status CHAR(10),
        bike_stands INT,
        available_bike_stands INT,
        available_bikes INT,
        last_update DATETIME
        )"""
        self.cur.execute(self.sql) 
        
    def inserter_dynamic(self, a, b, c, d, e, f):
        self.num=a
        self.status=b
        self.bikestands=c
        self.avail=d
        self.availbikes=e
        self.last=f  
        self.sql = "INSERT INTO dynamic_test (number, \
                 status, bike_stands, available_bike_stands, available_bikes, last_update) \
               VALUES ('%d', '%s', '%d', '%d', '%d', '%s' )" % \
               (self.num, self.status, self.bikestands, self.avail, self.availbikes, self.last)   
        try:
           self.cur.execute(self.sql)
           self.db.commit()
           return print("inserted into db")
        except:
           self.db.rollback()
                              
main()


