"""
Author: Sarah Tennant
Date: 8/8/2024
Script: Control_Post_Analysis.py

Description:

"""

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

def plot_average_time(data, output_path):
    df = data.loc[data['period'] == 'total']

    wake_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_wake']
    wake_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_wake']
    wake_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'total_minutes_wake']
    wake_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'total_minutes_wake']
    nrem_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_nrem']
    nrem_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_nrem']
    nrem_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'total_minutes_nrem']
    nrem_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'total_minutes_nrem']
    rem_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_rem']
    rem_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_rem']
    rem_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'total_minutes_rem']
    rem_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'total_minutes_rem']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_wake']))
    wake_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_wake']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'total_minutes_wake']))
    wake_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'total_minutes_wake']))
    nrem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_nrem']))
    nrem_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_nrem']))
    nrem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'total_minutes_nrem']))
    nrem_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'total_minutes_nrem']))
    rem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_rem']))
    rem_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_rem']))
    rem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'total_minutes_rem']))
    rem_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'total_minutes_rem']))

    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_wake']))/math.sqrt(8)
    wake_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_wake']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'total_minutes_wake']))/math.sqrt(8)
    wake_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'total_minutes_wake']))/math.sqrt(8)
    nrem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_nrem']))/math.sqrt(8)
    nrem_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_nrem']))/math.sqrt(8)
    nrem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'total_minutes_nrem']))/math.sqrt(8)
    nrem_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'total_minutes_nrem']))/math.sqrt(8)
    rem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'total_minutes_rem']))/math.sqrt(8)
    rem_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'total_minutes_rem']))/math.sqrt(8)
    rem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'total_minutes_rem']))/math.sqrt(8)
    rem_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'total_minutes_rem']))/math.sqrt(8)

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
    plt.ylabel('Wake (min)', fontsize=12)
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
    plt.savefig(output_path + '/total_time_wake' + '.png', dpi=100)


    total_time_wake = [nrem_wt_pbs_mean, nrem_het_pbs_mean, nrem_het_syn21_mean, nrem_het_syn20_mean]
    average_sd = [nrem_wt_pbs_sd, nrem_het_pbs_sd, nrem_het_syn21_sd, nrem_het_syn20_sd]
    bins = np.arange(4)
    total_time_wake2 = [0, 0, 0, nrem_het_syn20_mean]

    percent_histogram = plt.figure(figsize=(3, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color, edgecolor = 'black', linewidth=1.5)
    ax.bar(bins, total_time_wake2, color = color, edgecolor = '#ff5b00', hatch = '//', linewidth=1.5)
    ax.bar(bins, total_time_wake2, edgecolor = 'black', color='none', zorder=1, linewidth=1.5)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(nrem_wt_pbs))), np.array(nrem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_pbs))), np.array(nrem_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(nrem_het_syn21))), np.array(nrem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(nrem_het_syn20))), np.array(nrem_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('NREM (min)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT', 'PBS', 'SYN21', 'SYN20'])
    plt.xticks(rotation=70)
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
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.35, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_nrem' + '.png', dpi=100)


    total_time_wake = [rem_wt_pbs_mean, rem_het_pbs_mean, rem_het_syn21_mean, rem_het_syn20_mean]
    average_sd = [rem_wt_pbs_sd, rem_het_pbs_sd, rem_het_syn21_sd, rem_het_syn20_sd]
    bins = np.arange(4)
    total_time_wake2 = [0, 0, 0, rem_het_syn20_mean]

    percent_histogram = plt.figure(figsize=(3, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color, edgecolor = 'black', linewidth=1.5)
    ax.bar(bins, total_time_wake2, color = color, edgecolor = '#ff5b00', hatch = '//', linewidth=1.5)
    ax.bar(bins, total_time_wake2, edgecolor = 'black', color='none', zorder=1, linewidth=1.5)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs))), np.array(rem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_pbs))), np.array(rem_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(rem_het_syn21))), np.array(rem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(rem_het_syn20))), np.array(rem_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('REM (min)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT', 'PBS', 'SYN21', 'SYN20'])
    plt.xticks(rotation=70)
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
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.35, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_rem' + '.png', dpi=100)

    return


def plot_average_bout_time(data, output_path):
    df = data.loc[data['period'] == 'total']

    wake_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_wake']
    wake_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_wake']
    wake_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_wake']
    wake_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_wake']
    nrem_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_nrem']
    nrem_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_nrem']
    nrem_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_nrem']
    nrem_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_nrem']
    rem_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_rem']
    rem_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_rem']
    rem_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_rem']
    rem_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_rem']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_wake']))
    wake_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_wake']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_wake']))
    wake_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_wake']))
    nrem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_nrem']))
    nrem_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_nrem']))
    nrem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_nrem']))
    nrem_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_nrem']))
    rem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_rem']))
    rem_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_rem']))
    rem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_rem']))
    rem_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_rem']))

    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_wake']))/math.sqrt(8)
    wake_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_wake']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_wake']))/math.sqrt(8)
    wake_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_wake']))/math.sqrt(8)
    nrem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_nrem']))/math.sqrt(8)
    nrem_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_nrem']))/math.sqrt(8)
    nrem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_nrem']))/math.sqrt(8)
    nrem_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_nrem']))/math.sqrt(8)
    rem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'avg_bout_duration_rem']))/math.sqrt(8)
    rem_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'avg_bout_duration_rem']))/math.sqrt(8)
    rem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_rem']))/math.sqrt(8)
    rem_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'avg_bout_duration_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_mean, wake_het_pbs_mean, wake_het_syn21_mean, wake_het_syn20_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_pbs_sd, wake_het_syn21_sd, wake_het_syn20_sd]
    bins = np.arange(4)

    color = ['#363636', 'mediumseagreen', 'dodgerblue', 'crimson']
    percent_histogram = plt.figure(figsize=(1.5, 2.5))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_pbs))), np.array(wake_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn20))), np.array(wake_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Mean bout duration (seconds)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT - PBS', 'HET - PBS', 'HET - SYN21', 'HET - SYN20'])
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_wake' + '.png', dpi=100)


    total_time_wake = [nrem_wt_pbs_mean, nrem_het_pbs_mean, nrem_het_syn21_mean, nrem_het_syn20_mean]
    average_sd = [nrem_wt_pbs_sd, nrem_het_pbs_sd, nrem_het_syn21_sd, nrem_het_syn20_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 2.5))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(nrem_wt_pbs))), np.array(nrem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_pbs))), np.array(nrem_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(nrem_het_syn21))), np.array(nrem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(nrem_het_syn20))), np.array(nrem_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Mean bout duration (seconds)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT - PBS', 'HET - PBS', 'HET - SYN21', 'HET - SYN20'])
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_nrem' + '.png', dpi=100)


    total_time_wake = [rem_wt_pbs_mean, rem_het_pbs_mean, rem_het_syn21_mean, rem_het_syn20_mean]
    average_sd = [rem_wt_pbs_sd, rem_het_pbs_sd, rem_het_syn21_sd, rem_het_syn20_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 2.5))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs))), np.array(rem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_pbs))), np.array(rem_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(rem_het_syn21))), np.array(rem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(rem_het_syn20))), np.array(rem_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Mean bout duration (seconds)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT - PBS', 'HET - PBS', 'HET - SYN21', 'HET - SYN20'])
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_rem' + '.png', dpi=100)

    return


def plot_average_bouts(data, output_path):
    df = data.loc[data['period'] == 'total']

    wake_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'bout_num_wake']
    wake_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'bout_num_wake']
    wake_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'bout_num_wake']
    wake_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'bout_num_wake']
    nrem_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'bout_num_nrem']
    nrem_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'bout_num_nrem']
    nrem_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'bout_num_nrem']
    nrem_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'bout_num_nrem']
    rem_het_syn21 = df.loc[df['Group'] == 'HET - SYN21', 'bout_num_rem']
    rem_het_syn20 = df.loc[df['Group'] == 'HET - SYN20', 'bout_num_rem']
    rem_wt_pbs = df.loc[df['Group'] == 'WT - PBS', 'bout_num_rem']
    rem_het_pbs = df.loc[df['Group'] == 'HET - PBS', 'bout_num_rem']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'bout_num_wake']))
    wake_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'bout_num_wake']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'bout_num_wake']))
    wake_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'bout_num_wake']))
    nrem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'bout_num_nrem']))
    nrem_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'bout_num_nrem']))
    nrem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'bout_num_nrem']))
    nrem_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'bout_num_nrem']))
    rem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN21', 'bout_num_rem']))
    rem_het_syn20_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - SYN20', 'bout_num_rem']))
    rem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT - PBS', 'bout_num_rem']))
    rem_het_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET - PBS', 'bout_num_rem']))

    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'bout_num_wake']))/math.sqrt(8)
    wake_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'bout_num_wake']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'bout_num_wake']))/math.sqrt(8)
    wake_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'bout_num_wake']))/math.sqrt(8)
    nrem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'bout_num_nrem']))/math.sqrt(8)
    nrem_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'bout_num_nrem']))/math.sqrt(8)
    nrem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'bout_num_nrem']))/math.sqrt(8)
    nrem_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'bout_num_nrem']))/math.sqrt(8)
    rem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN21', 'bout_num_rem']))/math.sqrt(8)
    rem_het_syn20_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - SYN20', 'bout_num_rem']))/math.sqrt(8)
    rem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT - PBS', 'bout_num_rem']))/math.sqrt(8)
    rem_het_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET - PBS', 'bout_num_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_mean, wake_het_pbs_mean, wake_het_syn21_mean, wake_het_syn20_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_pbs_sd, wake_het_syn21_sd, wake_het_syn20_sd]
    bins = np.arange(4)

    color = ['#363636', 'mediumseagreen', 'dodgerblue', 'crimson']
    percent_histogram = plt.figure(figsize=(1.5, 2.5))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_pbs))), np.array(wake_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn20))), np.array(wake_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Wake Bouts (no)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT - PBS', 'HET - PBS', 'HET - SYN21', 'HET - SYN20'])
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_wake' + '.png', dpi=100)


    total_time_wake = [nrem_wt_pbs_mean, nrem_het_pbs_mean, nrem_het_syn21_mean, nrem_het_syn20_mean]
    average_sd = [nrem_wt_pbs_sd, nrem_wt_pbs_sd, nrem_het_syn21_sd, nrem_het_syn20_sd]
    bins = np.arange(4)
    percent_histogram = plt.figure(figsize=(1.5, 2.5))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(nrem_wt_pbs))), np.array(nrem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_pbs))), np.array(nrem_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(nrem_het_syn21))), np.array(nrem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(nrem_het_syn20))), np.array(nrem_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('NREM Bouts (no)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT - PBS', 'HET - PBS', 'HET - SYN21', 'HET - SYN20'])
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_nrem' + '.png', dpi=100)


    total_time_wake = [rem_wt_pbs_mean, rem_het_pbs_mean, rem_het_syn21_mean, rem_het_syn20_mean]
    average_sd = [rem_wt_pbs_sd, rem_het_pbs_sd, rem_het_syn21_sd, rem_het_syn20_sd]
    bins = np.arange(4)
    percent_histogram = plt.figure(figsize=(1.5, 2.5))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs))), np.array(rem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_pbs))), np.array(rem_het_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(rem_het_syn21))), np.array(rem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(rem_het_syn20))), np.array(rem_het_syn20), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('REM Bouts (no)', fontsize=12)
    plt.locator_params(axis='x', nbins=6)
    ax.set_xticklabels(['', 'WT - PBS', 'HET - PBS', 'HET - SYN21', 'HET - SYN20'])
    plt.xticks(rotation=70)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.38, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_rem' + '.png', dpi=100)
    return


def plot_average_time_over_hours(df, output_path):
    wake_het_syn21 = df[(df['Group'] == 'HET - SYN21')]
    wake_het_syn21_mean = np.array(wake_het_syn21.groupby('hour_of_day')['wake_minutes_per_hour'].mean())
    wake_het_syn21_sd = np.array(wake_het_syn21.groupby('hour_of_day')['wake_minutes_per_hour'].sem())
    wake_het_syn20 = df[(df['Group'] == 'HET - SYN20')]
    wake_het_syn20_mean = np.array(wake_het_syn20.groupby('hour_of_day')['wake_minutes_per_hour'].mean())
    wake_het_syn20_sd = np.array(wake_het_syn20.groupby('hour_of_day')['wake_minutes_per_hour'].sem())
    wake_het_pbs = df[(df['Group'] == 'HET - PBS')]
    wake_het_pbs_mean = np.array(wake_het_pbs.groupby('hour_of_day')['wake_minutes_per_hour'].mean())
    wake_het_pbs_sd = np.array(wake_het_pbs.groupby('hour_of_day')['wake_minutes_per_hour'].sem())
    wake_wt_pbs = df[(df['Group'] == 'WT - PBS')]
    wake_wt_pbs_mean = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_minutes_per_hour'].mean())
    wake_wt_pbs_sd = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_minutes_per_hour'].sem())

    nrem_het_syn21 = df[(df['Group'] == 'HET - SYN21')]
    nrem_het_syn21_mean = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_minutes_per_hour'].mean())
    nrem_het_syn21_sd = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_minutes_per_hour'].sem())
    nrem_het_syn20 = df[(df['Group'] == 'HET - SYN20')]
    nrem_het_syn20_mean = np.array(nrem_het_syn20.groupby('hour_of_day')['nrem_minutes_per_hour'].mean())
    nrem_het_syn20_sd = np.array(nrem_het_syn20.groupby('hour_of_day')['nrem_minutes_per_hour'].sem())
    nrem_het_pbs = df[(df['Group'] == 'HET - PBS')]
    nrem_het_pbs_mean = np.array(nrem_het_pbs.groupby('hour_of_day')['nrem_minutes_per_hour'].mean())
    nrem_het_pbs_sd = np.array(nrem_het_pbs.groupby('hour_of_day')['nrem_minutes_per_hour'].sem())
    nrem_wt_pbs = df[(df['Group'] == 'WT - PBS')]
    nrem_wt_pbs_mean = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_minutes_per_hour'].mean())
    nrem_wt_pbs_sd = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_minutes_per_hour'].sem())

    rem_het_syn21 = df[(df['Group'] == 'HET - SYN21')]
    rem_het_syn21_mean = np.array(rem_het_syn21.groupby('hour_of_day')['rem_minutes_per_hour'].mean())
    rem_het_syn21_sd = np.array(rem_het_syn21.groupby('hour_of_day')['rem_minutes_per_hour'].sem())
    rem_het_syn20 = df[(df['Group'] == 'HET - SYN20')]
    rem_het_syn20_mean = np.array(rem_het_syn20.groupby('hour_of_day')['rem_minutes_per_hour'].mean())
    rem_het_syn20_sd = np.array(rem_het_syn20.groupby('hour_of_day')['rem_minutes_per_hour'].sem())
    rem_het_pbs = df[(df['Group'] == 'HET - PBS')]
    rem_het_pbs_mean = np.array(rem_het_pbs.groupby('hour_of_day')['rem_minutes_per_hour'].mean())
    rem_het_pbs_sd = np.array(rem_het_pbs.groupby('hour_of_day')['rem_minutes_per_hour'].sem())
    rem_wt_pbs = df[(df['Group'] == 'WT - PBS')]
    rem_wt_pbs_mean = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_minutes_per_hour'].mean())
    rem_wt_pbs_sd = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_minutes_per_hour'].sem())

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, wake_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_syn21_mean - wake_het_syn21_sd, wake_het_syn21_mean + wake_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, wake_het_syn20_mean, color = "crimson", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_syn20_mean - wake_het_syn20_sd, wake_het_syn20_mean + wake_het_syn20_sd, facecolor='crimson', alpha=0.2)
    ax.plot(bins, wake_het_pbs_mean, color = "mediumseagreen", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_pbs_mean - wake_het_pbs_sd, wake_het_pbs_mean + wake_het_pbs_sd, facecolor='mediumseagreen', alpha=0.2)
    ax.plot(bins, wake_wt_pbs_mean, color = "#363636", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_wt_pbs_mean - wake_wt_pbs_sd, wake_wt_pbs_mean + wake_wt_pbs_sd, facecolor='#363636', alpha=0.2)
    plt.ylabel('Wake (min)', fontsize=12, labelpad=8)
    plt.xlabel('Hours since light on', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=6)
    plt.locator_params(axis='y', nbins=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=15, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_hourly_wake' + '.png', dpi=100)

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, nrem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_syn21_mean - nrem_het_syn21_sd, nrem_het_syn21_mean + nrem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, nrem_het_syn20_mean, color = "crimson", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_syn20_mean - nrem_het_syn20_sd, nrem_het_syn20_mean + nrem_het_syn20_sd, facecolor='crimson', alpha=0.2)
    ax.plot(bins, nrem_het_pbs_mean, color = "mediumseagreen", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_pbs_mean - nrem_het_pbs_sd, nrem_het_pbs_mean + nrem_het_pbs_sd, facecolor='mediumseagreen', alpha=0.2)
    ax.plot(bins, nrem_wt_pbs_mean, color = "#363636", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_wt_pbs_mean - nrem_wt_pbs_sd, nrem_wt_pbs_mean + nrem_wt_pbs_sd, facecolor='#363636', alpha=0.2)
    plt.ylabel('NREM (min)', fontsize=12, labelpad=8)
    plt.xlabel('Hours since light on', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=6)
    plt.locator_params(axis='y', nbins=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-2, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_hourly_nrem' + '.png', dpi=100)


    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, rem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_syn21_mean - rem_het_syn21_sd, rem_het_syn21_mean + rem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, rem_het_syn20_mean, color = "crimson", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_syn20_mean - rem_het_syn20_sd, rem_het_syn20_mean + rem_het_syn20_sd, facecolor='crimson', alpha=0.2)
    ax.plot(bins, rem_het_pbs_mean, color = "mediumseagreen", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_pbs_mean - rem_het_pbs_sd, rem_het_pbs_mean + rem_het_pbs_sd, facecolor='mediumseagreen', alpha=0.2)
    ax.plot(bins, rem_wt_pbs_mean, color = "#363636", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_wt_pbs_mean - rem_wt_pbs_sd, rem_wt_pbs_mean + rem_wt_pbs_sd, facecolor='#363636', alpha=0.2)
    plt.ylabel('REM (min)', fontsize=12, labelpad=8)
    plt.xlabel('Hours since light on', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=6)
    plt.locator_params(axis='y', nbins=5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-1, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_hourly_rem' + '.png', dpi=100)

    return



def plot_average_bouts_over_hours(df, output_path):
    wake_het_syn21 = df[(df['Group'] == 'HET - SYN21')]
    wake_het_syn21_mean = np.array(wake_het_syn21.groupby('hour_of_day')['wake_bout_duration_per_hour'].mean())
    wake_het_syn21_sd = np.array(wake_het_syn21.groupby('hour_of_day')['wake_bout_duration_per_hour'].sem())
    wake_het_syn20 = df[(df['Group'] == 'HET - SYN20')]
    wake_het_syn20_mean = np.array(wake_het_syn20.groupby('hour_of_day')['wake_bout_duration_per_hour'].mean())
    wake_het_syn20_sd = np.array(wake_het_syn20.groupby('hour_of_day')['wake_bout_duration_per_hour'].sem())
    wake_het_pbs = df[(df['Group'] == 'HET - PBS')]
    wake_het_pbs_mean = np.array(wake_het_pbs.groupby('hour_of_day')['wake_bout_duration_per_hour'].mean())
    wake_het_pbs_sd = np.array(wake_het_pbs.groupby('hour_of_day')['wake_bout_duration_per_hour'].sem())
    wake_wt_pbs = df[(df['Group'] == 'WT - PBS')]
    wake_wt_pbs_mean = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_bout_duration_per_hour'].mean())
    wake_wt_pbs_sd = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_bout_duration_per_hour'].sem())

    nrem_het_syn21 = df[(df['Group'] == 'HET - SYN21')]
    nrem_het_syn21_mean = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_bout_duration_per_hour'].mean())
    nrem_het_syn21_sd = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_bout_duration_per_hour'].sem())
    nrem_het_syn20 = df[(df['Group'] == 'HET - SYN20')]
    nrem_het_syn20_mean = np.array(nrem_het_syn20.groupby('hour_of_day')['nrem_bout_duration_per_hour'].mean())
    nrem_het_syn20_sd = np.array(nrem_het_syn20.groupby('hour_of_day')['nrem_bout_duration_per_hour'].sem())
    nrem_het_pbs = df[(df['Group'] == 'HET - PBS')]
    nrem_het_pbs_mean = np.array(nrem_het_pbs.groupby('hour_of_day')['nrem_bout_duration_per_hour'].mean())
    nrem_het_pbs_sd = np.array(nrem_het_pbs.groupby('hour_of_day')['nrem_bout_duration_per_hour'].sem())
    nrem_wt_pbs = df[(df['Group'] == 'WT - PBS')]
    nrem_wt_pbs_mean = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_bout_duration_per_hour'].mean())
    nrem_wt_pbs_sd = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_bout_duration_per_hour'].sem())

    rem_het_syn21 = df[(df['Group'] == 'HET - SYN21')]
    rem_het_syn21_mean = np.array(rem_het_syn21.groupby('hour_of_day')['rem_bout_duration_per_hour'].mean())
    rem_het_syn21_sd = np.array(rem_het_syn21.groupby('hour_of_day')['rem_bout_duration_per_hour'].sem())
    rem_het_syn20 = df[(df['Group'] == 'HET - SYN20')]
    rem_het_syn20_mean = np.array(rem_het_syn20.groupby('hour_of_day')['rem_bout_duration_per_hour'].mean())
    rem_het_syn20_sd = np.array(rem_het_syn20.groupby('hour_of_day')['rem_bout_duration_per_hour'].sem())
    rem_het_pbs = df[(df['Group'] == 'HET - PBS')]
    rem_het_pbs_mean = np.array(rem_het_pbs.groupby('hour_of_day')['rem_bout_duration_per_hour'].mean())
    rem_het_pbs_sd = np.array(rem_het_pbs.groupby('hour_of_day')['rem_bout_duration_per_hour'].sem())
    rem_wt_pbs = df[(df['Group'] == 'WT - PBS')]
    rem_wt_pbs_mean = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_bout_duration_per_hour'].mean())
    rem_wt_pbs_sd = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_bout_duration_per_hour'].sem())

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, wake_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_syn21_mean - wake_het_syn21_sd, wake_het_syn21_mean + wake_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, wake_het_syn20_mean, color = "crimson", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_syn20_mean - wake_het_syn20_sd, wake_het_syn20_mean + wake_het_syn20_sd, facecolor='crimson', alpha=0.2)
    ax.plot(bins, wake_het_pbs_mean, color = "mediumseagreen", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_pbs_mean - wake_het_pbs_sd, wake_het_pbs_mean + wake_het_pbs_sd, facecolor='mediumseagreen', alpha=0.2)
    ax.plot(bins, wake_wt_pbs_mean, color = "#363636", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_wt_pbs_mean - wake_wt_pbs_sd, wake_wt_pbs_mean + wake_wt_pbs_sd, facecolor='#363636', alpha=0.2)
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=8)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-2, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_time_hourly_wake' + '.png', dpi=100)

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, nrem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_syn21_mean - nrem_het_syn21_sd, nrem_het_syn21_mean + nrem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, nrem_het_syn20_mean, color = "crimson", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_syn20_mean - nrem_het_syn20_sd, nrem_het_syn20_mean + nrem_het_syn20_sd, facecolor='crimson', alpha=0.2)
    ax.plot(bins, nrem_het_pbs_mean, color = "mediumseagreen", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_pbs_mean - nrem_het_pbs_sd, nrem_het_pbs_mean + nrem_het_pbs_sd, facecolor='mediumseagreen', alpha=0.2)
    ax.plot(bins, nrem_wt_pbs_mean, color = "#363636", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_wt_pbs_mean - nrem_wt_pbs_sd, nrem_wt_pbs_mean + nrem_wt_pbs_sd, facecolor='#363636', alpha=0.2)
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=8)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-2, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_time_hourly_nrem' + '.png', dpi=100)


    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, rem_het_syn21_mean, color = "crimson", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_syn21_mean - rem_het_syn21_sd, rem_het_syn21_mean + rem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, rem_het_syn20_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_syn20_mean - rem_het_syn20_sd, rem_het_syn20_mean + rem_het_syn20_sd, facecolor='crimson', alpha=0.2)
    ax.plot(bins, rem_het_pbs_mean, color = "mediumseagreen", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_pbs_mean - rem_het_pbs_sd, rem_het_pbs_mean + rem_het_pbs_sd, facecolor='mediumseagreen', alpha=0.2)
    ax.plot(bins, rem_wt_pbs_mean, color = "#363636", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_wt_pbs_mean - rem_wt_pbs_sd, rem_wt_pbs_mean + rem_wt_pbs_sd, facecolor='#363636', alpha=0.2)
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=8)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-7, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_time_hourly_rem' + '.png', dpi=100)

    return



def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    overall_data_path = '/Volumes/Sarah/SYNGAPE8/analysis_all_animals_avg2.csv'
    hourly_data_path = '/Volumes/Sarah/SYNGAPE8/analysis_hour_by_hour_all_animals_avg2.csv'
    output_path = '/Volumes/Sarah/SYNGAPE8/'

    # LOAD DATA
    overall_data = process_dir(overall_data_path) # overall data
    hourly_data = process_dir(hourly_data_path) # overall data

    # BAR GRAPHS
    plot_average_time(overall_data, output_path)

    plot_average_bout_time(overall_data, output_path)

    plot_average_bouts(overall_data, output_path)

    # HOURLY PLOTS
    plot_average_time_over_hours(hourly_data, output_path)
    plot_average_bouts_over_hours(hourly_data, output_path)
    #plot_average_bouts_over_hours(hourly_data, output_path)




if __name__ == '__main__':
    main()


