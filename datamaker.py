#this is to generate whaterver
import struct
import math
import matplotlib.pyplot as plt 
import sys

#print('hi')
#print(sys.argv)
#sys.exit(0)

""" as;"ldkfjasl;dkjfal;"skdjf;kjf   """

def sinMaker(sampleFreq, sinFreq, amplitude, samplesN):
	"""
	generate a sine wave
    this a list containing a sine wave
	"""
	wave = [0] * samplesN
	for i in range(samplesN):
		wave[i] = amplitude * math.sin(2 * math.pi * i * sinFreq / sampleFreq)
	return wave

wave = sinMaker(8000, 80, 10, 8000)

wave = [ x * 1.2 for x in wave ] 

wave = [ sum(x) for x in zip(wave, sinMaker(8000, 20, 16, 8000)) ]
wave = [ sum(x) for x in zip(wave, sinMaker(8000, 25, 13, 8000)) ]
wave = [ sum(x) for x in zip(wave, sinMaker(8000, 1000, 19, 8000)) ]
wave = [ sum(x) for x in zip(wave, sinMaker(8000, 70, 23, 8000)) ]
wave = [ sum(x) for x in zip(wave, sinMaker(8000, 12, 10, 8000)) ]
wave = [ sum(x) for x in zip(wave, sinMaker(8000, 60, 11, 8000)) ]

for point in wave:
	sys.stdout.buffer.write(struct.pack('h', int(point)))

sys.exit(0)