'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Lab 6 - Exponential Smoothing (Python Edition)
3rd March 2025
'''

import pandas as pd

# Function for Single Exponential Smoothing (SES)
def single_exponential_smoothing(data, alpha):
    """
    Performing Single Exponential Smoothing.
    Formula: L_t = alpha * X_t + (1 - alpha) * L_{t-1}
    """
    Lt = [data[0]]  # Initializing the first level estimate with the first actual value
    for t in range(1, len(data)):
        new_Lt = alpha * data[t] + (1 - alpha) * Lt[-1]  # Apply smoothing formula
        Lt.append(new_Lt)
    return Lt

# Function for Double Exponential Smoothing
def double_exponential_smoothing(data, alpha, beta):
    """
    Performing Double Exponential Smoothing.
    """
    Lt = [data[0]]  # First level estimate
    Bt = [data[1] - data[0]]  # First trend estimate
    smoothed_values = [Lt[0]]  # Store smoothed values
    
    for t in range(1, len(data)):
        new_Lt = alpha * data[t] + (1 - alpha) * (Lt[-1] + Bt[-1])
        new_Bt = beta * (new_Lt - Lt[-1]) + (1 - beta) * Bt[-1]
        Lt.append(new_Lt)
        Bt.append(new_Bt)
        smoothed_values.append(new_Lt)
    
    return smoothed_values, Bt

# Function for Triple Exponential Smoothing (Holt-Winters Method)
def triple_exponential_smoothing(data, alpha, beta, gamma, season_length):
    """
    Performing Triple Exponential Smoothing
    """
    Lt = [data[0]]  # First level estimate
    Bt = [data[1] - data[0]]  # First trend estimate
    St = [1] * len(data)  # Initialize seasonality to length of data to avoid mismatch
    smoothed_values = [Lt[0] * St[0]]
    
    for t in range(1, len(data)):
        if t >= season_length:
            new_St = gamma * (data[t] / Lt[-1]) + (1 - gamma) * St[t - season_length]
        else:
            new_St = St[t]
        
        new_Lt = alpha * (data[t] / new_St) + (1 - alpha) * (Lt[-1] + Bt[-1])
        new_Bt = beta * (new_Lt - Lt[-1]) + (1 - beta) * Bt[-1]
        
        Lt.append(new_Lt)
        Bt.append(new_Bt)
        St.append(new_St)
        smoothed_values.append((new_Lt + new_Bt) * new_St)
    
    # Ensuring that the output lists have the same length as input data
    return Lt[:len(data)], Bt[:len(data)], St[:len(data)]

# Main function to execute the smoothing methods
def main():
    df = pd.read_csv("Applied Time Series Analysis/AirPassengers.csv")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")  
    df = df.dropna().reset_index(drop=True)  
    
    # Defining smoothing parameters
    alpha = 0.1  # Level smoothing factor
    beta = 0.02  # Trend smoothing factor
    gamma = 0.05  # Seasonality smoothing factor
    season_length = 12  # Seasonal period
    
    # Apply Single Exponential Smoothing (SES)
    df["Lt_SES"] = single_exponential_smoothing(df["value"].tolist(), alpha)
    df["Forecast_SES"] = df["Lt_SES"].shift(1)
    df["Residual^2_SES"] = (df["value"] - df["Forecast_SES"])**2  # Computing squared residuals
    
    # Applying Double Exponential Smoothing (DES)
    df["Lt_DES"], df["Bt_DES"] = double_exponential_smoothing(df["value"].tolist(), alpha, beta)
    df["Forecast_DES"] = df["Lt_DES"].shift(1)
    df["Residual^2_DES"] = (df["value"] - df["Forecast_DES"])**2
    
    # Applying Triple Exponential Smoothing (TES)
    df["Lt_TES"], df["Bt_TES"], df["St_TES"] = triple_exponential_smoothing(df["value"].tolist(), alpha, beta, gamma, season_length)
    df["Forecast_TES"] = df["Lt_TES"].shift(1)
    df["Residual^2_TES"] = (df["value"] - df["Forecast_TES"])**2
    
    print(df.to_string())
    # df.to_csv("AirPassengers_Smoothing_Results.csv", index=False)  # Commented out saving to file
    #print("Smoothing complete. Results printed to console.")

# Main Runner
if __name__ == "__main__":
    main()

# Catastrophically Crafted By Achintya Kamath/Redzwinger #
