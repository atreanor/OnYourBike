import MySQLdb

def main():
    x = Databaser()
    x.db.close()


class Databaser:
    
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="root",  # your password
                         db="mydb")        # name of the data base
        self.cur = self.db.cursor()
        
    def createstatictable(self):
        self.cur.execute("DROP TABLE IF EXISTS static")
        # Create table as per requirement
        self.sql = """CREATE TABLE static (number INT,
        contract_name CHAR(20),
        name CHAR(20),
        address CHAR(20),
        lat INT,
        lon INT,
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
        # Prepare SQL query to INSERT a record into the database.
        self.sql = "INSERT INTO static (number,\
                 contract_name, name, address, lat, lon, banking, bonus) \
               VALUES ('%d', '%s', '%s', '%s', '%d', '%d', '%s', '%s' )"  % \
               (self.num, self.con, self.name, self.add, self.lat, self.lon, self.bank, self.bonus) 
        try:
           # Execute the SQL command
           self.cur.execute(self.sql)
           # Commit your changes in the database
           self.db.commit()
        except:
           # Rollback in case there is any error
           self.db.rollback()
        
        
    def createdynamictable(self):
        self.cur.execute("DROP TABLE IF EXISTS dynamic1")
        # Create table as per requirement
        self.sql = """CREATE TABLE dynamic1 (
        number INT NOT NULL,
        status CHAR(10),
        bike_stands INT,
        available_bike_stands INT,
        available_bikes INT,
        last_update TIMESTAMP
        )"""
        self.cur.execute(self.sql) 
        
    def inserter_dynamic(self, a, b, c, d, e, f):
        self.num=a
        self.status=b
        self.bikestands=c
        self.avail=d
        self.availbikes=e
        self.last=f
        # Prepare SQL query to INSERT a record into the database.
        self.sql = """INSERT INTO dynamic1 (number,
                 status, bike_stands, available_bike_stands, available_bikes, last_update) \
               VALUES ('%d', '%s', '%d', '%d', '%d', '%s' )""" % \
               (self.num, self.status, self.bikestands, self.avail, self.availbikes, self.last)
        try:
           # Execute the SQL command
           self.cur.execute(self.sql)
           # Commit your changes in the database
           self.db.commit()
        except:
           # Rollback in case there is any error
           self.db.rollback()
                              
main()
