# import necessary libraries
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

#define the function
def my_func():
    response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi") #pull from api
    obj = response.text #save as text
    with open('output.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',') #write data to specified CSV file
        for row in obj.split('\n'): #read the data into the file by splitting the text
            split_commas = row.split(',')
            factor_num = split_commas[0]
            factor_num = factor_num[10:]
            pi_num = split_commas[1]
            pi_num = pi_num[5:]
            time_num = split_commas[2]
            time_num = time_num[8:-2]
            writer.writerow((factor_num, pi_num, time_num))
    f.close()

#run the function once every 60 seconds until 60 minutes have elapsed
for i in range(0, 3600, 60):
    threading.Timer(i, my_func).start()