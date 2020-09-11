import numpy as np
np.set_printoptions(suppress=True)
data=np.genfromtxt('../P1/mumbai_data.csv',dtype=float, delimiter=',', skip_header=1)
data=data.transpose()
_2=np.round(data[2]/data[1], decimals=3)
_1=np.round(data[1]/20.4)
data[2]=_2
data[1]=_1
data=data.transpose()
data=np.delete(data, 0, 1)
data=data.astype(np.str)
data=np.char.rstrip(data, chars='.0')
fields=np.array(['Day','Tests per million', 'Test positivity rate', 'Recovered', 'Deceased' ])
days=np.genfromtxt('./mumbai_data.csv',dtype=str, delimiter=',', skip_header=1).transpose()[0]
data=np.insert(data, 0, days, axis=1)
data=np.insert(data, 0, fields, 0)
np.savetxt('transformed.csv', data, fmt='%s',delimiter=',')