from flask import render_template
from app import app
from app import model

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Tom'
    returnDict['title'] = 'Home'
    #contract = "Dublin"
    #apikey = "e8823ad03eaa6b4b5b80b84203e56c1740394008" # API key for JC Decaux
    #returnDict['owm'] = owm.owm_scrape()
    return render_template("index.html", **returnDict)
    

@app.route('/map')
def map():
    returnDict = {}
    returnDict['name'] = 'Thomas Street'
    returnDict['available_bikes'] = '20'
    returnDict['free_stands'] = '13'
    #returnDict['title'] = 'Home'
    return render_template("friday.html", **returnDict)


@app.route('/map2')
def map2():
    returnDict = {}
    #returnDict['title'] = 'Home'
    return render_template("friday2.html", **returnDict)

