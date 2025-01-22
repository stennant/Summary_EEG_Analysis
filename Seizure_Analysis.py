"""
Author: Sarah Tennant
Date: 8/8/2024
Script: Seizure_Analysis.py

Description: This script loads the seizure csv output from Matlab which contains the start, end time and duration of each
seizure for one animal and plots the distribution of seizure durations and other various parameters of seizures in the
selected recording

"""

# import packages
from pylab import *
import pandas as pd
import numpy as np

# import scripts
import Plots


def process_dir(file_path):
    # Load sleep state score from .csv
    data = pd.read_csv(file_path, delimiter=",") # read .csv file with sleep score
    return data

def create_histogram(spike_times, number_of_bins, step):
    posrange = np.linspace(number_of_bins.min(), number_of_bins.max(),  num=step+1)
    values = np.array([[posrange[0], posrange[-1]]])
    H, bins = np.histogram(spike_times, bins=(posrange), range=values)
    return H, bins

def bin_seizure_durations(data):
    durations = np.array(data.loc[:,"dur"])

    posrange = np.linspace(0, 60,  num=60+1)
    values = np.array([[posrange[0], posrange[-1]]])
    H, bins = np.histogram(durations, bins=(posrange), range=values)
    return H, bins

def save_binned_seizure_durations_to_csv(durations, output_path):
    df = pd.DataFrame({'bin_number': np.arange(0,60), 'count': durations})
    df.to_csv(output_path + 'binned_seizure_durations.csv', sep='\t', encoding='utf-8', index=False, header=True)


def bin_seizure_start_times(data):
    start_times = np.array(data.loc[:,"sec_start"])

    posrange = np.linspace(0, 86400,  num=24+1)
    values = np.array([[posrange[0], posrange[-1]]])
    H, bins = np.histogram(start_times, bins=(posrange), range=values)
    return H, bins



def save_seizure_count_per_hour_to_csv(start_times, output_path):
    df = pd.DataFrame({'bin_number': np.arange(0,24), 'count': start_times})
    df.to_csv(output_path + 'seizure_count_per_hour.csv', sep='\t', encoding='utf-8', index=False, header=True)


def load_sleep_data(file_path):
    # Load sleep state score from .csv
    data = pd.read_csv(file_path, delimiter=",") # read .csv file with sleep score
    return data

def find_seizures_around_sleep(sleep_state_data, seizure_start_times):
    #sleep_state_values = np.array(list(flatten(np.array(sleep_state_data))))
    sleep_state_values1 = np.array(sleep_state_data)
    sleep_state_values = np.array(list(sleep_state_values1.flatten()))
    sleep_state_values_flanked = np.hstack((np.zeros((24)), sleep_state_values, np.zeros((24))))

    seizures_around_sleep = []

    for rowcount, row in enumerate(range(len(sleep_state_values_flanked-24))):
        if rowcount > 24:
            current_state = sleep_state_values_flanked[rowcount]
            if current_state == 1:
                time_of_state = (rowcount-24)*5
                before = time_of_state - 120
                after = time_of_state + 125
                seizure_times_around_sleep = seizure_start_times[(seizure_start_times >= before) & (seizure_start_times <= after)]
                seizures_around_sleep = np.append(seizures_around_sleep, seizure_times_around_sleep)

    unique_seizures = np.unique(seizures_around_sleep)
    number_of_seizures = np.count_nonzero(unique_seizures)
    return number_of_seizures, unique_seizures

def find_duration_of_seizures_around_sleep(seizure_start_times, seizure_durations, unique_seizures):
    durations = seizure_durations[np.where(np.in1d(seizure_start_times, unique_seizures))[0]]

    avg_duration = np.nanmean(durations)
    return avg_duration


# calculate total seizures within 2 minutes of sleep (nrem) epochs
def calculate_seizures_around_sleep(sleep_state_path, seizure_start_times, seizure_durations):

    sleep_state_data = load_sleep_data(sleep_state_path)

    df = pd.DataFrame()
    number_of_seizures, unique_seizures = find_seizures_around_sleep(sleep_state_data, seizure_start_times)
    seizure_duration = find_duration_of_seizures_around_sleep(seizure_start_times, seizure_durations, unique_seizures)

    df["seizures_around_sleep"] = pd.Series(number_of_seizures)
    df["duration_of_seizures_around_sleep"] = pd.Series(seizure_duration)
    print('number of seizures within 2 minutes of nrem sleep is ' + str(number_of_seizures))

    return df


def save_seizure_data_to_csv(df, output_path):
    df.to_csv(output_path + 'seizures_2mins_around_nrem.csv', columns = ["seizures_around_sleep", "duration_of_seizures_around_sleep"], sep='\t', encoding='utf-8', index=False, header=True)


def Analyse_SleepScore(sleep_state_path, seizure_times_path, output_path, animal_to_analyse):
    # LOAD DATA
    data = process_dir(seizure_times_path) # overall data

    # BIN SEIZURE DURATIONS
    durations, bins = bin_seizure_durations(data)
    Plots.plot_seizure_durations(durations, output_path)
    save_binned_seizure_durations_to_csv(durations, output_path)

    start_times, bins = bin_seizure_start_times(data)
    Plots.plot_seizure_start_times(start_times, output_path)
    save_seizure_count_per_hour_to_csv(start_times, output_path)

    df = calculate_seizures_around_sleep(sleep_state_path, np.array(data['sec_start']),  np.array(data['dur']))
    save_seizure_data_to_csv(df, output_path)


"""
This is for testing!!
"""

def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    sleep_state_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/SYNGAPE8_3131_BL1-dge_swd.csv'
    file_name = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/24h/seiz/SYNGAPE8_3131_BL1_Seizures.csv'
    output_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/'

    # LOAD DATA
    data = process_dir(file_name) # overall data

    # BIN SEIZURE DURATIONS
    durations, bins = bin_seizure_durations(data)
    Plots.plot_seizure_durations(durations, output_path)
    save_binned_seizure_durations_to_csv(durations, output_path)

    start_times, bins = bin_seizure_start_times(data)
    Plots.plot_seizure_start_times(start_times, output_path)
    save_seizure_count_per_hour_to_csv(start_times, output_path)

    df = calculate_seizures_around_sleep(sleep_state_path, np.array(data['sec_start']),  np.array(data['dur']))
    save_seizure_data_to_csv(df, output_path)


if __name__ == '__main__':
    main()

