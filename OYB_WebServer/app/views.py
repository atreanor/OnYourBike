from flask import render_template
from flask import jsonify
from app import app
from app import model
import json
import simplejson


@app.route('/')
def index():
    a = {}
    a['title'] = 'OnYourBike with DublinBikes'
    jsonify(a=a)
    return render_template("index.html", **a)

@app.route('/getjson')
def getjson():
    c = {}
    c['name'] = 'Thomas Street', 'James Street', 'Stephens Green', 'Christchurch Place', 'Excise Walk', 'Fownes Street Upper', 'Custom House'  
    c['number']= 1,2,3,4,5,6,7
    c['available_bikes'] = '20','26','29','0','15','21','11'
    c['free_stands'] = '13','14','15', '0','10','16','8'
    c['lat'] = 53.3496, 53.3535, 53.336, 53.3434, 53.3478, 53.3446, 53.3483
    c['lng'] = -6.2782, -6.26531,-6.26298, -6.27012, -6.24424, -6.26337, -6.25466
    return jsonify(c=c)


@app.route('/getweather')
def getweather():
    w = {}
    w['description'] = {"main":"clouds","description":"overcast clouds","icon":"04n"} 
    w['temp']= 12
    w['tempmin'] = 7
    return jsonify(w=w)


