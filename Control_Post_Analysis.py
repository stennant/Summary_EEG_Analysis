"""
Author: Sarah Tennant
Date: 8/8/2024
Script: Control_Post_Analysis.py

Description: 

"""
# import packages
import os

# import scripts
import SleepScore_Analysis
import Seizure_Analysis


downtime_lists_path = '/Users/sarahtennant/Work_Alfredo/Analysis/Summary_EEG_Analysis/downtime/'


def delete_processed_line(list_to_read_path):
    with open(list_to_read_path, 'r') as file_in:
        data = file_in.read().splitlines(True)
    with open(list_to_read_path, 'w') as file_out:
        file_out.writelines(data[1:])

def get_next_recording():
    recording_to_sort = False
    if not os.listdir(downtime_lists_path):
        return False
    else:
        list_to_read = os.listdir(downtime_lists_path)[0]
        list_to_read_path = downtime_lists_path + list_to_read
        if os.stat(list_to_read_path).st_size == 0:
            os.remove(list_to_read_path)
        else:
            downtime_file_reader = open(list_to_read_path, 'r+')
            recording_to_sort = downtime_file_reader.readlines()[0].strip()

            delete_processed_line(list_to_read_path)
            if recording_to_sort is False:
                return False
            recording_to_sort = recording_to_sort.split("/")[-1]

    return recording_to_sort


def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    analyse_list = True

    if analyse_list is True:
        print('I am checking whether there is something to analyse.')
        animal_to_analyse = get_next_recording()
        if animal_to_analyse is not False:

            #path to the recording .dat file
            sleep_state_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_' + str(animal_to_analyse) + '/SYNGAPE8_' + str(animal_to_analyse) + '_BL1-dge_swd.csv'
            seizure_times_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_' + str(animal_to_analyse) + '/24h/seiz/SYNGAPE8_' + str(animal_to_analyse) + '_BL1_Seizures.csv'
            output_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_' + str(animal_to_analyse) + '/'

            SleepScore_Analysis.Analyse_SleepScore(sleep_state_path, seizure_times_path, output_path)
            Seizure_Analysis.Analyse_SleepScore(sleep_state_path, seizure_times_path, output_path)


if __name__ == '__main__':
    main()

