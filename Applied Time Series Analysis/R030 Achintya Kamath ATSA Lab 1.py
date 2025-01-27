'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Lab 1 - Time Series Basics
6th January 2025
'''

from tkinter import font
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa. stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
sns.set_style('darkgrid')
sns.set_context('notebook', font_scale=1)
sns.set_palette('plasma')

# Reading the raw data and making a copy to make suitable changes
rawCSV = pd.read_csv("Applied Time Series Analysis/Index2018.csv")
df_copy = rawCSV.copy()

# Getting the data type info of the data
print("Original Data:\n")
print(df_copy.info())

# Changing date column format to standard
df_copy['date'] = pd.to_datetime(df_copy['date'], dayfirst=True)
print("\n\nChanged Copy:\n")
print(df_copy.info())

# Removing all other columns aside from spx or now market_data and date
df_copy['market_data'] = df_copy['spx']
#print(df_copy.info())

del df_copy['spx']
del df_copy['dax']
del df_copy['ftse']
del df_copy['nikkei']

print("\n\nFurther Changes Of Copy:\n")
print(df_copy.info(), "\n\n Head:\n", df_copy.head())

# Doing train-test split
size = int(len(df_copy)*0.8)
df_train, df_test = df_copy.iloc[:size], df_copy.iloc[size:]

print("\nTrain Size: ", df_train.size)
print("Test Size: ", df_test.size)

# Checking for Seasonality using seasonal decompose
s_dec_multiplicative = seasonal_decompose(df_train.market_data, model='multiplicative', period=1)
s_dec_multiplicative.plot()
plt.show()

# Autocorrelation / ACF - Plotting the graph
sgt.plot_acf(df_train.market_data, lags=40, zero=False)
plt.title("Autocorrelation of S&P Prices", size = 24)
plt.show()

# Partial Autocorrelation
sgt.plot_pacf(df_train.market_data, lags=40, zero=False, method=('ols') )
plt.title("PACF of S&P Prices", size = 24)
plt.show()

# Generating White Noise
wn= np.random.normal(loc=df_train.market_data.mean(),scale=df_train.market_data.std(),size=len(df_train))
df_train['wn']=wn
df_train.describe()

# Plotting the above generated White Noise
df_train.wn.plot(figsize=(20,5))
plt.title("White Noise Time Series", size = 24)
plt.show()

# Finally, plotting the train set data
df_train.market_data.plot(figsize=(20,5))
plt.title("S&P Prices", size = 24)
plt.ylim(0,2300 )
plt.show()

# Curiously Crafted By Achintya Kamath/Redzwinger #