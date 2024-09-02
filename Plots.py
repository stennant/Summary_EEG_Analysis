# import packages
from pylab import *
import numpy as np
import math

def plot_total_states(df, output_path):

    wake = df.loc[0,"total_minutes_wake"]
    nrem = df.loc[0,"total_minutes_nrem"]
    rem = df.loc[0,"total_minutes_rem"]
    swd = df.loc[0,"total_minutes_swd"]

    total_mins_for_each_state = [wake, nrem, rem, swd]
    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'MidnightBlue']
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_mins_for_each_state, color= color)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'wake', 'nrem', 'rem', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalTime_perstate' + '.png', dpi=200)

def plot_total_states_sleep(df, output_path):

    wake = df.loc[0,"total_minutes_wake"]
    sleep = df.loc[0,"total_minutes_sleep"]
    swd = df.loc[0,"total_minutes_swd"]
    total_mins_for_each_state = [wake, sleep, swd]

    color = ['LightSkyBlue', 'DodgerBlue', 'MidnightBlue']
    bins = np.arange(3)

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_mins_for_each_state, color= color)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=4)
    ax.set_xticklabels(['', 'wake', 'sleep', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalTime_perstate_sleep' + '.png', dpi=200)



def plot_total_states_for_light_and_dark(df, output_path):

    wake_light = df.loc[1,"total_minutes_wake"]
    nrem_light = df.loc[1,"total_minutes_nrem"]
    rem_light = df.loc[1,"total_minutes_rem"]
    swd_light = df.loc[1,"total_minutes_swd"]
    wake_dark = df.loc[2,"total_minutes_wake"]
    nrem_dark = df.loc[2,"total_minutes_nrem"]
    rem_dark = df.loc[2,"total_minutes_rem"]
    swd_dark = df.loc[2,"total_minutes_swd"]

    total_time = [wake_light, nrem_light, rem_light, swd_light, wake_dark, nrem_dark, rem_dark, swd_dark]

    bins = np.arange(8)
    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'MidnightBlue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time, color= color)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=9)
    ax.set_xticklabels(['', 'wake', 'nrem', 'rem', 'swd', 'wake', 'nrem', 'rem', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    #plt.axhline(y=600, xmin =0, xmax=0.482, color='grey', linewidth=10, alpha=0.85, zorder=0)
    plt.axhline(y=600, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    text(0.25, 0.95, 'Light', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
    text(0.75, 0.95, 'Dark', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, color = 'White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalTime_perstate_lightanddark' + '.png', dpi=200)


def plot_total_states_sleep_light_and_dark(df, output_path):

    wake_light = df.loc[1,"total_minutes_wake"]
    sleep_light = df.loc[1,"total_minutes_sleep"]
    swd_light = df.loc[1,"total_minutes_swd"]
    wake_dark = df.loc[2,"total_minutes_wake"]
    sleep_dark = df.loc[2,"total_minutes_sleep"]
    swd_dark = df.loc[2,"total_minutes_swd"]

    total_time = [wake_light, sleep_light, swd_light, wake_dark, sleep_dark, swd_dark]

    bins = np.arange(6)
    color = ['LightSkyBlue', 'DodgerBlue', 'MidnightBlue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time, color= color)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=7)
    ax.set_xticklabels(['', 'wake', 'sleep', 'swd', 'wake', 'sleep', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=600, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    text(0.25, 0.95, 'Light', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
    text(0.75, 0.95, 'Dark', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, color = 'White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalTime_perstate_sleep_lightanddark' + '.png', dpi=200)


def plot_states_per_hour(df,output_path):
    print('plotting histogram of sleep states per hour...')

    wake = np.array(df.loc[:, "wake_minutes_per_hour"])
    nrem = np.array(df.loc[:, "nrem_minutes_per_hour"])
    rem = np.array(df.loc[:, "rem_minutes_per_hour"])
    swd = np.array(df.loc[:, "swd_minutes_per_hour"])
    bins = np.arange(24)

    epochs_histogram = plt.figure(figsize=(6, 4))
    ax = epochs_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, swd, color = "MidnightBlue")
    ax.bar(bins, rem, bottom = swd, color = "Blue")
    ax.bar(bins, nrem, bottom = swd + rem, color = "DodgerBlue")
    ax.bar(bins, wake, bottom = swd + rem + nrem, color = "LightSkyBlue")
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Hour', fontsize=12, labelpad=10)
    plt.legend(["swd", "rem", "nrem", "wake"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.12, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalTime_States_perhour' + '.png', dpi=200)
    plt.close()



def plot_average_bout_durations(df, output_path):
    print('plotting histogram of average bout durations...')

    wake = df.loc[0, "avg_bout_duration_wake"]
    nrem = df.loc[0, "avg_bout_duration_nrem"]
    rem = df.loc[0, "avg_bout_duration_rem"]

    wake_sd = df.loc[0, "sd_bout_duration_wake"]
    nrem_sd = df.loc[0, "sd_bout_duration_nrem"]
    rem_sd = df.loc[0, "sd_bout_duration_rem"]

    average_durations = [wake, nrem, rem]
    average_sd = [wake_sd, nrem_sd, rem_sd]
    bins = np.arange(3)

    color = ['LightSkyBlue', 'DodgerBlue', 'Blue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, average_durations, color = color)
    #ax.plot(np.random.uniform(low=0.6, high=1.4, size=(len(np.array(df.loc[:, "wake_bout_durations"])))), np.array(df.loc[:, "wake_bout_durations"]), color = "LightSkyBlue")
    #ax.plot(np.random.uniform(low=1.6, high=2.4, size=(len(np.array(df.loc[:, "nrem_bout_durations"])))), np.array(df.loc[:, "nrem_bout_durations"]), color = "DodgerBlue")
    #ax.plot(np.random.uniform(low=2.6, high=3.4, size=(len(np.array(df.loc[:, "rem_bout_durations"])))), np.array(df.loc[:, "rem_bout_durations"]), color = "Blue")
    plt.errorbar(bins, average_durations, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Average bout time (seconds)', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'Wake', 'nrem', 'rem'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/AverageDuration_bouts' + '.png', dpi=200)



def plot_average_bout_durations_lightanddark(df, output_path):
    print('plotting histogram of average bout durations...')

    wake_light = df.loc[1, "avg_bout_duration_wake"]
    nrem_light = df.loc[1, "avg_bout_duration_nrem"]
    rem_light = df.loc[1, "avg_bout_duration_rem"]
    wake_dark = df.loc[2, "avg_bout_duration_wake"]
    nrem_dark = df.loc[2, "avg_bout_duration_nrem"]
    rem_dark = df.loc[2, "avg_bout_duration_rem"]

    wake_sd_light = df.loc[1, "sd_bout_duration_wake"]
    nrem_sd_light = df.loc[1, "sd_bout_duration_nrem"]
    rem_sd_light = df.loc[1, "sd_bout_duration_rem"]
    wake_sd_dark = df.loc[2, "sd_bout_duration_wake"]
    nrem_sd_dark = df.loc[2, "sd_bout_duration_nrem"]
    rem_sd_dark = df.loc[2, "sd_bout_duration_rem"]

    average_durations = [wake_light, nrem_light, rem_light, wake_dark, nrem_dark, rem_dark]
    average_sd = [wake_sd_light, nrem_sd_light, rem_sd_light, wake_sd_dark, nrem_sd_dark, rem_sd_dark]
    bins = np.arange(6)

    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'LightSkyBlue', 'DodgerBlue', 'Blue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, average_durations, color = color)
    #ax.plot(np.random.uniform(low=0.6, high=1.4, size=(len(np.array(df.loc[:, "wake_bout_durations"])))), np.array(df.loc[:, "wake_bout_durations"]), color = "LightSkyBlue")
    #ax.plot(np.random.uniform(low=1.6, high=2.4, size=(len(np.array(df.loc[:, "nrem_bout_durations"])))), np.array(df.loc[:, "nrem_bout_durations"]), color = "DodgerBlue")
    #ax.plot(np.random.uniform(low=2.6, high=3.4, size=(len(np.array(df.loc[:, "rem_bout_durations"])))), np.array(df.loc[:, "rem_bout_durations"]), color = "Blue")
    plt.errorbar(bins, average_durations, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Average bout time (seconds)', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=8)
    ax.set_xticklabels(['', 'Wake', 'nrem', 'rem', 'Wake', 'nrem', 'rem'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=290, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    text(0.25, 0.95, 'Light', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
    text(0.75, 0.95, 'Dark', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/AverageDuration_bouts_lightanddark' + '.png', dpi=200)



def plot_total_bout_number(df, seizure_number, output_path):
    wake = df.loc[0, "bout_num_wake"]
    nrem = df.loc[0, "bout_num_nrem"]
    rem = df.loc[0, "bout_num_rem"]

    average_durations = [wake, nrem, rem, seizure_number]
    bins = np.arange(4)
    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'MidnightBlue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, average_durations, color= color)
    plt.ylabel('Total number of bouts', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'Wake', 'nrem', 'rem', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalNumber_bouts' + '.png', dpi=200)



def plot_total_bout_number_lightanddark(df, seizure_number, output_path):
    wake_light = df.loc[1, "bout_num_wake"]
    nrem_light = df.loc[1, "bout_num_nrem"]
    rem_light = df.loc[1, "bout_num_rem"]
    wake_dark = df.loc[2, "bout_num_wake"]
    nrem_dark = df.loc[2, "bout_num_nrem"]
    rem_dark = df.loc[2, "bout_num_rem"]

    average_durations = [wake_light, nrem_light, rem_light, wake_dark, nrem_dark, rem_dark]
    bins = np.arange(6)
    color = ['LightSkyBlue', 'DodgerBlue', 'Blue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, average_durations, color= color)
    plt.ylabel('Total number of bouts', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=8)
    ax.set_xticklabels(['', 'Wake', 'nrem', 'rem', 'Wake', 'nrem', 'rem'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=230, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    text(0.25, 0.95, 'Light', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
    text(0.75, 0.95, 'Dark', horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, color = 'White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/TotalNumber_bouts_lightanddark' + '.png', dpi=200)



def plot_total_durations(df, output_path):
    print('plotting histogram of total duration of each sleep state...')

    wake = np.array(df.loc[0:23, "wake_bout_duration_per_hour"])
    nrem = np.array(df.loc[0:23, "nrem_bout_duration_per_hour"])
    rem = np.array(df.loc[0:23, "rem_bout_duration_per_hour"])

    bins = np.arange(24)

    epochs_histogram = plt.figure(figsize=(6, 4))
    ax = epochs_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, rem, color = "Blue")
    ax.bar(bins, nrem, bottom = rem, color = "DodgerBlue")
    ax.bar(bins, wake, bottom = rem + nrem, color = "LightSkyBlue")
    plt.ylabel('Time (seconds)', fontsize=12, labelpad=10)
    plt.xlabel('Hour', fontsize=12, labelpad=10)
    plt.legend(["rem", "nrem", "wake"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.12, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_duration_per_hour' + '.png', dpi=200)
    return df


def plot_seizure_durations(durations, output_path):

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(np.arange(60), durations, color= "black")
    plt.ylabel('Number of seizures', fontsize=12, labelpad=10)
    plt.xlabel('Time bins (seconds)', fontsize=12, labelpad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/seizure_durations' + '.png', dpi=200)



def plot_seizure_start_times(durations, output_path):

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(np.arange(24), durations, color= "black")
    plt.ylabel('Number of seizures', fontsize=12, labelpad=10)
    plt.xlabel('Time (hours)', fontsize=12, labelpad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/seizure_start_times' + '.png', dpi=200)
