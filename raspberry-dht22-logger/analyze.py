# ANALYZE SENSOR abs

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log/log.csv")
df = df.set_index('time')

# calculate dew point
df['dew_point_temperature'] = df.temperature - ((100 - df.humidity)/5.)

df['temperature_lower_dew_point'] = df.temperature < df.dew_point_temperature
if any(df.temperature_lower_dew_point):
    print("Bad! Temperature was below dew point.")
else:
    print("Good! Temperature was never below dew point.")

fig = plt.figure()
df.plot(y=['humidity', 'temperature', 'dew_point_temperature'],
        rot=45)
# ax = ax.set_xticklabels(df.time, rotation=45)
plt.tight_layout()
plt.savefig('reports/timeseries.pdf')

print('Report was written to \'reports/timeseries.pdf\'.')
