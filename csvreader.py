import csv
# import numpy as np
# import pickle
# import matplotlib.pyplot as plt

def get_csv(csv_name):
    muse_data = []
    with open(csv_name, newline='') as csv_file:
        # muse_data looks like [[row],[row],[row]]
        data_reader = csv.reader(csv_file, delimter=',')
        for row_num in data_reader:
            muse_data += [row_num]

    return muse_data

# time = np.array(muse_dataMatrix[0])
# DataStream1 = np.array(muse_dataMatrix[1])

# fft_DataStream1 = np.fft.fft(DataStream1)
# print(fft_DataStream1)

# freq = np.fft.fftfreq(time.shape[0])
# plt.plot(freq, fft_DataStream1.real, freq, fft_DataStream1.imag)

# plt.show()


