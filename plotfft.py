import struct
import matplotlib.pyplot as plt 
import numpy as np
import scipy.fftpack
from datamaker import *
import math

wave = []
with open("out.bin", "rb") as binFile:
    while True:
        binNum = binFile.read(2)
        if not binNum:
            break
        num = struct.unpack('h', binNum)[0]
        wave.append(num)

N = len(wave)
plt.plot(wave)
plt.show()
wave = wave*np.hanning(N)
plt.plot(wave)
plt.show()
print(SAMPLE_RATE)
period = 1 / SAMPLE_RATE
yf = scipy.fftpack.fft(wave) 
xf = np.linspace(0, 1/(2*period), N/2)
print(wave)
#Splt.plot(yf)
#plt.show()
ypos = 2.0 /N * np.abs(yf[:math.floor(N/2)]) * 2
plt.plot(xf, ypos)
plt.show()