# Rail_Wreck_Data_Analysis
Rail Wreck Data Analysis: A CSV file has data for last 10 years of rail wreck in USA. Using Spark, python, MongoDB, Angular JS, HTML 5, CSS,
Flask, Restlet API, a distributed application is developed that analyse this file to get useful information.

#Following concepts are used:
1. RDD
2. Dataframe
3. Map-Reduce
4. Filter, regular expression
5. Tuple, list, Dictionary
6. MongoDB collection, documents, data insertion, data retrival, data modification.
7. AngularJS - Controller, redirection, ng-repeat, watch, Service, JSON, HTTP communication
8. Flask: Web application resource, Static file rendering

#Architecture:

1. A CSV file is read as Dataframe.
2. On this data frame, different filtering, map-reduce functions are applied to get important information.
3. These important information is stored in database (Cloud MongoDB)
4. This CSV file is read as RDD.
5. On this RDD, different filtering, map-reduce functions are applied to get important information.
6. These important information is stored in database (Cloud MongoDB)
7. A Flask-python web application is developed that define web route resources to retrieve these important information from database.
8. A single-page website is created that uses AngularJS, HTML5, CSS to connect to this web application and rendering those important information to user.

#Steps to run this in local development environment:

1. Download this project. My application location is "C:\spark-2.1.0-bin-hadoop2.7\bin\project\Rail_Wreck_Data_Analysis"
2. File "train_wreck.csv" is in data folder.
3. Run python_MongoDB.py as shown below. This .py does data analysis on "train_wreck.csv" and insert important imformation into database.

                C:\spark-2.1.0-bin-hadoop2.7\bin>spark-submit project/Rail_Wreck_Data_Analysis/python_MongoDB.py
                [Stage 2:>                                                          (0 + 2) / 2]
                Accident Yearly Data Updated. Total Time taken (3.77 Sec)
                [Stage 4:>                                                          (0 + 2) / 2]
                [Stage 4:=============================>                             (1 + 1) / 2]
                Monthly Accident Data Updated. Total Time taken (3.03 Sec)
                [Stage 6:>                                                          (0 + 2) / 2]
                [Stage 6:=============================>                             (1 + 1) / 2]
                [Stage 7:>                                                          (0 + 2) / 2]
                Date Accident Data Updated. Total Time taken (2.86 Sec)
                [Stage 11:=====================================================>(197 + 3) / 200]
                [Stage 12:>                                                        (0 + 4) / 27]
                [Stage 12:======>                                                  (3 + 4) / 27]
                [Stage 12:==============>                                          (7 + 4) / 27]
                [Stage 12:======================>                                 (11 + 4) / 27]
                [Stage 12:===============================>                        (15 + 4) / 27]
                [Stage 12:=======================================>                (19 + 4) / 27]
                [Stage 12:===============================================>        (23 + 4) / 27]
                [Stage 12:=================================================>      (24 + 3) / 27]
                [Stage 13:>                                                        (0 + 4) / 27]
                [Stage 13:======>                                                  (3 + 4) / 27]
                [Stage 13:========>                                                (4 + 4) / 27]
                [Stage 13:============>                                            (6 + 4) / 27]
                [Stage 13:==============>                                          (7 + 4) / 27]
                [Stage 13:===================>                                     (9 + 4) / 27]
                [Stage 13:====================>                                   (10 + 4) / 27]
                [Stage 13:========================>                               (12 + 4) / 27]
                [Stage 13:==========================>                             (13 + 4) / 27]
                [Stage 13:===============================>                        (15 + 4) / 27]
                [Stage 13:=================================>                      (16 + 4) / 27]
                [Stage 13:=====================================>                  (18 + 4) / 27]
                [Stage 13:=======================================>                (19 + 4) / 27]
                [Stage 13:===========================================>            (21 + 4) / 27]
                [Stage 13:=============================================>          (22 + 4) / 27]
                [Stage 13:=================================================>      (24 + 3) / 27]
                [Stage 13:===================================================>    (25 + 2) / 27]
                Each State accident count Data Updated. Total Time taken (32.21 Sec)
                Each Hourly accident count Data Updated. Total Time taken (5.15 Sec)
                Each Railroad accident count Data Updated. Total Time taken (22.33 Sec)
                 
4. MongoDB collections are created by python_MongoDB.py as shown in Data/Database_collection.jpg
5. Now run Web Application as shown below. This start the web application on http://127.0.0.1:5000

      C:\spark-2.1.0-bin-hadoop2.7\bin\project\Rail_Wreck_Data_Analysis\Server>python Web_Application.py
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
      
6. Enter http://127.0.0.1:5000 in web browser and browse rail wrecks analytical data.
