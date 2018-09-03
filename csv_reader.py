"""
    File Name: csv_reader.py
    Author: Barney Wei
    Date Created: 09/02/2018
    Python Version: 3.5
"""

# import required files and libraries
import csv
import numpy as np


def get_processed_data(csv_file, sensor_cols, data_type_col, data_type):
    """
    main function that returns processed data from csv
    :param csv_file: STRING - file path directory
    :param sensor_cols: INT ARRAY - integer index of sensor columns in csv file
    :param data_type_col: INT - integer index of "data_type"
    :param data_type: STRING - name of the type of csv data to collect (eg. "Person0/eeg"
    :return: NUMPY FLOAT ARRAY - processed data
    """
    raw_data = get_raw_data(csv_file)
    return process_data(raw_data, sensor_cols, data_type_col, data_type)


def get_raw_data(csv_file):
    """
    function that extracts data from csv file located at "csv_file" directory
    :param csv_file: STRING - file path directory
    :return: STRING 2-D LIST - raw csv data
    """
    raw_muse_data = []
    try:
        with open(csv_file, newline='') as file:
            # muse_data looks like [[row],[row],[row]]
            data_reader = csv.reader(file, delimiter=',')
            for row_num in data_reader:
                raw_muse_data += [row_num]

        return raw_muse_data
    except:
        print("ERROR - get_data_from_csv(csv_file): unable to read csv file")


def process_data(raw_data, sensor_cols, data_type_col, data_type):
    """
    function that cleans up "raw_data" by:
    1) extract string values at each "sensor_cols"
    2) convert string to float and replace blanks with 0
    3) input to a numpy array
    4) transpose numpy arraw
    :param raw_data: STRING 2-D LIST - raw csv data
    :param sensor_cols: INT ARRAY - integer index of sensor columns in csv file
    :param data_type_col: INT - integer index of "data_type"
    :param data_type: STRING - name of the type of csv data to collect (eg. " Person0/eeg"
    :return: NUMPY FLOAT ARRAY - processed data
    """
    # initiate a numpy array
    processed_data = np.zeros((0, len(sensor_cols)))

    # iterate through each row in "raw_data" 2D array
    for each_row in raw_data:
        # take each row labelled by "data_type"
        if each_row[data_type_col] == data_type:
            # create temporary list to store a row of sensor values
            temp_list = []
            # iterate through each sensor column of each data row to extract value
            for sensor_col in sensor_cols:
                # replace blank data with zeros and convert data type to float
                if each_row[sensor_col] != "":
                    temp_list += [float(each_row[sensor_col])]
                else:
                    temp_list += [float(0)]
            # appends "temp_list" to numpy array
            processed_data = np.append(processed_data, [temp_list], axis=0)

    # transpose numpy array
    processed_data = processed_data.transpose()

    return processed_data


# CODE TESTING
if __name__ == '__main__':
    csv_file = "SCRAPCSV.csv"
    csv_file = "Blinks1.csv"
    sensor_cols = [2, 3, 4, 5]
    data_type_col = 1
    data_type = " Person0/eeg"
    print(get_raw_data(csv_file))
    print("______________________")
    print(get_processed_data(csv_file, sensor_cols, data_type_col, data_type))
    print(get_processed_data(csv_file, sensor_cols, data_type_col, data_type).shape)
