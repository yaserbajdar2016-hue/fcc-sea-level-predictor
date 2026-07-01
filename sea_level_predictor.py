import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create figure and axis
    fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = list(range(df['Year'].min(), 2051))
    y1 = [res.slope * x + res.intercept for x in x1]
    ax.plot(x1, y1)

    # Second line of best fit (from year 2000)
    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = list(range(2000, 2051))
    y2 = [res2.slope * x + res2.intercept for x in x2]
    ax.plot(x2, y2)

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save figure
    plt.savefig("sea_level_plot.png")

    return ax
