"""
Author: Sarah Tennant
Date: 15/10/2024
Script: Control_Post_Analysis.py

Description:

"""

# import packages
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


def process_dir(file_path):
    # Load sleep state score from .csv
    data = pd.read_csv(file_path, delimiter=",") # read .csv file with sleep score
    return data



def plot_average_seizures(data, output_path):
    df = data.loc[data['Age'] == '17 weeks']

    het_syn21 = df.loc[df['Treatment'] == 'HET - UPV-AAV9/SYN21', 'Number of seizures']
    het_syn20 = df.loc[df['Treatment'] == 'HET - UPV-AAV9/SYN20', 'Number of seizures']
    wt_pbs = df.loc[df['Treatment'] == 'WT - PBS', 'Number of seizures']
    het_pbs = df.loc[df['Treatment'] == 'HET - PBS', 'Number of seizures']


    het_syn21_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'HET SYN21', 'Number of seizures']))
    het_syn20_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'HET SYN20', 'Number of seizures']))
    wt_pbs_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'WT PBS', 'Number of seizures']))
    het_pbs_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'HET PBS', 'Number of seizures']))

    het_syn21_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'HET SYN21', 'Number of seizures']))/math.sqrt(8)
    het_syn20_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'HET SYN20', 'Number of seizures']))/math.sqrt(8)
    wt_pbs_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'WT PBS', 'Number of seizures']))/math.sqrt(8)
    het_pbs_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'HET PBS', 'Number of seizures']))/math.sqrt(8)

    total_time_wake = [het_syn21_mean, het_syn20_mean, het_pbs_mean, wt_pbs_mean]
    average_sd = [het_syn21_sd, het_syn20_sd, het_pbs_sd, wt_pbs_sd]
    bins = np.arange(4)

    #color = ['OrangeRed', 'PeachPuff', 'SandyBrown', 'dimgrey']
    color = ['forestgreen', 'dodgerblue', 'mediumslateblue', 'dimgrey']

    percent_histogram = plt.figure(figsize=(3, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.plot(np.random.uniform(low=-0.2, high=0.2, size=(len(het_syn21))), np.array(het_syn21), color = "black", marker = 's', linestyle='None', markersize = 2)
    ax.plot(np.random.uniform(low=0.8, high=1.2, size=(len(het_syn20))), np.array(het_syn20), color = "black", marker = 's', linestyle='None', markersize = 2)
    ax.plot(np.random.uniform(low=1.8, high=2.2, size=(len(het_pbs))), np.array(het_pbs), color = "black", marker = 's', linestyle='None', markersize = 2)
    ax.plot(np.random.uniform(low=2.8, high=3.2, size=(len(wt_pbs))), np.array(wt_pbs), color = "black", marker = 's', linestyle='None', markersize = 2)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'SYN21', 'SYN20', 'PBS', 'WT'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.3, right=0.87, top=0.92)
    plt.savefig(output_path + '/average_seizures' + '.png', dpi=100)
    return


def plot_seizure_duration(data, output_path):
    df = data.loc[data['Age'] == '17 weeks']

    het_syn21 = df.loc[df['Treatment'] == 'HET - UPV-AAV9/SYN21', 'Avg. seizure duration']
    het_syn20 = df.loc[df['Group'] == 'HET - UPV-AAV9/SYN20', 'Avg. seizure duration']
    wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'Avg. seizure duration']
    het_pbs = df.loc[df['Group'] == 'HET - PBS', 'Avg. seizure duration']


    het_syn21_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'HET SYN21', 'Avg. seizure duration']))
    het_syn20_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'HET SYN20', 'Avg. seizure duration']))
    wt_pbs_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'WT PBS', 'Avg. seizure duration']))
    het_pbs_mean = np.nanmean(np.array(df.loc[df['Treatment'] == 'HET PBS', 'Avg. seizure duration']))

    het_syn21_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'HET SYN21', 'Avg. seizure duration']))/math.sqrt(8)
    het_syn20_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'HET SYN20', 'Avg. seizure duration']))/math.sqrt(8)
    wt_pbs_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'WT PBS', 'Avg. seizure duration']))/math.sqrt(8)
    het_pbs_sd = np.nanstd(np.array(df.loc[df['Treatment'] == 'HET PBS', 'Avg. seizure duration']))/math.sqrt(8)

    total_time_wake = [het_syn21_mean, het_syn20_mean, het_pbs_mean, wt_pbs_mean]
    average_sd = [het_syn21_sd, het_syn20_sd, het_pbs_sd, wt_pbs_sd]
    bins = np.arange(4)

    color = ['forestgreen', 'dodgerblue', 'mediumslateblue', 'dimgrey']

    percent_histogram = plt.figure(figsize=(3, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.plot(np.random.uniform(low=-0.2, high=0.2, size=(len(het_syn21))), np.array(het_syn21), color = "black", marker = 's', linestyle='None', markersize = 2)
    ax.plot(np.random.uniform(low=0.8, high=1.2, size=(len(het_syn20))), np.array(het_syn20), color = "black", marker = 's', linestyle='None', markersize = 2)
    ax.plot(np.random.uniform(low=1.8, high=2.2, size=(len(het_pbs))), np.array(het_pbs), color = "black", marker = 's', linestyle='None', markersize = 2)
    ax.plot(np.random.uniform(low=2.8, high=3.2, size=(len(wt_pbs))), np.array(wt_pbs), color = "black", marker = 's', linestyle='None', markersize = 2)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'SYN21', 'SYN20', 'PBS', 'WT'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.3, right=0.87, top=0.92)
    plt.savefig(output_path + '/average_seizure_duration' + '.png', dpi=100)
    return

def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    overall_data_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/SyngapE8_Analysis.csv'
    output_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/'

    # LOAD DATA
    overall_data = process_dir(overall_data_path) # overall data

    # BAR GRAPHS
    plot_average_seizures(overall_data, output_path)
    plot_seizure_duration(overall_data, output_path)




if __name__ == '__main__':
    main()


