"""
Author: Sarah Tennant
Date: 8/8/2024
Script: Seizure_Analysis.py

Description: This script loads the sleep score csv output from R which contains the sleep score for each 5 second epoch
of the 24 hour recording. 0 = wake, 1 = nrem, 2 = rem, 4 = seizure. The script then calculates and plots several
analyses including:
- the total amount of time in minutes spent in each sleep state
- the total number of episodes/bouts for each sleep state
- the average length of bouts for each sleep state

"""

# import packages
import pandas as pd
import numpy as np

# import scripts
import Seizure_Correction
import Plots


'''

### calculate the time spent in each state for the whole recording and light dark portions

'''

# load sleep state data output from R
# Note : Data should be length 24 hours/5 second epochs = 17280 epochs
def process_dir(file_path):
    # Load sleep state score from .csv
    data = pd.read_csv(file_path, delimiter=",") # read .csv file with sleep score
    return data


# calculate the total amount of time in minutes in each sleep state across the 24 hour whole recording
def calculate_total_states(data, df):
    df.at[0,'total_minutes_wake'] = ((np.count_nonzero(data == 0))*5)/60 # count all the rows that equal 0 and convert to minutes
    df.at[0,'total_minutes_nrem'] = ((np.count_nonzero(data == 1))*5)/60 # count all the rows that equal 1 and convert to minutes
    df.at[0,'total_minutes_rem'] = ((np.count_nonzero(data == 2))*5)/60 # count all the rows that equal 2 and convert to minutes
    df.at[0,'total_minutes_swd'] = ((np.count_nonzero(data == 4))*5)/60 # count all the rows that equal 4 and convert to minutes

    df.at[0,'total_minutes_sleep'] = float(df.at[0,'total_minutes_nrem'] + df.at[0,'total_minutes_rem']) # for total sleep just add nrem and rem together

    df.at[0,'period'] = "total" # add a label that this data is for the whole/total recording and not just for the light/dark period
    return df

# calculate the total amount of time in minutes in each sleep state for the light and dark periods of the recording
# Note : light is the first 12 hours/720 minutes and dark is for the last 12 hours/720 minutes
def calculate_total_states_in_light_and_dark(data, df):
    data["time_mins"] = (data.index*5)/60 # first make column with time in minutes

    # calculate and save total minutes for the light period
    df.at[1,'total_minutes_wake'] = (len(data[(data['sleep.score'] == 0) & (data['time_mins'] < 720)])*5)/60
    df.at[1,'total_minutes_nrem'] = (len(data[(data['sleep.score'] == 1) & (data['time_mins'] < 720)])*5)/60
    df.at[1,'total_minutes_rem'] = (len(data[(data['sleep.score'] == 2) & (data['time_mins'] < 720)])*5)/60
    df.at[1,'total_minutes_swd'] = (len(data[(data['sleep.score'] == 2) & (data['time_mins'] < 720)])*5)/60
    df.at[1,'total_minutes_sleep'] = float(df.at[1,'total_minutes_nrem'] + df.at[1,'total_minutes_rem'])
    df.at[1,'period'] = "light" # add a label that this data is for the light period of the recording

    # calculate and save total minutes for the dark period
    df.at[2,'total_minutes_wake'] = (len(data[(data['sleep.score'] == 0) & (data['time_mins'] >= 720)])*5)/60
    df.at[2,'total_minutes_nrem'] = (len(data[(data['sleep.score'] == 1) & (data['time_mins'] >= 720)])*5)/60
    df.at[2,'total_minutes_rem'] = (len(data[(data['sleep.score'] == 2) & (data['time_mins'] >= 720)])*5)/60
    df.at[2,'total_minutes_swd'] = (len(data[(data['sleep.score'] == 2) & (data['time_mins'] >= 720)])*5)/60
    df.at[2,'total_minutes_sleep'] = float(df.at[2,'total_minutes_nrem'] + df.at[2,'total_minutes_rem'])
    df.at[2,'period'] = "dark" # add a label that this data is for the dark period of the recording
    return df


'''

### calculate the bout durations for each sleep state

'''

# function below splits sleep state data into 4 colummns that is the same length as the data but instead of wake = 0, nrem = 1 and rem = 2
# each column represents wake/nrem/rem/swd and 0 = not in that state and 1 = in that state for each epoch of data
def seperate_scores(data):
    data = np.array(data) # convert data to numpy array
    df = pd.DataFrame(columns=['wake_bouts','nrem_bouts','rem_bouts']) # make dataframe with column names

    for rowcount, row in enumerate(range(len(data))):
        current_state = data[rowcount][0]
        if current_state == 0:
            df.at[rowcount,"rem_bouts"] = 0
            df.at[rowcount,"nrem_bouts"] = 0
            df.at[rowcount,"wake_bouts"] = 1
        elif current_state == 1:
            df.at[rowcount,"rem_bouts"] = 0
            df.at[rowcount,"nrem_bouts"] = 1
            df.at[rowcount,"wake_bouts"] = 0
        elif current_state == 2:
            df.at[rowcount,"rem_bouts"] = 1
            df.at[rowcount,"nrem_bouts"] = 0
            df.at[rowcount,"wake_bouts"] = 0
        elif current_state == 4:
            df.at[rowcount,"rem_bouts"] = 0
            df.at[rowcount,"nrem_bouts"] = 0
            df.at[rowcount,"wake_bouts"] = 0
    return df


# calculate duration of each episode/bout for each sleep state
def calculate_duration(data):

    bout_start_times = []
    bout_end_times = []
    bout_start = False # create a flag for whether a bout has started
    for rowcount, row in enumerate(data):
        current_state = data[rowcount]
        if current_state == 1 and bout_start == False:
            bout_start_time = rowcount
            bout_start = True
        elif current_state == 0 and bout_start == True:
            bout_end_time = rowcount
            bout_start = False
            bout_start_times = np.append(bout_start_times, bout_start_time)
            bout_end_times = np.append(bout_end_times, bout_end_time)

    bout_durations = []
    for rowcount, row in enumerate(range(len(bout_start_times))):
        bout_duration = (bout_end_times[rowcount] - bout_start_times[rowcount])*5
        bout_durations = np.append(bout_durations, bout_duration)
    return bout_durations, bout_start_times, bout_end_times


def calculate_bout_durations(data, df):

    # make arrays for each sleep state where 0 represents off and 1 represents on
    seperate_scores_df = seperate_scores(data)

    # calculate duration of episode/bouts
    nrem_bouts, nrem_start_times, nrem_end_times = calculate_duration(np.array(seperate_scores_df.loc[:, "nrem_bouts"]))
    rem_bouts, rem_start_times, rem_end_times = calculate_duration(np.array(seperate_scores_df.loc[:, "rem_bouts"]))
    wake_bouts, wake_start_times, wake_end_times = calculate_duration(np.array(seperate_scores_df.loc[:, "wake_bouts"]))

    # store average bout durations for each sleep state
    df.at[0,"avg_bout_duration_rem"] = np.nanmean(rem_bouts)
    df.at[0,"avg_bout_duration_nrem"] = np.nanmean(nrem_bouts)
    df.at[0,"avg_bout_duration_wake"] = np.nanmean(wake_bouts)

    # store sd bout durations for each sleep state
    df.at[0,"sd_bout_duration_rem"] = np.nanstd(rem_bouts)/np.sqrt(np.shape(rem_bouts)[0])
    df.at[0,"sd_bout_duration_nrem"] = np.nanstd(nrem_bouts)/np.sqrt(np.shape(nrem_bouts)[0])
    df.at[0,"sd_bout_duration_wake"] = np.nanstd(wake_bouts)/np.sqrt(np.shape(wake_bouts)[0])

    # store total number of bouts
    df.at[0,"bout_num_rem"] = np.count_nonzero(rem_bouts)
    df.at[0,"bout_num_nrem"] = np.count_nonzero(nrem_bouts)
    df.at[0,"bout_num_wake"] = np.count_nonzero(wake_bouts)

    # save all the bouts data
    bouts_df = pd.DataFrame(columns=['wake_bout_durations','nrem_bout_durations','rem_bout_durations',
                               'wake_bout_start_times','nrem_bout_start_times','rem_bout_start_times'])

    bouts_df["wake_bout_durations"] = pd.Series(wake_bouts)
    bouts_df["nrem_bout_durations"] = pd.Series(nrem_bouts)
    bouts_df["rem_bout_durations"] = pd.Series(rem_bouts)

    bouts_df["wake_bout_start_times"] = pd.Series(wake_start_times)
    bouts_df["nrem_bout_start_times"] = pd.Series(nrem_start_times)
    bouts_df["rem_bout_start_times"] = pd.Series(rem_start_times)
    return df, bouts_df, seperate_scores_df



def calculate_light_dark_durations(durations, start_times):
    light_durations = durations[start_times < 8640]
    dark_durations = durations[start_times >= 8640]
    return light_durations, dark_durations


def calculate_bout_durations_light_dark(bouts_df, df):

    rem_light_durations, rem_dark_durations = calculate_light_dark_durations(np.array(bouts_df.loc[:, "rem_bout_durations"]), np.array(bouts_df.loc[:, "rem_bout_start_times"]))
    nrem_light_durations, nrem_dark_durations = calculate_light_dark_durations(np.array(bouts_df.loc[:, "nrem_bout_durations"]), np.array(bouts_df.loc[:, "nrem_bout_start_times"]))
    wake_light_durations, wake_dark_durations = calculate_light_dark_durations(np.array(bouts_df.loc[:, "wake_bout_durations"]), np.array(bouts_df.loc[:, "wake_bout_start_times"]))

    # store average bout durations for each sleep state
    df.at[1,"avg_bout_duration_rem"] = np.nanmean(rem_light_durations)
    df.at[1,"avg_bout_duration_nrem"] = np.nanmean(nrem_light_durations)
    df.at[1,"avg_bout_duration_wake"] = np.nanmean(wake_light_durations)

    # store sd bout durations for each sleep state
    df.at[1,"sd_bout_duration_rem"] = np.nanstd(rem_light_durations)/np.sqrt(np.shape(rem_light_durations)[0])
    df.at[1,"sd_bout_duration_nrem"] = np.nanstd(nrem_light_durations)/np.sqrt(np.shape(nrem_light_durations)[0])
    df.at[1,"sd_bout_duration_wake"] = np.nanstd(wake_light_durations)/np.sqrt(np.shape(wake_light_durations)[0])

    # store total number of bouts
    df.at[1,"bout_num_rem"] = np.count_nonzero(rem_light_durations)
    df.at[1,"bout_num_nrem"] = np.count_nonzero(nrem_light_durations)
    df.at[1,"bout_num_wake"] = np.count_nonzero(wake_light_durations)


    # store average bout durations for each sleep state
    df.at[2,"avg_bout_duration_rem"] = np.nanmean(rem_dark_durations)
    df.at[2,"avg_bout_duration_nrem"] = np.nanmean(nrem_dark_durations)
    df.at[2,"avg_bout_duration_wake"] = np.nanmean(wake_dark_durations)

    # store sd bout durations for each sleep state
    df.at[2,"sd_bout_duration_rem"] = np.nanstd(rem_dark_durations)/np.sqrt(np.shape(rem_dark_durations)[0])
    df.at[2,"sd_bout_duration_nrem"] = np.nanstd(nrem_dark_durations)/np.sqrt(np.shape(nrem_dark_durations)[0])
    df.at[2,"sd_bout_duration_wake"] = np.nanstd(wake_dark_durations)/np.sqrt(np.shape(wake_dark_durations)[0])

    # store total number of bouts
    df.at[2,"bout_num_rem"] = np.count_nonzero(rem_dark_durations)
    df.at[2,"bout_num_nrem"] = np.count_nonzero(nrem_dark_durations)
    df.at[2,"bout_num_wake"] = np.count_nonzero(wake_dark_durations)
    return df


'''

### calculate hour by hour bout durations

'''

# find bout durations for each hour
def find_hourly_durations(durations, start_times):
    epochs_array = np.arange(0,17281, 720)
    hourly_duration = np.zeros((24))

    for rowcount, row in enumerate(range(24)):
        epoch_start = epochs_array[rowcount]
        epoch_end = epochs_array[rowcount + 1]
        times = durations[(start_times > epoch_start) & (start_times <= epoch_end)]
        hourly_duration[rowcount] = np.nanmean(times)
        if len(times) == 0:
            hourly_duration[rowcount] = 0

    return hourly_duration


def calculate_duration_per_hour(bouts_df, animal_to_analyse):
    nrem_bouts = find_hourly_durations(np.array(bouts_df.loc[:, "nrem_bout_durations"]), np.array(bouts_df.loc[:, "nrem_bout_start_times"]))
    rem_bouts = find_hourly_durations(np.array(bouts_df.loc[:, "rem_bout_durations"]), np.array(bouts_df.loc[:, "rem_bout_start_times"]))
    wake_bouts = find_hourly_durations(np.array(bouts_df.loc[:, "wake_bout_durations"]), np.array(bouts_df.loc[:, "wake_bout_start_times"]))

    hourly_df = pd.DataFrame(columns=['hour', 'rem_bout_duration_per_hour', 'nrem_bout_duration_per_hour', 'wake_bout_duration_per_hour', 'sleep_bout_duration_per_hour',
                                      'wake_minutes_per_hour','nrem_minutes_per_hour','rem_minutes_per_hour','swd_minutes_per_hour','sleep_minutes_per_hour'])
    hourly_df["hour"] = pd.Series(np.arange(24))
    hourly_df["hour_of_day"] = pd.Series(np.arange(24))
    hourly_df["ID"] = pd.Series(np.repeat(animal_to_analyse, repeats=24))

    hourly_df["rem_bout_duration_per_hour"] = pd.Series(rem_bouts)
    hourly_df["nrem_bout_duration_per_hour"] = pd.Series(nrem_bouts)
    hourly_df["wake_bout_duration_per_hour"] = pd.Series(wake_bouts)
    return hourly_df


'''

### calculate hour by hour time spent in each state

'''

# Calculates the number of epochs spent in each sleep state for each hour of the 24 hour recording
def calculate_states_per_hour(data, hourly_df):

    epochs_array = np.arange(0,17281, 720)

    for rowcount, row in enumerate(range(24)):
            epoch_start = epochs_array[rowcount]
            epoch_end = epochs_array[rowcount+1]
            hourly_epochs = data[epoch_start:epoch_end]
            hourly_df.at[rowcount,"wake_minutes_per_hour"] = (np.count_nonzero(hourly_epochs == 0)*5)/60
            hourly_df.at[rowcount,"nrem_minutes_per_hour"] = (np.count_nonzero(hourly_epochs == 1)*5)/60
            hourly_df.at[rowcount,"rem_minutes_per_hour"] = (np.count_nonzero(hourly_epochs == 2)*5)/60
            hourly_df.at[rowcount,"swd_minutes_per_hour"] = (np.count_nonzero(hourly_epochs == 4)*5)/60
            hourly_df.at[rowcount,'sleep_minutes_per_hour'] = float(hourly_df.at[rowcount,'nrem_minutes_per_hour'] + hourly_df.at[rowcount,'rem_minutes_per_hour']) # for total sleep just add nrem and rem together
    return hourly_df


'''

### save data to csv

'''

def save_states_to_csv(df, output_path):
    df.to_csv(output_path + 'total_sleep_states.csv', sep='\t', encoding='utf-8', index=False, header=True)


def save_states_per_hour_to_csv(df, output_path):
    df.to_csv(output_path + 'sleep_states_per_hour.csv', sep='\t', encoding='utf-8', index=False, header=True)

def save_bout_durations_to_csv(df, output_path):
    df.to_csv(output_path + 'bout_durations.csv', sep='\t', encoding='utf-8', index=False, header=True)

def save_per_hour_data_to_csv(df, output_path):
    df.to_csv(output_path + 'data_per_hour.csv', sep='\t', encoding='utf-8', index=False, header=True)


'''

### MAIN FUNCTION

'''


def Analyse_SleepScore(sleep_state_path, seizure_times_path, output_path, animal_to_analyse):
    # LOAD DATA
    data = process_dir(sleep_state_path) # overall data

    # Make dataframe for storing data
    df = pd.DataFrame(columns = ['ID', 'animal_id','period',
                                 'total_minutes_wake', 'total_minutes_nrem', 'total_minutes_rem', 'total_minutes_swd', 'total_minutes_sleep',
                                 'avg_bout_duration_wake', 'avg_bout_duration_nrem', 'avg_bout_duration_rem', 'avg_bout_duration_swd',
                                 'sd_bout_duration_wake', 'sd_bout_duration_nrem', 'sd_bout_duration_rem', 'sd_bout_duration_swd',
                                 'bout_num_wake', 'bout_num_nrem', 'bout_num_rem', 'bout_num_swd'])

    df.at[0,'ID'] = str(animal_to_analyse) # add a label for animal id
    df.at[1,'ID'] = str(animal_to_analyse) # add a label for animal id
    df.at[2,'ID'] = str(animal_to_analyse) # add a label for animal id
    df.at[0,'animal_id'] = str(animal_to_analyse) # add a label for animal id
    df.at[1,'animal_id'] = str(animal_to_analyse) # add a label for animal id
    df.at[2,'animal_id'] = str(animal_to_analyse) # add a label for animal id

    # SEIZURE CORRECTION
    data, seizure_number = Seizure_Correction.correct_seizures(data, seizure_times_path)

    # CALCULATE TOTAL STATES
    df = calculate_total_states(data, df)
    Plots.plot_total_states(df, output_path)
    Plots.plot_total_states_sleep(df, output_path) # same plot as above but nrem and rem and added together to make 'sleep' catagory

    # CALCULATE TOTAL STATES IN LIGHT AND DARK
    df = calculate_total_states_in_light_and_dark(data, df)
    Plots.plot_total_states_for_light_and_dark(df, output_path)
    Plots.plot_total_states_sleep_light_and_dark(df, output_path) # same plot as above but nrem and rem and added together to make 'sleep' catagory

    # CALCULATE NUMBER AND LENGTH OF BOUTS
    df, bouts_df, seperate_scores_df = calculate_bout_durations(data, df)
    Plots.plot_average_bout_durations(df, output_path)
    Plots.plot_total_bout_number(df, seizure_number, output_path)

    # CALCULATE NUMBER AND LENGTH OF BOUTS IN LIGHT AND DARK
    df = calculate_bout_durations_light_dark(bouts_df, df)
    Plots.plot_average_bout_durations_lightanddark(df, output_path)
    Plots.plot_total_bout_number_lightanddark(df, seizure_number, output_path)

    # SAVE BOUT DURATIONS TO CSV
    #save_bout_durations_to_csv(df, output_path)

    # SAVE TOTAL STATES TO CSV
    save_states_to_csv(df, output_path)

    # CALCULATE TOTAL TIME IN EACH STATE
    hourly_df = calculate_duration_per_hour(bouts_df, animal_to_analyse)
    #Plots.plot_total_durations(df, output_path)

    # CALCULATE STATES PER HOUR
    hourly_df = calculate_states_per_hour(data, hourly_df)
    Plots.plot_states_per_hour(hourly_df, output_path)

    # SAVE HOUR BY HOUR ANALYSIS
    save_per_hour_data_to_csv(hourly_df, output_path)



"""
This is for testing!!
"""

def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    file_name = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/SYNGAPE8_3131_BL1-dge_swd.csv'
    seizure_times_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/24h/seiz/SYNGAPE8_3131_BL1_Seizures.csv'
    output_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/'

    # LOAD DATA
    data = process_dir(file_name) # overall data

    # SEIZURE CORRECTION
    data, seizure_number = Seizure_Correction.correct_seizures(data, seizure_times_path)

    # CALCULATE TOTAL STATES
    df = calculate_total_states(data)
    Plots.plot_total_states(df, output_path)

    # CALCULATE TOTAL STATES IN LIGHT AND DARK
    df = calculate_total_states_in_light_and_dark(data)
    Plots.plot_total_states_for_light_and_dark(df, output_path)

    # CALCULATE STATES PER HOUR
    df = calculate_states_per_hour(data)
    Plots.plot_states_per_hour(df, output_path)
    save_states_to_csv(df, output_path)

    # CALCULATE NUMBER AND LENGTH OF BOUTS
    df = calculate_bout_durations(df)
    Plots.plot_bout_durations(df, seizure_number, output_path)
    save_bout_durations_to_csv(df, output_path)

    # CALCULATE TOTAL TIME IN EACH STATE
    df = calculate_duration_per_hour(df)
    Plots.plot_total_durations(df, output_path)
    save_bout_durations_per_hour_to_csv(df, output_path)


if __name__ == '__main__':
    main()

