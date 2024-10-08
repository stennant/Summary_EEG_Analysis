
# import packages
import os
import glob
import pandas as pd


def concat_multi_dir():
    analysis_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/17W/'

    local_output_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/17W/analysis_all_animals.csv'

    if os.path.exists(analysis_path):
        print('I found the analysis folder.')

    sleep_analysis_data = pd.DataFrame()
    for recording_folder in glob.glob(analysis_path + '*'):
        os.path.isdir(recording_folder)
        data_path = recording_folder + '/total_sleep_states.csv'
        if os.path.exists(data_path):
            print('I found a data frame.')
            sleep_analysis = pd.read_csv(data_path)

            sleep_analysis_data = pd.concat([sleep_analysis_data, sleep_analysis])
    sleep_analysis_data.to_csv(local_output_path)
    return sleep_analysis_data




def concat_hourly_dir():
    analysis_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/17W/'

    local_output_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/17W/analysis_hour_by_hour_all_animals.csv'

    if os.path.exists(analysis_path):
        print('I found the analysis folder.')

    sleep_analysis_data = pd.DataFrame()
    for recording_folder in glob.glob(analysis_path + '*'):
        os.path.isdir(recording_folder)
        data_path = recording_folder + '/data_per_hour.csv'
        if os.path.exists(data_path):
            print('I found a data frame.')
            sleep_analysis = pd.read_csv(data_path)

            sleep_analysis_data = pd.concat([sleep_analysis_data, sleep_analysis])
    #sleep_analysis_data.reset_index(drop=True, inplace=True)
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