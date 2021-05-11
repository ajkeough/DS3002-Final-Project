#import necessary libraries
import json
import os
import threading
from datetime import datetime
import boto3
import requests
import time
import MySQLdb
import pymysql
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import csv

#assign names to db info
DB_NAME = 'ds3002final'
HOST = 'ds3002final.cmwxmkhayq8t.us-east-1.rds.amazonaws.com'
USER = 'admin'
PASS = 'hcps6471'

#connect to the AWS RDS server using the above info
db = MySQLdb.connect(
    host=HOST,
    user=USER,
    passwd=PASS,
    db="ds3002final"

)


for i in range(60): #this will iterate the function 60 times
    def my_func(): #defines the function
        threading.Timer(60.0, my_func).start() # called every minute
        response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi") #pull from the API
        obj = response.text #store as text
        factor_num = obj['factor'] #separate the text by the variable
        pi_num = obj['pi']
        time_num = obj['time']
        time_num = datetime.strptime(time_num, '%Y-%m-%d %H:%M:%S') #refactor the variable to datetime
        cursor = db.cursor() #call the database
        cursor.execute('''
                    INSERT INTO ds3002 (factor, pi, time1)  VALUES ('%s', '%s', '%s') #execute the SQL query
    ''', (factor_num, pi_num, time_num))
        db.close()

my_func()


#print table from rds
cursor1 = db.cursor()
cursor1.execute("""SELECT * FROM ds3002""") #execute the query
results = cursor1.fetchall() #this will capture and return the entire database
print(results) #This would display it

#read the data from the SQL database into a dataframe
df = ['factor', 'pi', 'time'] #initalize a new dataframe
cursor2 = db.cursor()
cursor2.execute("""SELECT * FROM ds3002""") #execute the query
for row in cursor2:
    df.append(row) #add each row to the empty dataframe



#Data Analysis
plt.scatter(df['factor'], df['time'], color='green') #create the scatterplot to show the relationship btw 'factor' and 'time'
plt.title('Factor Vs Time', fontsize=14) #add a title
plt.xlabel('Time', fontsize=14) #add an x axis
plt.ylabel('Factor', fontsize=14) #add a y axis
plt.show() #display the plot

model = LinearRegression().fit(x, y) #run the linear model
r_sq = model.score(x, y) #determine the R squared value (higher means better)
print('coefficient of determination:', r_sq) #print the R squared value
print('slope:', model.coef_) #print the slope



