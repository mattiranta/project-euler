#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

data_python        = np.genfromtxt('python.csv',        delimiter=';', skip_header=1, names=['problem', 'time']) 
data_fsharp        = np.genfromtxt('fsharp.csv',        delimiter=';', skip_header=1, names=['problem', 'time'])
#data_fsharp_bigint = np.genfromtxt('fsharp-bigint.csv', delimiter=';', skip_header=1, names=['problem', 'time'])
data_julia         = np.genfromtxt('julia.csv',         delimiter=';', skip_header=1, names=['problem', 'time'])

plt.plot(data_python['problem'], data_python['time'], 'o-')
plt.plot(data_fsharp['problem'], data_fsharp['time'], 'o-')
#plt.plot(data_fsharp_bigint['problem'], data_fsharp_bigint['time'], 'o-', zorder=1)
plt.plot(data_julia['problem'], data_julia['time'], 'o-')

plt.title ('Project Euler performance comparison')
plt.xlabel('Problem')
plt.ylabel('Time (s)')
#plt.legend(['Python', 'F#', 'F# (bigint)', 'Julia'], loc='upper right')
plt.legend(['Python', 'F#', 'Julia'], loc='upper right')
plt.xticks(range(1, int(data_python[len(data_python)-1][0]) + 1))
plt.tick_params(axis='x', which='major', labelsize=6)
plt.yscale('log')
#plt.ylim(0.0, 0.05);

plt.gcf().set_size_inches(18.5,10.5)
#plt.show()
plt.savefig('plot.png')