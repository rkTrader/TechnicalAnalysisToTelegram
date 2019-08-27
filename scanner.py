import os
import pandas as pd
import numpy as np
import talib as ta
from datetime import datetime

os.chdir("<<<YOUR PATH>>>>>")
from dbConn import createConnection # My custom MySQL connection function

conn = createConnection()
cursor = conn.cursor()

getScrips = "select symbol from highvaluescrips" ### Get a list of scrips
scrips = pd.read_sql(getScrips, con=conn)

# Pattern Checks
for scrip in scrips['symbol']:
    print("__________________________________________________")
    print(scrip)
    getQuery = "<<<<<QUERY TO GET DATA FOR LAST FEW DAYS>>>>>>>>>" % (scrip,)
    data = pd.read_sql(getQuery, con=conn)
    data=data.sort_index(axis=0, ascending=False)
    
    hammerCheck = ta.CDLHAMMER(data['Open'],data['High'],data['Low'],data['Close'])
    shootingStarCheck = ta.CDLSHOOTINGSTAR(data['Open'],data['High'],data['Low'],data['Close'])
    invertedHammerCheck = ta.CDLINVERTEDHAMMER(data['Open'],data['High'],data['Low'],data['Close'])
    hangingManCheck = ta.CDLHANGINGMAN(data['Open'],data['High'],data['Low'],data['Close'])
    engulfingCheck = ta.CDLENGULFING(data['Open'],data['High'],data['Low'],data['Close'])
    darkCloudCheck = ta.CDLDARKCLOUDCOVER(data['Open'],data['High'],data['Low'],data['Close'])
    piercingPatternCheck = ta.CDLPIERCING(data['Open'],data['High'],data['Low'],data['Close'])
    
    # Add Volume confirmation
    data['SMA20Volume']=ta.SMA(data.Volume,20)
    
    
    if (data['Volume'][0] >= data['SMA20Volume'][0]) :
        if hammerCheck[0] != 0:
            print("hammer formation")
        if shootingStarCheck[0] != 0:
            print("shooting star formation")
        if invertedHammerCheck[0] != 0:
            print("Inverted hammer formation")
        if hangingManCheck[0] != 0:
            print("Hanging man formation")
        if engulfingCheck[0] != 0:
            print("Engulfing formation")
        if darkCloudCheck[0] != 0:
            print("Dark cloud formation")
        if piercingPatternCheck[0] != 0:
            print("Piercing Pattern formation")
			
conn.close()