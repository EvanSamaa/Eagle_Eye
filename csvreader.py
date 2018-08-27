import csv
import numpy as np
import pickle
import matplotlib.pyplot as plt

def getcsv(csvName):
	museData = []
	with open(csvName, newline = '') as csvfile:
	    dataReader = csv.reader (csvfile, delimiter = ',')
	    for rowNum in dataReader:
	        museData = museData + [rowNum]
	#museData looks like [[row],[row],[row]]
	
	return museData
# time = np.array(museDataMatrix[0])
# DataStream1 = np.array(museDataMatrix[1])

# fft_DataStream1 = np.fft.fft(DataStream1)
# print(fft_DataStream1)

# freq = np.fft.fftfreq(time.shape[0])
# plt.plot(freq, fft_DataStream1.real, freq, fft_DataStream1.imag)

# plt.show()


