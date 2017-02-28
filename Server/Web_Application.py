from flask import Flask,  render_template
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient("mongodb://sunil:sunil@ds161059.mlab.com:61059/railwreck")
db = client.get_default_database()


@app.route("/")
def index():
   return render_template("index.htm")

@app.route('/RailAccident/Hour')
def Accident_Hour():
    try:
        pp = db.accident_hourly.find({},{"_id":0})                
        return dumps(list(pp))
    except:
        return "error"


@app.route('/RailAccident/State')
def Accident_State():
    try:
        pp = db.Accident_State.find({},{"_id":0})
        return dumps(list(pp))
    except:
        return "error"

@app.route('/RailAccident/City')
def Accident_City():
    try:
        pp = db.Accident_City.find({},{"_id":0})
        return dumps(list(pp))
    except:
        return "error"

@app.route('/RailAccident/Railroad')
def Accident_Railroad():
    try:
        pp = db.Accident_Railroad.find({},{"_id":0})
        return dumps(list(pp))
    except:
        return "error"

@app.route('/RailAccident/Year')
def Accident_Year():
    try:
        pp = db.Yearly_Accident.find({},{"_id":0})
        return dumps(list(pp))
    except:
        return "error"

@app.route('/RailAccident/Month')
def Accident_Month():
    try:
        pp = db.Monthly_Accident.find({},{"_id":0})
        return dumps(list(pp))
    except:
        return "error"

@app.route('/RailAccident/Date')
def Accident_Date():
    try:
        pp = db.Date_Accident.find({},{"_id":0})
        return dumps(list(pp))
    except:
        return "error"

if __name__ == '__main__':
   app.run()