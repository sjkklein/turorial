# Data format description  

this doc describes the data formats of the files in this directory

## .bin0

multi channel ADC data in counts. The binary format is described by the following details:

all multibyte fields are big endian
All samples are int16 values

* b0 = 0 (type of file)
* b1 = Number of channels in the data (nChannels)
* b2-5 = (int32) Samples per second
* [array of samples]
* * each samples is nChannels of uint16 values

Each value has the following conversion formula

mV = counts / 2

## .bin1

.bin1 is similart to .bin0
all multibyte fields are big endian
All samples are float32

* b0 = 1 (type of file)
* b1 = Number of channels in the data (nChannels)
* b2-5 = (int32) Samples per second
* [array of samples]
* * each samples is nChannels of float32 values

## .csv

If we get there