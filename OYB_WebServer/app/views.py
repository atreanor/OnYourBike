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
