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
colors = sns.color_palette("plasma", n_colors=10)

# Reading the raw data and making a copy to make suitable changes
Exceldata = pd.read_excel("Applied Time Series Analysis/Python Stuff.xlsx")

#print(Exceldata.head(15))

data = Exceldata.copy()
data['Date'] = pd.to_datetime(data['Date'])
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

data['SingularSeasonality'] = (data['12MA-Detrend'].groupby(data['Month'], dropna=True)).aggregate("mean")

ListBoi = data['SingularSeasonality']
ListBoi = ListBoi[1:13]
#print(ListBoi)

data['TiledSeasonality'] = np.tile(ListBoi, int(len(data)/len(ListBoi)))

data['Seasonality'] = data['TiledSeasonality'].shift(6)

data.drop(['SingularSeasonality', 'TiledSeasonality'], axis=1, inplace=True)

print("Seasonality: \n", data.head(25), "\n")

data['Residue'] = data['value']-data['12MA-Trend']-data['Seasonality']

print("Residue: \n", data.head(25), "\n")

just_data = data[['Date', 'value']].dropna()
lag_data = data[['Date', 'Lag1-12MA', 'Lag2-12MA']].dropna()
trend_data = data[['Date', '12MA-Trend', '12MA-Detrend']].dropna()
season_data = data[['Date', 'Seasonality']].dropna()
residue_data = data[['Date', 'Residue']].dropna()

plt.plot(just_data['Date'], just_data['value'], label='Value', color=colors[0])
plt.title('Original Data')
plt.legend()
plt.show()

plt.plot(lag_data['Date'], lag_data['Lag1-12MA'], label='Lag 1', color=colors[1])
plt.title('12 Month Average (Lag 1)')
plt.legend()
plt.plot(lag_data['Date'], lag_data['Lag2-12MA'], label='Lag 2', color=colors[2])
plt.title('12 Month Average (Lag 2)')
plt.legend()
plt.show()

plt.plot(trend_data['Date'], trend_data['12MA-Trend'], label='Trend', color=colors[3])
plt.title('Trend Component (12 Month Average)')
plt.legend()
plt.plot(trend_data['Date'], trend_data['12MA-Detrend'], label='DeTrend', color=colors[4])
plt.title('DeTrend Component (12 Month Average)')
plt.legend()
plt.show()

plt.plot(season_data['Date'], season_data['Seasonality'], label='Seasonality', color=colors[5])
plt.title('Seasonality Component (12 Month Average)')
plt.legend()
plt.show()

plt.plot(residue_data['Date'], residue_data['Residue'], label='Residue', color=colors[6])
plt.title('Residue (Value-Trend-Seasonality)')
plt.legend()
plt.show()

# Catastrophically Crafted By Achintya Kamath/Redzwinger #