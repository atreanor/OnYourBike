import MySQLdb

def main():
    x = databaser()
    #x.printfirstcolumn()
    #x.getversion()
    #x.selecter()
    
    x.createtable()
    #x.inserter_hardcoded()
    x.inserter_dynamic(42, 'Dublin', 'Dalkey', 'Myroad', 55.5, 55.5, 'False', 'False')
    x.db.close()


class databaser:
    
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="root",  # your password
                         db="mydb")        # name of the data base
        self.cur = self.db.cursor()
    
    def selecter(self):
        # Use all the SQL you like
        self.cur.execute("SELECT firstname, lastname FROM studentscourses")
        # print all the first cell of all the rows
        for row in self.cur.fetchall():
            print (row[0], row[1])
            
            
            
    def printfirstcolumn(self):
        # Use all the SQL you like
        self.cur.execute("SELECT * FROM studentscourses")
        # print all the first cell of all the rows
        for row in self.cur.fetchall():
            print (row[0])
        
    def getversion(self):
        # Use all the SQL you like
        self.cur.execute("SELECT VERSION()")
        self.data = self.cur.fetchone()
        print(self.data)
    
    def createtable(self):
        self.cur.execute("DROP TABLE IF EXISTS BIKETEST")
        # Create table as per requirement
        self.sql = """CREATE TABLE BIKETEST (
        NUMBER INT NOT NULL,
        CONTRACT CHAR(20),
        NAME CHAR(20),
        ADDRESS CHAR(20),
        LAT FLOAT,
        LON FLOAT,
        BANKING CHAR(20),
        BONUS CHAR(20)
        )"""
        self.cur.execute(self.sql)
         
        
         
        
    def inserter_hardcoded(self): 
        # Prepare SQL query to INSERT a record into the database.
        self.sql = """INSERT INTO TESTER(NUMBER,
                 CONTRACT, NAME, LAT, LON, BANKING, BONUS)
                 VALUES ('Sheena', 'Davitt', 20, 'F', 2000)"""
        try:
           # Execute the SQL command
           self.cur.execute(self.sql)
           # Commit your changes in the database
           self.db.commit()
        except:
           # Rollback in case there is any error
           self.db.rollback()

    def inserter_dynamic(self, a, b, c, d, e, f, g, h):
        self.num=a
        self.con=b
        self.name=c
        self.add=d
        self.lat=e
        self.lon=f
        self.bank=g
        self.bonus=h
        # Prepare SQL query to INSERT a record into the database.
        self.sql = """INSERT INTO BIKETEST(NUMBER,
                 CONTRACT, NAME, ADDRESS, LAT, LON, BANKING, BONUS) \
               VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
               (self.num, self.con, self.name, self.name, self.lat, self.lon, self.bank, self.bonus)"""
        try:
           # Execute the SQL command
           self.cur.execute(self.sql)
           # Commit your changes in the database
           self.db.commit()
        except:
           # Rollback in case there is any error
           self.db.rollback()



        
main()







