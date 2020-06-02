# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn 
import sys

from read_excel import read_excel

Fs = 500.0; # sampling rate采样率 
Ts = 1.0/Fs; # sampling interval 采样区间 
#t = np.arange(0,1,Ts) # time vector,这里Ts也是步长 
#
#ff = 25; # frequency of the signal 
#y = np.sin(2*np.pi*ff*t) 

if len(sys.argv)<4:
	print("please input excel file and sheet name, for example:")
	print("python signal_fft.py \"imu_sample.xlsx\" \"static\" 5")
	sys.exit(1)

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

print(type(sys.argv[0]))
print(type(sys.argv[1]))
print(type(sys.argv[2]))
print(type(sys.argv[3]))

#y=read_excel(r'imu_data.xlsx', '04', 0)
y=read_excel(sys.argv[1], sys.argv[2], int(sys.argv[3]))
n = len(y) # length of the signal 
k = np.arange(n) 
T = n/Fs 
t = np.arange(0,T,Ts) # time vector,这里Ts也是步长 
frq = k/T # two sides frequency range 
frq1 = frq[range(int(n/2))] # one side frequency range 
YY = np.fft.fft(y) # 未归一化 
Y = np.fft.fft(y)/n # fft computing and normalization 归一化
Y1 = Y[range(int(n/2))] 

fig, ax = plt.subplots(4, 1) 

ax[0].plot(t,y) 
ax[0].set_xlabel('Time') 
ax[0].set_ylabel('Amplitude') 

ax[1].plot(frq,abs(YY),'r') # plotting the spectrum 
ax[1].set_xlabel('Freq (Hz)') 
ax[1].set_ylabel('|Y(freq)|') 

ax[2].plot(frq,abs(Y),'G') # plotting the spectrum 
ax[2].set_xlabel('Freq (Hz)') 
ax[2].set_ylabel('|Y(freq)|') 

ax[3].plot(frq1,abs(Y1),'B') # plotting the spectrum 
ax[3].set_xlabel('Freq (Hz)') 
ax[3].set_ylabel('|Y(freq)|') 

plt.show()
