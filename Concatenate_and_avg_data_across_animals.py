
# import packages
import os
import glob
import pandas as pd
import numpy as np

def avg_across_days(day1, day2):
    #sleep_analysis_avg = pd.DataFrame()
    avg_day = day1.copy()

    for col, column in enumerate(day1):
        if col > 2:
            day1_col1 = day1[column]
            day2_col1 = day2[column]
            average = np.mean(np.array([day1_col1, day2_col1]), axis=0)
            avg_day[column] = average
    #sleep_analysis_data = pd.concat([sleep_analysis_avg, average])
    return avg_day

def concat_multi_dir():
    analysis_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/17W/'

    local_output_path = '/Volumes/Sarah/SYNGAPE8/analysis_all_animals_avg.csv'

    if os.path.exists(analysis_path):
        print('I found the analysis folder.')

    sleep_analysis_data = pd.DataFrame()
    for recording_folder in glob.glob(analysis_path + '*'):
        os.path.isdir(recording_folder)
        data_path = recording_folder + '/24h/total_sleep_states.csv'
        if os.path.exists(data_path):
            print('I found a data frame.')
            sleep_analysis_day1 = pd.read_csv(data_path, delimiter="\t")
        data_path = recording_folder + '/48h/total_sleep_states.csv'
        if os.path.exists(data_path):
            print('I found a data frame.')
            sleep_analysis_day2 = pd.read_csv(data_path, delimiter="\t")

            sleep_analysis = avg_across_days(sleep_analysis_day1, sleep_analysis_day2)

            sleep_analysis_data = pd.concat([sleep_analysis_data, sleep_analysis])
    sleep_analysis_data.to_csv(local_output_path)
    return sleep_analysis_data



def avg_across_days_hours(day1, day2):
    #sleep_analysis_avg = pd.DataFrame()
    avg_day = day1.copy()

    for col, column in enumerate(day1):
        if col > 1:
            day1_col1 = day1[column]
            day2_col1 = day2[column]
            average = np.mean(np.array([day1_col1, day2_col1]), axis=0)
            avg_day[column] = average
    #sleep_analysis_data = pd.concat([sleep_analysis_avg, average])
    return avg_day

def concat_hourly_dir():
    analysis_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/17W/'

    local_output_path = '/Volumes/Sarah/SYNGAPE8/analysis_hour_by_hour_all_animals_avg.csv'

    if os.path.exists(analysis_path):
        print('I found the analysis folder.')

    sleep_analysis_data = pd.DataFrame()
    for recording_folder in glob.glob(analysis_path + '*'):
        os.path.isdir(recording_folder)
        data_path = recording_folder + '/24h/data_per_hour.csv'
        if os.path.exists(data_path):
            print('I found a data frame.')
            sleep_analysis_day1 = pd.read_csv(data_path, delimiter="\t")
        data_path = recording_folder + '/48h/data_per_hour.csv'
        if os.path.exists(data_path):
            print('I found a data frame.')
            sleep_analysis_day2 = pd.read_csv(data_path, delimiter="\t")

            sleep_analysis = avg_across_days_hours(sleep_analysis_day1, sleep_analysis_day2)

            sleep_analysis_data = pd.concat([sleep_analysis_data, sleep_analysis])

    sleep_analysis_data.to_csv(local_output_path)
    return sleep_analysis_data




#  this is here for testing
def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    sleep_data = concat_multi_dir()
    sleep_data = concat_hourly_dir()

    return sleep_data

if __name__ == '__main__':
    main()