import argparse
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser()
parser.add_argument('--data', required=True)
args=parser.parse_args()
df=pd.read_csv(args.data)
df['epsalg']=df['algorithm']
df.loc[df['algorithm']=='epsilon-greedy','epsalg']+=' with epsilon='+df.loc[df['algorithm']=='epsilon-greedy','epsilon'].astype(str)
grp=df.groupby(['instance','epsalg','horizon']).apply(lambda x: x.sample(50).mean()).unstack([0,1])['REG']
for fil in grp.columns.levels[0]:
	plt.clf()
	plt.loglog(grp[fil])
	plt.legend(grp[fil].columns)
	plt.title('Instance {} - both axes in log scale'.format(fil[-5]))
	plt.xlabel('horizon')
	plt.ylabel('Regret')
	plt.savefig('instance{}.png'.format(fil[-5]))
