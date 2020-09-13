import numpy as np
np.set_printoptions(suppress=True)

unlock=np.genfromtxt('./mumbai_unlock.csv', dtype=float, delimiter=",", skip_header=1)
lock=np.genfromtxt('./mumbai_data.csv', dtype=float, delimiter=",", skip_header=1)
infected_lock= lock[:, 2]
rate_lock=np.round(lock[:,2]/lock[:,1], decimals=3)
infected_unlock=unlock[:,2]
rate_unlock=np.round(unlock[:,2]/unlock[:,1], decimals=3)
data=np.array([infected_unlock, infected_lock, rate_lock, rate_unlock]).transpose().astype(np.str)
fields=np.array(['Day','Infected(Unlock)','Infected(Lock)','Positivity Rate(Lock)','Positivity Rate(UnLock)'])
days=np.genfromtxt('./mumbai_data.csv',dtype=str, delimiter=',', skip_header=1).transpose()[0]
data=np.char.rstrip(data, chars='.0')
data=np.insert(data, 0, days, axis=1)
data=np.insert(data, 0, fields, 0)
np.savetxt('info_combine.csv', data, fmt='%s',delimiter=',')