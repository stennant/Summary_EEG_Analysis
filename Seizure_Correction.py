"""
Author: Sarah Tennant
Date: 8/8/2024
Script: Seizure_Correction.py

Description: This script takes the sleep score csv that is output from R, and the seizure csv output from Matlab,
and checks that every seizure is recorded correctly in the sleep score

"""

# import packages
from pylab import *
import pandas as pd
import numpy as np


def round_down(num, divisor):
    return num - (num % divisor)


def correct_seizures(data, seizure_times_path):
    # Load seizure correction from .csv
    seizure_times = pd.read_csv(seizure_times_path, delimiter=",") # read .csv file with sleep score
    seizure_number = len(np.array(seizure_times['dur']))

    for rowcount, row in enumerate(range(len(seizure_times))):
        seizure_start_time = seizure_times.at[rowcount, 'sec_start']
        seizure_duration = round_down(seizure_times.at[rowcount, 'dur'], 1)
        epoch_start_number = seizure_start_time/5
        epoch = int(round(epoch_start_number))
        if data.at[epoch, "sleep.score"] != 4:
            data.at[epoch, "sleep.score"] = 4
        if seizure_duration > 5:
            if data.at[epoch+1, "sleep.score"] != 4:
                data.at[epoch+1, "sleep.score"] = 4
        if seizure_duration > 10:
            if data.at[epoch+2, "sleep.score"] != 4:
                data.at[epoch+2, "sleep.score"] = 4
    return data, seizure_number
