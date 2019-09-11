#this is to generate whaterver
from struct import pack
import math
import matplotlib.pyplot as plt 
import sys

SAMPLE_RATE=8000

def sinMaker(sampleFreq, sinFreq, amplitude, samplesN):
    """
    generate a sine wave
    this a list containing a sine wave
    """
    wave = [0] * samplesN
    for i in range(samplesN):
        wave[i] = amplitude * math.sin(2 * math.pi * i * sinFreq / sampleFreq)
    return wave

class binX:
    def __init__(self, fname, binType, sample_rate, channels_n):
        self.sample_rate = sample_rate
        self.binType = binType
        self.fname = fname
        self.channels_n = channels_n

    def print_header(self):
        with open(self.fname, 'wb') as out:
            out.write(pack('>b', self.binType))
            out.write(pack('>b', self.channels_n))
            out.write(pack('>i', self.sample_rate))

    def generate_print_data(self):
        if self.binType == 0:
            self.generate_print_data0()
        elif self.binType == 1:
            self.generate_print_data1()

    def generate_print_data0(self):
        # make each wave, append it to the array of points
        points_n = 36000
        points = []
        wave = sinMaker(self.sample_rate, 80, 10, points_n)
        wave = [ x * 1.2 for x in wave ] 
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 20, 16, points_n)) ]
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 25, 13, points_n)) ]
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 1000, 19, points_n)) ]
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 60, 200, points_n)) ]
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 2359, 10, points_n)) ]
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 60, 11, points_n)) ] 
        points.append(wave)
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 666, 300, points_n)) ] 
        points.append(wave)
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 101, 900, points_n)) ] 
        points.append(wave)
        wave = [ sum(x) for x in zip(wave, sinMaker(self.sample_rate, 303, 3030, points_n)) ] 
        points.append(wave)
        with open(self.fname, 'ab') as out:
            for tup in zip(*points):
                for p in tup:
                    out.write(pack(">h", int(p)))

    def generate_print_data1(self):
        # make each wave, append it to the array of points
        points_n = 4000
        points = []

        for channel_num in range(self.channels_n):
            wave = sinMaker(self.sample_rate, 80, 10, points_n)

        with open(self.fname, 'ab') as out:
            for tup in zip(*points):
                for p in tup:
                    out.write(pack(">h", int(p)))


if __name__ == '__main__':
    print('main')
    b0 = binX("out.bin0", 0, 8000, 4)
    b0.print_header()
    b0.generate_print_data()

    b1 = binX("out.bin1", 1, 1000, 90)
    b1.print_header()
    b1.generate_print_data()

#    if __name__ == "__main__":
#     wave = sinMaker(SAMPLE_RATE, 80, 10, SAMPLE_RATE)

#     wave = [ x * 1.2 for x in wave ] 

#     wave = [ sum(x) for x in zip(wave, sinMaker(SAMPLE_RATE, 20, 16, SAMPLE_RATE)) ]
#     wave = [ sum(x) for x in zip(wave, sinMaker(SAMPLE_RATE, 25, 13, SAMPLE_RATE)) ]
#     wave = [ sum(x) for x in zip(wave, sinMaker(SAMPLE_RATE, 1000, 19, SAMPLE_RATE)) ]
#     wave = [ sum(x) for x in zip(wave, sinMaker(SAMPLE_RATE, 70, 23, SAMPLE_RATE)) ]
#     wave = [ sum(x) for x in zip(wave, sinMaker(SAMPLE_RATE, 2359, 10, SAMPLE_RATE)) ]
#     wave = [ sum(x) for x in zip(wave, sinMaker(SAMPLE_RATE, 60, 11, SAMPLE_RATE)) ]

#     sys.exit(0)