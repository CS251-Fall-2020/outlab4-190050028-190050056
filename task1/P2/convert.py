import numpy as np
data=np.genfromtxt('mumbai_data.csv',dtype=float, delimiter=',', names=True)
data["Infected"]=np.round(data["Infected"]/data["Tests"], decimals=3)
data["Tests"]=np.round(data['Tests']/20.4, decimals=3)
data=data.view(np.recarray)
print(data)
np.savetxt('transformed.csv', data, delimiter=',')