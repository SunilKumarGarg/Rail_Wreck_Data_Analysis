
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pymongo import MongoClient
import re
import time

sc = SparkContext()
sqlContext = SQLContext(sc)

#Create write for MongoDB
#client = MongoClient("mongodb://127.0.0.1:27017")
client = MongoClient("mongodb://sunil:sunil@ds161059.mlab.com:61059/railwreck")

text = sc.textFile("project/Rail_Wreck_Data_Analysis/Data/train_wreck.csv")
#Create the data frame
df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").load("project/Rail_Wreck_Data_Analysis/Data/train_wreck.csv")


def UpdateEachHourAccidentCount(sc, sqlContext, client, df):    
    tm = time.time()
    t = []
    for i in range(0, 24):
        t.append((i , df.filter(df['Date'].rlike("[.characters.]*"+" "+str(i)+":[.characters.]*")).count()))

    db = client.get_default_database()
    bulk = db.accident_hourly.initialize_ordered_bulk_op()
    for (Time_Hour,Count) in t:
        bulk.find({"Time_Hour": Time_Hour}).upsert().update(                
                {
                "$set": {
                    "Time_Hour":Time_Hour,
                    "Count":Count
                }
                }
            )
    bulk.execute()
    print ("Each Hourly accident count Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))

def getState(x):
    if x[0].find(", ") != -1:
        return (x[0].split(", ")[1] , x[1])
    else:
        return (x[0], x[1])



def UpdateEachStateAccidentCount(sc, sqlContext, client, df):    
    tm = time.time()
    #Get the list of State with total number of accident
    p = df.groupBy(df['City, State']).count().orderBy('count', ascending=False)

    #Map Dataframe into list of tuple
    pList = p.rdd.map(getState).reduceByKey(lambda a,b: a+b).collect()

    db = client.get_default_database()
    bulk = db.Accident_State.initialize_ordered_bulk_op()
    for (State,Count) in pList:
        bulk.find({"State": State}).upsert().update(                
                {
                "$set": {
                    "State":State,
                    "Count":Count
                }
                }
            )
    bulk.execute()
    print ("Each State accident count Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))


def UpdateEachCityAccidentCount(sc, sqlContext, client, df):    
    tm = time.time()
    #Get the list of City with total number of accident
    p = df.groupBy(df['City, State']).count().orderBy('count', ascending=False)

    #Map Dataframe into list of tuple
    pList = p.rdd.map(lambda x: (x[0], x[1])).collect()

    db = client.get_default_database()
    bulk = db.Accident_City.initialize_ordered_bulk_op()
    for (City,Count) in pList:
        bulk.find({"City": City}).upsert().update(                
                {
                "$set": {
                    "City":City,
                    "Count":Count
                }
                }
            )
    bulk.execute()
    print ("Each City accident count Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))



def UpdateEachRailroadAccidentCount(sc, sqlContext, client, df):    
    tm = time.time()
    #Get the list of Railroad with total number of accident
    p = df.groupBy(df['Railroad']).count().orderBy('count', ascending=False)

    #Map Dataframe into list of tuple
    pList = p.rdd.map(lambda x: (x[0], x[1])).collect()

    db = client.get_default_database()
    bulk = db.Accident_Railroad.initialize_ordered_bulk_op()
    for (Railroad,Count) in pList:
        bulk.find({"Railroad": Railroad}).upsert().update(                
                {
                "$set": {
                    "Railroad":Railroad,
                    "Count":Count
                }
                }
            )
    bulk.execute()
    print ("Each Railroad accident count Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))


def getYear(x):
    outputPattern = re.compile(r'\d+/\d+/(\d+)')
    if outputPattern.search(str(x)) != None:
        a = outputPattern.search(str(x)).groups()
        (f,) = a

        try:
            return int(f)
        except:
            return -1000
    else:
        return -1000


def UpdateYearlyAccidentData(sc, sqlContext, client, text):
    tm = time.time()
    yearData = text.map(lambda x: (getYear(x), 1)).reduceByKey(lambda a,b:a+b).collect()
    yearData = filter(lambda x: x[0] >= 0, yearData)
    yearData = sorted(yearData, key=lambda tup:tup[0], reverse=True)

    db = client.get_default_database()
    bulk = db.Yearly_Accident.initialize_ordered_bulk_op()
    for (year,count) in yearData:
        bulk.find({"Year": year}).upsert().update(                
                {
                "$set": {
                    "Year":year,
                    "count":count
                }
                }
            )

    bulk.execute()
    print ("Accident Yearly Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))




def getMonth(x):
    outputPattern = re.compile(r'(\d+)/\d+/\d+')
    if outputPattern.search(str(x)) != None:
        a = outputPattern.search(str(x)).groups()
        (f,) = a

        try:
            return int(f)
        except:
            return -1000
    else:
        return -1000


def UpdateMonthlyAccidentData(sc, sqlContext, client, text):
    tm = time.time()
    monthData = text.map(lambda x: (getMonth(x), 1)).reduceByKey(lambda a,b:a+b).collect()
    monthData = filter(lambda x: x[0] >= 0, monthData) 
    monthData = sorted(monthData, key=lambda tup:tup[0])
    db = client.get_default_database()
    bulk = db.Monthly_Accident.initialize_ordered_bulk_op()
    for (month,count) in monthData:
        bulk.find({"Month": month}).upsert().update(                
                {
                "$set": {
                    "Month":month,
                    "count":count
                }
                }
            )
    
    bulk.execute()
    print ("Monthly Accident Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))


def getDate(x):
    outputPattern = re.compile(r'\d+/(\d+)/\d+')
    if outputPattern.search(str(x)) != None:
        a = outputPattern.search(str(x)).groups()
        (f,) = a

        try:
            return int(f)
        except:
            return -1000
    else:
        return -1000


def UpdateDateAccidentData(sc, sqlContext, client, text):
    tm = time.time()
    dateData = text.map(lambda x: (getDate(x), 1)).reduceByKey(lambda a,b:a+b).collect()
    dateData = filter(lambda x: x[0] >= 0, dateData) 
    dateData = sorted(dateData, key=lambda tup:tup[0])
    db = client.get_default_database()

    bulk = db.Date_Accident.initialize_ordered_bulk_op()
    for (Date, count) in dateData:
        bulk.find({"Date": Date}).upsert().update(                
                {
                "$set": {
                    "Date":Date,
                    "count":count
                }
                }
            )     
    bulk.execute()       
    print ("Date Accident Data Updated. Total Time taken (%0.2f Sec)"%(time.time() - tm))

UpdateYearlyAccidentData(sc, sqlContext, client, text)
UpdateMonthlyAccidentData(sc, sqlContext, client, text)
UpdateDateAccidentData(sc, sqlContext, client, text)
UpdateEachStateAccidentCount(sc, sqlContext, client, df)
UpdateEachHourAccidentCount(sc, sqlContext, client, df)
UpdateEachRailroadAccidentCount(sc, sqlContext, client, df)
UpdateEachCityAccidentCount(sc, sqlContext, client, df)