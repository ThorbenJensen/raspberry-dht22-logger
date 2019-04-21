"""Visualize logged data."""

import pandas as pd
import matplotlib.pyplot as plt

# %% Load data
df = pd.read_csv('log/log.csv', parse_dates=['time']) \
    .set_index(keys='time')

# %% Line plot

df.plot.line(style='.', subplots=True)
plt.savefig('plots/time_series.png')   # save the figure to file
plt.close()
