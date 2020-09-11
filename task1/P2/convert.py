import numpy as np
np.set_printoptions(suppress=True)
data=np.genfromtxt('../P1/mumbai_data.csv',dtype=float, delimiter=',', skip_header=1)
for i in range(len(data)):
    data[i][2]=np.round(data[i][2]/data[i][1], decimals=3)
    data[i][1]=np.round(data[i][1]/20.4, decimals=3)
data=np.delete(data, 0, 1)
data=data.astype(np.str)
fields=np.array(['Day','Tests per million', 'Test positivity rate', 'Recovered', 'Deceased' ])
days=np.array(['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday'])
data=np.insert(data, 0, days, axis=1)
data=np.insert(data, 0, fields, 0)
np.savetxt('transformed.csv', data, fmt='%s',delimiter=',')