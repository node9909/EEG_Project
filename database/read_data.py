import matplotlib.pyplot as plt
import numpy as np

data_file = 'lol.txt'
with open(data_file) as f:
    txt = f.read()

data = txt.split('\n')
data = [x.split('\t') for x in data]
p = np.zeros(shape=(70, 1651))
prev = '-'
stim = []
for i, d in enumerate(data[7:len(data)-1]):
    for k, j in enumerate(range(17, len(d)-6)):
        p[k][i-1] = float(d[j])
        if d[5] != prev:
            stim.append(i)
            prev = d[5]
print(len(p))
a = np.sum(p, 0)
plt.plot(a)

for i in stim:
    plt.axvline(i)

plt.show()