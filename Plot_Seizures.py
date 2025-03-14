
# import packages
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
plt.rcParams['hatch.linewidth'] = 4.0  # previous svg hatch linewidth


def process_dir(file_path):
    # Load sleep state score from .csv
    data = pd.read_csv(file_path, delimiter=",") # read .csv file with sleep score
    return data

def plot_average_seizures(df, output_path):

    wake_het_syn21 = df.loc[df['Groups'] == 'HET SYN21', 'Total']
    wake_het_syn20 = df.loc[df['Groups'] == 'HET SYN20', 'Total']
    wake_wt_pbs = df.loc[df['Groups'] == 'WT PBS', 'Total']
    wake_het_pbs = df.loc[df['Groups'] == 'HET PBS', 'Total']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'HET SYN21', 'Total']))
    wake_het_syn20_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'HET SYN20', 'Total']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'WT PBS', 'Total']))
    wake_het_pbs_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'HET PBS', 'Total']))


    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'HET SYN21', 'Total']))/math.sqrt(8)
    wake_het_syn20_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'HET SYN20', 'Total']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'WT PBS', 'Total']))/math.sqrt(8)
    wake_het_pbs_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'HET PBS', 'Total']))/math.sqrt(8)


    total_time_wake = [wake_wt_pbs_mean, wake_het_pbs_mean, wake_het_syn21_mean, wake_het_syn20_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_pbs_sd, wake_het_syn21_sd, wake_het_syn20_sd]
    bins = np.arange(4)
    total_time_wake2 = [0, 0, 0, wake_het_syn20_mean]

    #color = ['#363636', 'mediumseagreen', 'dodgerblue', 'crimson']
    color = ['#363636', '#ff5b00', '#ffb16d', '#ffb16d']

    percent_histogram = plt.figure(figsize=(3, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color, edgecolor = 'black', linewidth=1.5)
    ax.bar(bins, total_time_wake2, color = color, edgecolor = '#ff5b00', hatch = '//', linewidth=1.5)
    ax.bar(bins, total_time_wake2, edgecolor = 'black', color='none', zorder=1, linewidth=1.5)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_pbs))), np.array(wake_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn20))), np.array(wake_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Mean number of seizures (24h)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT', 'PBS', 'SYN21', 'SYN20'])
    ax.tick_params(
        axis='both',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=True,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        right=False,
        left=True,
        labelleft=True,
        labelbottom=True,
        labelsize=12,
        length=5,
        width=1.5)  # labels along the bottom edge are off
    ax.axvline(-0.55, linewidth=1.5, color='black')  # bold line on the y axis
    ax.axhline(0, linewidth=1.5, color='black')  # bold line on the x axis
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.35, right=0.87, top=0.92)
    plt.savefig(output_path + '/average_seizures' + '.png', dpi=100)




def plot_average_seizures_duration(df, output_path):

    wake_het_syn21 = df.loc[df['Groups'] == 'HET SYN21', 'Total_duration']
    wake_het_syn20 = df.loc[df['Groups'] == 'HET SYN20', 'Total_duration']
    wake_wt_pbs = df.loc[df['Groups'] == 'WT PBS', 'Total_duration']
    wake_het_pbs = df.loc[df['Groups'] == 'HET PBS', 'Total_duration']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'HET SYN21', 'Total_duration']))
    wake_het_syn20_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'HET SYN20', 'Total_duration']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'WT PBS', 'Total_duration']))
    wake_het_pbs_mean = np.nanmean(np.array(df.loc[df['Groups'] == 'HET PBS', 'Total_duration']))


    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'HET SYN21', 'Total_duration']))/math.sqrt(8)
    wake_het_syn20_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'HET SYN20', 'Total_duration']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'WT PBS', 'Total_duration']))/math.sqrt(8)
    wake_het_pbs_sd = np.nanstd(np.array(df.loc[df['Groups'] == 'HET PBS', 'Total_duration']))/math.sqrt(8)


    total_time_wake = [wake_wt_pbs_mean, wake_het_pbs_mean, wake_het_syn21_mean, wake_het_syn20_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_pbs_sd, wake_het_syn21_sd, wake_het_syn20_sd]
    bins = np.arange(4)
    total_time_wake2 = [0, 0, 0, wake_het_syn20_mean]

    #color = ['#363636', 'mediumseagreen', 'dodgerblue', 'crimson']
    color = ['#363636', '#ff5b00', '#ffb16d', '#ffb16d']

    percent_histogram = plt.figure(figsize=(3, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color, edgecolor = 'black', linewidth=1.5)
    ax.bar(bins, total_time_wake2, color = color, edgecolor = '#ff5b00', hatch = '//', linewidth=1.5)
    ax.bar(bins, total_time_wake2, edgecolor = 'black', color='none', zorder=1, linewidth=1.5)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_pbs))), np.array(wake_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn20))), np.array(wake_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Mean duration (seconds)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT', 'PBS', 'SYN21', 'SYN20'])
    ax.tick_params(
        axis='both',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=True,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        right=False,
        left=True,
        labelleft=True,
        labelbottom=True,
        labelsize=12,
        length=5,
        width=1.5)  # labels along the bottom edge are off
    ax.axvline(-0.55, linewidth=1.5, color='black')  # bold line on the y axis
    ax.axhline(0, linewidth=1.5, color='black')  # bold line on the x axis
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.35, right=0.87, top=0.92)
    plt.savefig(output_path + '/average_seizure_duration' + '.png', dpi=100)




def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    overall_data_path = '/Volumes/Sarah/SYNGAPE8/syngapanalysis.csv'
    output_path = '/Volumes/Sarah/SYNGAPE8/'

    # LOAD DATA
    overall_data = process_dir(overall_data_path) # overall data

    # BAR GRAPHS
    plot_average_seizures(overall_data, output_path)

    plot_average_seizures_duration(overall_data, output_path)




if __name__ == '__main__':
    main()


