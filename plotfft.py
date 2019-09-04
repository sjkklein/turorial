import struct
import matplotlib.pyplot as plt 

wave = []
with open("out.bin", "rb") as binFile:
    while True:
        binNum = binFile.read(2)
        if not binNum:
            break
        num = struct.unpack('h', binNum)[0]
        wave.append(num)

plt.plot(wave)
plt.show()