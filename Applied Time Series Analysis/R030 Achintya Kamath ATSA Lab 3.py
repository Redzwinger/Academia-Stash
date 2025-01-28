'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Lab 3 - Trends and Seasonality
27th January 2025
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
sns.set_context('notebook', font_scale=1)
sns.set_palette('plasma')

# Reading the raw data and making a copy to make suitable changes
Exceldata = pd.read_excel("Applied Time Series Analysis/Python Stuff.xlsx")

#print(Exceldata.head(15))

data = Exceldata.copy()
data['Month'] = pd.to_datetime(data['Date']).dt.month
print("\n Original Data: \n", data.head(15), "\n")

data['Lag1-12MA'] = data['value'].rolling(window=12).mean()
data['Lag1-12MA'] = data['Lag1-12MA'].shift(-6)

print("Adding 12 Month Moving Average: \n", data.head(15), "\n")

data['Lag2-12MA'] = data['Lag1-12MA'].copy().shift(1)

print("Adding A Second (Lagged) 12 Month Moving Average: \n", data.head(15), "\n")

data['12MA-Trend'] = (data['Lag1-12MA']+data['Lag2-12MA'])/2

print("Observing Trends By Calculating Average of Averages: \n", data.head(15), "\n")

data['12MA-Detrend'] = data['value']-data['12MA-Trend']

print("Detrending The Averages By Removing Value Points: \n", data.head(15), "\n")

data['Seasonality'] = (data['12MA-Detrend'].groupby(data['Month'], dropna=True)).aggregate("mean")

ListBoi = data['Seasonality']
ListBoi = ListBoi[1:13]
#print(ListBoi)

data['TiledSeasonality'] = np.tile(ListBoi, int(len(data)/len(ListBoi))) #BAD BAD BAD BAD BAD BAD BAD BAD change later

print("Seasonality Maybe: \n", data.head(25), "\n")
