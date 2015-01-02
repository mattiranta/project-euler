import matplotlib.pyplot as plt
import numpy as np

data_python        = np.genfromtxt('python.csv',        delimiter=';', skip_header=1, names=['problem', 'time']) 
data_fsharp        = np.genfromtxt('fsharp.csv',        delimiter=';', skip_header=1, names=['problem', 'time'])
data_fsharp_bigint = np.genfromtxt('fsharp-bigint.csv', delimiter=';', skip_header=1, names=['problem', 'time'])
data_julia         = np.genfromtxt('julia.csv',         delimiter=';', skip_header=1, names=['problem', 'time'])

plt.plot(data_python['problem'], data_python['time'], 'o-')
plt.plot(data_fsharp['problem'], data_fsharp['time'], 'o-')
plt.plot(data_fsharp_bigint['problem'], data_fsharp_bigint['time'], 'o-', zorder=1)
plt.plot(data_julia['problem'], data_julia['time'], 'o-')

plt.title ('Project Euler performance comparison')
plt.xlabel('Problem')
plt.ylabel('Time (ms)')
plt.legend(['Python', 'F#', 'F# (bigint)', 'Julia'], loc='top right')
plt.xticks(range(1,len(data_python)))
#plt.yscale('log')
plt.ylim(0.0, 0.05);
plt.show()
#plt.savefig('plot.png')