import json
import os
import threading
from datetime import datetime

import boto3
import mysql.connector
import requests
import time
import os
import MySQLdb
import pymysql
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

DB_NAME = 'ds3002final'
HOST = 'ds3002final.cmwxmkhayq8t.us-east-1.rds.amazonaws.com'
USER = 'admin'
PASS = 'hcps6471'

db = MySQLdb.connect(
    host=HOST,
    user=USER,
    passwd=PASS,
    db="ds3002final"
)

#keys = ["factor", "pi", "time"]


def hello_world():
    for i in range(2):
        threading.Timer(60.0, hello_world).start() # called every minute
        response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
        obj = response.json()
        factor_num = obj['factor']
        pi_num = obj['pi']
        time_num = obj['time']
        time_num = datetime.strptime(time_num, '%Y-%m-%d %H:%M:%S')
        print(factor_num)
        print(pi_num)
        print(time_num)
        #text = json.dumps(obj, sort_keys=True)
        #text = text.replace('"', '\"').replace('\n', '\n')
        #print(text)
        cursor = db.cursor()
        cursor.execute('''
                        INSERT INTO ds3002 (factor, pi, time1)
                        VALUES ('%s', '%s', '%s')
                        ''', (factor_num, pi_num, time_num))
        db.close()

hello_world()

#Query data from database



#print table from rds
cursor1 = db.cursor()
cursor1.execute("""SELECT * FROM ds3002""")
results = cursor1.fetchall()
print(results)


def Decoder(o):
    if isinstance(o, datetime.datetime):
        return str(o)
    if isinstance(o, decimal.Decimal):
        return o.__str__()

df = []
for result in results:
    df.append(dict(zip(result)))
    output = json.dumps(df, default = Decoder)
    print(output)
    return output

#Data Analysis
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')
plt.title('Factor Vs Time', fontsize=14)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Factor', fontsize=14)
plt.grid(True)
plt.show()

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('slope:', new_model.coef_)


#print(response.json())
#def jprint(obj):
    # create a formatted string of the Python JSON object
  #  text = json.dumps(obj, sort_keys=True, indent=4)
   # print(text)

#jprint(response.json())



