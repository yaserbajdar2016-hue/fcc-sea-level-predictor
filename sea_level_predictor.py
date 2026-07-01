import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = np.arange(df["Year"].min(), 2051)
    y = result.slope * x + result.intercept
    plt.plot(x, y, "r")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    result2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x2 = np.arange(2000, 2051)
    y2 = result2.slope * x2 + result2.intercept
    plt.plot(x2, y2, "g")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
