import matplotlib.pyplot as plt
import numpy as np

data_python        = np.genfromtxt('python.csv',        skip_header=1) 
data_fsharp        = np.genfromtxt('fsharp.csv',        skip_header=1)
data_fsharp_bigint = np.genfromtxt('fsharp-bigint.csv', skip_header=1)
data_julia         = np.genfromtxt('julia.csv',         skip_header=1)
#plt.plot(data_python, data_fsharp, data_fsharp_bigint, data_julia,'o-')
plt.plot(data_python,'o-')
plt.plot(data_fsharp,'o-')
plt.plot(data_fsharp_bigint,'o-')
plt.plot(data_julia,'o-')
plt.title ('Project Euler performance comparison')
plt.ylabel('Time (ms)')
plt.xlabel('Problem')
plt.legend(['Python', 'F#', 'F# (bigint)', 'Julia'], loc='lower right')
#plt.set_xlim([xmin,xmax])
#plt.set_ylim([0,0.5])
#plt.axis('off')
ax = plt.gca();
ax.set_xticks(list(range(1,len(data_python))), minor=True)
#ax.set_xlim(0.0, width_of_im);
ax.set_ylim(0.0, 0.05);
plt.show()
#plt.savefig('plot.png')