import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
from scipy import stats
import math

df=pd.read_csv('case_time_series.csv')
id=df.set_index('Date').index.get_loc('14 April ')
df=df['Total Deceased'][id:].astype(int)
days=range(1,df.size)
fwd=df[1:]
bwd=df[:-1]
fwd.index=bwd.index=days
h=fwd/bwd
slope, intercept, r_value, p_value, std_err=stats.linregress(days, h)
plt.xlabel('Day no. (since 01 April)')
plt.ylabel('H(t)')
plt.title("A plot of Levitt's metric against days")
plt.scatter(days, h)
plt.plot(days*slope+intercept)
plt.savefig('covid.png')
print(math.ceil((1-intercept)/slope))
