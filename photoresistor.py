import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from matplotlib.ticker import FormatStrFormatter

data = []
data2 = []

with open('strobe1_4.3kHz.txt') as file: #write your file here
    print(file.readline())
    for line in file:
        data.append(int(line.replace('\n','')))
file.close()


for i in range(len(data)):
    data2.append(0.000273 * (i))
plt.figure(1) #obvious
plt.plot(data2, data)
plt.xlabel('czas')
plt.ylabel('amplituda')
plt.xlim(0,2)
plt.show()

y = np.array(data) 
t = np.array(data2)


Fs = 4300 #number of samples per seconds
T = 1/Fs

N = t.size

spectre = np.abs(fft(y))

spectre[0] = spectre[0] / N
i = 1
while i < N:
    spectre[i] = spectre [i] / (N/2)
    i += 1
    
dFs = Fs/N
f = np.arange(0,Fs, dFs)
fig, ax=plt.subplots()
ax.plot(f, spectre)
ax.set_xscale("log")
plt.xlim(1, Fs/2)
ax.xaxis.set_minor_formatter(FormatStrFormatter("%d"))
ax.tick_params(axis='x', which='major', length=6, labelsize=10)
ax.tick_params(axis='x', which='minor', labelsize="6", labelrotation=90)
plt.show()