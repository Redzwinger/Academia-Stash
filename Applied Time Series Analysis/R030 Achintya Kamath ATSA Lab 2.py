'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Lab 2 - More Time Series Basics
13th January 2025
'''

from tkinter import font
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tseries.offsets import YearEnd
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa. stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
from pandas.plotting import lag_plot
sns.set_style('darkgrid')
sns.set_context('notebook', font_scale=1)
sns.set_palette('viridis')

# Reading the raw data and making a copy to make suitable changes
rawCSV = pd.read_csv("Applied Time Series Analysis/AirPassengers.csv")
df_copy = rawCSV.copy()

# Getting the data type info of the data
print("Original Data:\n")
print(df_copy.info())
print("\nHead:\n", df_copy.head())

# Changing date column format to standard
df_copy['date'] = pd.to_datetime(df_copy['date'], yearfirst=True)
print("\n\nChanged Copy:\n")
print(df_copy.info())
print("\nHead:\n", df_copy.head())

# Doing train-test split
size = int(len(df_copy)*0.8)
df_train, df_test = df_copy.iloc[:size], df_copy.iloc[size:]

print("\nTrain Size: ", df_train.size)
print("Test Size: ", df_test.size)

# Plotting a simple time plot (line plot)
plt.title("Time Plot For AirPassengers.csv")
sns.lineplot(x='date', y='value', data=df_copy)
plt.show()

df_copy['month'] = df_copy['date'].dt.month
df_copy['year'] = df_copy['date'].dt.year

print("\nHead:\n", df_copy.head())
sns.lineplot(x='month',y='value', hue='year', data=df_copy)
plt.show()

# Checking for Trends and Seasonality using seasonal decompose
s_dec_multiplicative = seasonal_decompose(df_train.value, model='multiplicative', period=1)
s_dec_multiplicative.plot()
plt.show()

laggy = [1,2,3,6,12]

plt.figure(figsize=(10, 8))
for i, lag in enumerate(laggy, 1):
    plt.subplot(3, 2, i)
    lag_plot(df_copy['value'], lag=lag)
    plt.title(f'Lag {lag}')
plt.tight_layout()
plt.show()

for lag in laggy:
    sgt.plot_acf(df_train.value, lags=lag, zero=False)
    plt.title(f"Autocorrelation for Lag {lag}")
    plt.show()

    sgt.plot_pacf(df_train.value, lags=lag, zero=False, method=('ols') )
    plt.title(f"Partial Autocorrelation for Lag {lag}")
    plt.show()

# Curiously Crafted By Achintya Kamath/Redzwinger #