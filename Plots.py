# import packages
from pylab import *
import numpy as np


def plot_total_states(total_epochs_for_each_state, output_path):

    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'MidnightBlue']
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_epochs_for_each_state, color= color)
    plt.ylabel('Total number of epochs', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'wake', 'nrem', 'rem', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_epochs_per_state' + '.png', dpi=200)

def plot_total_states_sleep(total_epochs_for_each_state, output_path):

    color = ['LightSkyBlue', 'DodgerBlue', 'MidnightBlue']

    total_epochs_for_each_state_sleep = [total_epochs_for_each_state[0], total_epochs_for_each_state[1] + total_epochs_for_each_state[2], total_epochs_for_each_state[3]]
    bins = np.arange(3)

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_epochs_for_each_state_sleep, color= color)
    plt.ylabel('Total number of epochs', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=4)
    ax.set_xticklabels(['', 'wake', 'sleep', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_epochs_per_state_sleep' + '.png', dpi=200)



def plot_total_states_for_light_and_dark(total_epochs, output_path):

    bins = np.arange(8)
    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'MidnightBlue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_epochs, color= color)
    plt.ylabel('Total number of epochs', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=9)
    ax.set_xticklabels(['', 'wake', 'nrem', 'rem', 'swd', 'wake', 'nrem', 'rem', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=7000, xmin =0, xmax=0.482, color='grey', linewidth=10, alpha=0.85, zorder=0)
    plt.axhline(y=7000, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_epochs_per_state_in_light_and_dark' + '.png', dpi=200)


def plot_total_states_sleep_light_and_dark(total_epochs, output_path):

    total_epochs_sleep = [total_epochs[0], total_epochs[1] + total_epochs[2], total_epochs[3], total_epochs[4], total_epochs[5] + total_epochs[6], total_epochs[7]]
    bins = np.arange(6)
    color = ['LightSkyBlue', 'DodgerBlue', 'Blue', 'MidnightBlue']

    percent_histogram = plt.figure(figsize=(6, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_epochs_sleep, color= color)
    plt.ylabel('Total number of epochs', fontsize=12, labelpad=10)
    plt.xlabel('Sleep state', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=7)
    ax.set_xticklabels(['', 'wake', 'sleep', 'swd', 'wake', 'sleep', 'swd'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=7000, xmin =0, xmax=0.482, color='grey', linewidth=10, alpha=0.85, zorder=0)
    plt.axhline(y=7000, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.22, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_epochs_per_state_sleep_light_and_dark' + '.png', dpi=200)


def plot_states_per_hour(df,output_path):
    print('plotting histogram of sleep states per hour...')

    wake = np.array(df.loc[:, "total_wake_epochs"])
    nrem = np.array(df.loc[:, "total_nrem_epochs"])
    rem = np.array(df.loc[:, "total_rem_epochs"])
    swd = np.array(df.loc[:, "total_swd_epochs"])
    bins = np.arange(24)

    epochs_histogram = plt.figure(figsize=(6, 4))
    ax = epochs_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, swd, color = "MidnightBlue")
    ax.bar(bins, rem, bottom = swd, color = "Blue")
    ax.bar(bins, nrem, bottom = swd + rem, color = "DodgerBlue")
    ax.bar(bins, wake, bottom = swd + rem + nrem, color = "LightSkyBlue")
    plt.ylabel('Total number of epochs', fontsize=12, labelpad=10)
    plt.xlabel('Hour', fontsize=12, labelpad=10)
    plt.legend(["swd", "rem", "nrem", "wake"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.12, right=0.87, top=0.92)
    plt.savefig(output_path + '/epochs_per_hour' + '.png', dpi=200)
    plt.close()



def plot_bout_durations(df, seizure_number, output_path):
    print('plotting histogram of average bout durations...')

    wake = np.nanmean(np.array(df.loc[:, "wake_bout_durations"]))
    nrem = np.nanmean(np.array(df.loc[:, "nrem_bout_durations"]))
    rem = np.nanmean(np.array(df.loc[:, "rem_bout_durations"]))

    wake_array = np.array(df.loc[:, "wake_bout_durations"])
    nrem_array = np.array(df.loc[:, "nrem_bout_durations"])
    rem_array = np.array(df.loc[:, "rem_bout_durations"])

    wake_shape = np.shape(wake_array[~np.isnan(wake_array)])[0]
    nrem_shape = np.shape(nrem_array[~np.isnan(nrem_array)])[0]
    rem_shape = np.shape(rem_array[~np.isnan(rem_array)])[0]

    wake_sd = np.nanstd(np.array(df.loc[:, "wake_bout_durations"]))/math.sqrt(wake_shape)
    nrem_sd = np.nanstd(np.array(df.loc[:, "nrem_bout_durations"]))/math.sqrt(nrem_shape)
    rem_sd = np.nanstd(np.array(df.loc[:, "rem_bout_durations"]))/math.sqrt(rem_shape)

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
    plt.savefig(output_path + '/average_bout_duration' + '.png', dpi=200)

    wake_array = np.array(df.loc[:, "wake_bout_durations"])
    wake = np.shape(wake_array[~np.isnan(wake_array)])[0]
    nrem_array = np.array(df.loc[:, "nrem_bout_durations"])
    nrem = np.shape(nrem_array[~np.isnan(nrem_array)])[0]
    rem_array = np.array(df.loc[:, "rem_bout_durations"])
    rem = np.shape(rem_array[~np.isnan(rem_array)])[0]

    average_durations = [wake, nrem, rem, seizure_number]
    bins = np.arange(4)

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
    plt.savefig(output_path + '/total_bout_number' + '.png', dpi=200)



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