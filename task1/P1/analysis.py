import numpy as np
data = np.genfromtxt("mumbai_data.csv", dtype=int, delimiter=',', skip_header=0)
mean=np.mean(data[1:], axis=0)
stddev=np.std(data[1:], axis=0)
fields=np.genfromtxt("mumbai_data.csv", dtype=str, delimiter=',')[0]
ans=np.array([["Field", "Mean", "Std.Dev."]])
for i in range(len(mean)-1):
    row=[fields[i+1], round(mean[i+1], 3), round(stddev[i+1], 3)]
    ans=np.vstack((ans, row))
# ans=np.ans(ans)
# print(ans)
for i in ans:
    print(*i)
s = [[str(e) for e in row] for row in ans]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print ('\n'.join(table))