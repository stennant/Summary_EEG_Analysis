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


def process_dir(file_path):
    # Load sleep state score from .csv
    data = pd.read_csv(file_path, delimiter=",") # read .csv file with sleep score
    return data

def plot_average_time(data, output_path):
    df = data.loc[data['period'] == 'total']

    wake_het_syn21 = df.loc[df['Group'] == 'HET', 'total_minutes_wake']
    wake_wt_pbs = df.loc[df['Group'] == 'WT', 'total_minutes_wake']
    nrem_het_syn21 = df.loc[df['Group'] == 'HET', 'total_minutes_nrem']
    nrem_wt_pbs = df.loc[df['Group'] == 'WT', 'total_minutes_nrem']
    rem_het_syn21 = df.loc[df['Group'] == 'HET', 'total_minutes_rem']
    rem_wt_pbs = df.loc[df['Group'] == 'WT', 'total_minutes_rem']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_wake']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_wake']))
    nrem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_nrem']))
    nrem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_nrem']))
    rem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_rem']))
    rem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_rem']))

    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_wake']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_wake']))/math.sqrt(8)
    nrem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_nrem']))/math.sqrt(8)
    nrem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_nrem']))/math.sqrt(8)
    rem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_rem']))/math.sqrt(8)
    rem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_mean, wake_het_syn21_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_syn21_sd]
    bins = np.arange(2)

    #color = ['OrangeRed', 'PeachPuff', 'SandyBrown', 'dimgrey']
    color = ['black', 'dodgerblue']

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color, alpha=0.8)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_wake' + '.png', dpi=100)


    total_time_wake = [nrem_wt_pbs_mean, nrem_het_syn21_mean]
    average_sd = [nrem_wt_pbs_sd, nrem_het_syn21_sd]
    bins = np.arange(2)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(nrem_wt_pbs))), np.array(nrem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_syn21))), np.array(nrem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_nrem' + '.png', dpi=100)


    total_time_wake = [rem_wt_pbs_mean, rem_het_syn21_mean]
    average_sd = [rem_wt_pbs_sd, rem_het_syn21_sd]
    bins = np.arange(2)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs))), np.array(rem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_syn21))), np.array(rem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_rem' + '.png', dpi=100)

    return


def plot_average_time_light_and_dark(data, output_path):
    df = data.loc[data['period'] == 'light']

    wake_het_syn21_light = df.loc[df['Group'] == 'HET', 'total_minutes_wake']
    wake_wt_pbs_light = df.loc[df['Group'] == 'WT', 'total_minutes_wake']
    nrem_het_syn21_light = df.loc[df['Group'] == 'HET', 'total_minutes_nrem']
    nrem_wt_pbs_light = df.loc[df['Group'] == 'WT', 'total_minutes_nrem']
    rem_het_syn21_light = df.loc[df['Group'] == 'HET', 'total_minutes_rem']
    rem_wt_pbs_light = df.loc[df['Group'] == 'WT', 'total_minutes_rem']

    wake_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_wake']))
    wake_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_wake']))
    nrem_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_nrem']))
    nrem_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_nrem']))
    rem_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_rem']))
    rem_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_rem']))

    wake_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_wake']))/math.sqrt(8)
    wake_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_wake']))/math.sqrt(8)
    nrem_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_nrem']))/math.sqrt(8)
    nrem_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_nrem']))/math.sqrt(8)
    rem_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_rem']))/math.sqrt(8)
    rem_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_rem']))/math.sqrt(8)



    df = data.loc[data['period'] == 'dark']

    wake_het_syn21_dark = df.loc[df['Group'] == 'HET', 'total_minutes_wake']
    wake_wt_pbs_dark = df.loc[df['Group'] == 'WT', 'total_minutes_wake']
    nrem_het_syn21_dark = df.loc[df['Group'] == 'HET', 'total_minutes_nrem']
    nrem_wt_pbs_dark = df.loc[df['Group'] == 'WT', 'total_minutes_nrem']
    rem_het_syn21_dark = df.loc[df['Group'] == 'HET', 'total_minutes_rem']
    rem_wt_pbs_dark = df.loc[df['Group'] == 'WT', 'total_minutes_rem']

    wake_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_wake']))
    wake_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_wake']))
    nrem_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_nrem']))
    nrem_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_nrem']))
    rem_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_rem']))
    rem_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_rem']))

    wake_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_wake']))/math.sqrt(8)
    wake_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_wake']))/math.sqrt(8)
    nrem_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_nrem']))/math.sqrt(8)
    nrem_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_nrem']))/math.sqrt(8)
    rem_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'total_minutes_rem']))/math.sqrt(8)
    rem_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'total_minutes_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_light_mean, wake_het_syn21_light_mean,
                       wake_wt_pbs_dark_mean, wake_het_syn21_dark_mean]
    average_sd = [wake_wt_pbs_light_sd, wake_het_syn21_light_sd,
                  wake_wt_pbs_dark_sd, wake_het_syn21_dark_sd]
    bins = np.arange(4)

    color = ['black', 'dodgerblue', 'black', 'dodgerblue']

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs_light))), np.array(wake_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_syn21_light))), np.array(wake_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_wt_pbs_dark))), np.array(wake_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn21_dark))), np.array(wake_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=640, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_wake_lightdark' + '.png', dpi=100)


    total_time_nrem = [nrem_wt_pbs_light_mean, nrem_het_syn21_light_mean,
                       nrem_wt_pbs_dark_mean, nrem_het_syn21_dark_mean]
    average_sd = [nrem_wt_pbs_light_sd, nrem_het_syn21_light_sd,
                  nrem_wt_pbs_dark_sd, nrem_het_syn21_dark_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 4))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_nrem, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(nrem_wt_pbs_light))), np.array(nrem_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_syn21_light))), np.array(nrem_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(nrem_wt_pbs_dark))), np.array(nrem_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(nrem_het_syn21_dark))), np.array(nrem_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_nrem, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=390, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_nrem_lightdark' + '.png', dpi=100)


    total_time_rem = [rem_wt_pbs_light_mean, rem_het_syn21_light_mean,
                       rem_wt_pbs_dark_mean, rem_het_syn21_dark_mean]
    average_sd = [rem_wt_pbs_light_sd, rem_het_syn21_light_sd,
                  rem_wt_pbs_dark_sd, rem_het_syn21_dark_sd]
    bins = np.arange(4)
    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_rem, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs_light))), np.array(rem_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_syn21_light))), np.array(rem_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(rem_wt_pbs_dark))), np.array(rem_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(rem_het_syn21_dark))), np.array(rem_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_rem, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=70, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_rem_lightdark' + '.png', dpi=100)

    return


def plot_average_bout_time(data, output_path):
    df = data.loc[data['period'] == 'total']

    wake_het_syn21 = df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']
    wake_wt_pbs = df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']
    nrem_het_syn21 = df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']
    nrem_wt_pbs = df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']
    rem_het_syn21 = df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']
    rem_wt_pbs = df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']))
    nrem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']))
    nrem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']))
    rem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']))
    rem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']))

    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']))/math.sqrt(8)
    nrem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']))/math.sqrt(8)
    nrem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']))/math.sqrt(8)
    rem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']))/math.sqrt(8)
    rem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_mean, wake_het_syn21_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_syn21_sd]
    bins = np.arange(2)

    color = ['black', 'dodgerblue']
    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.7, high=0.3, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.7, high=1.3, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_wake' + '.png', dpi=100)


    total_time_wake = [nrem_wt_pbs_mean, nrem_het_syn21_mean]
    average_sd = [nrem_wt_pbs_sd, nrem_het_syn21_sd]
    bins = np.arange(2)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.7, high=0.3, size=(len(nrem_wt_pbs))), np.array(nrem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.7, high=1.3, size=(len(nrem_het_syn21))), np.array(nrem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_nrem' + '.png', dpi=100)


    total_time_wake = [rem_wt_pbs_mean, rem_het_syn21_mean]
    average_sd = [rem_wt_pbs_sd, rem_het_syn21_sd]
    bins = np.arange(2)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.7, high=0.3, size=(len(rem_wt_pbs))), np.array(rem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.7, high=1.3, size=(len(rem_het_syn21))), np.array(rem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_rem' + '.png', dpi=100)

    return


def plot_average_bout_time_light_and_dark(data, output_path):
    df = data.loc[data['period'] == 'light']

    wake_het_syn21_light = df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']
    wake_wt_pbs_light = df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']
    nrem_het_syn21_light = df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']
    nrem_wt_pbs_light = df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']
    rem_het_syn21_light = df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']
    rem_wt_pbs_light = df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']

    wake_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']))
    wake_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']))
    nrem_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']))
    nrem_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']))
    rem_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']))
    rem_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']))

    wake_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']))/math.sqrt(8)
    wake_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']))/math.sqrt(8)
    nrem_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']))/math.sqrt(8)
    nrem_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']))/math.sqrt(8)
    rem_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']))/math.sqrt(8)
    rem_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']))/math.sqrt(8)



    df = data.loc[data['period'] == 'dark']

    wake_het_syn21_dark = df.loc[df['Group'] == 'HET - UPV-AAV9/SYN21', 'avg_bout_duration_wake']
    wake_wt_pbs_dark = df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_wake']
    nrem_het_syn21_dark = df.loc[df['Group'] == 'HET - UPV-AAV9/SYN21', 'avg_bout_duration_nrem']
    nrem_wt_pbs_dark = df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_nrem']
    rem_het_syn21_dark = df.loc[df['Group'] == 'HET - UPV-AAV9/SYN21', 'avg_bout_duration_rem']
    rem_wt_pbs_dark = df.loc[df['Group'] == 'WT - PBS', 'avg_bout_duration_rem']

    wake_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']))
    wake_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']))
    nrem_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']))
    nrem_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']))
    rem_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']))
    rem_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']))

    wake_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_wake']))/math.sqrt(8)
    wake_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_wake']))/math.sqrt(8)
    nrem_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_nrem']))/math.sqrt(8)
    nrem_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_nrem']))/math.sqrt(8)
    rem_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'avg_bout_duration_rem']))/math.sqrt(8)
    rem_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'avg_bout_duration_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_light_mean, wake_het_syn21_light_mean,
                       wake_wt_pbs_dark_mean, wake_het_syn21_dark_mean]
    average_sd = [wake_wt_pbs_light_sd, wake_het_syn21_light_sd,
                  wake_wt_pbs_dark_sd, wake_het_syn21_dark_sd]
    bins = np.arange(4)

    color = ['black', 'dodgerblue', 'black', 'dodgerblue']

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs_light))), np.array(wake_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_syn21_light))), np.array(wake_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_wt_pbs_dark))), np.array(wake_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn21_dark))), np.array(wake_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=600, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_wake_lightdark' + '.png', dpi=100)


    total_time_nrem = [nrem_wt_pbs_light_mean, nrem_het_syn21_light_mean,
                       nrem_wt_pbs_dark_mean, nrem_het_syn21_dark_mean]
    average_sd = [nrem_wt_pbs_light_sd, nrem_het_syn21_light_sd,
                  nrem_wt_pbs_dark_sd, nrem_het_syn21_dark_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_nrem, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(nrem_wt_pbs_light))), np.array(nrem_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_syn21_light))), np.array(nrem_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(nrem_wt_pbs_dark))), np.array(nrem_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(nrem_het_syn21_dark))), np.array(nrem_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_nrem, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=210, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_nrem_lightdark' + '.png', dpi=100)


    total_time_rem = [rem_wt_pbs_light_mean, rem_het_syn21_light_mean,
                       rem_wt_pbs_dark_mean, rem_het_syn21_dark_mean]
    average_sd = [rem_wt_pbs_light_sd, rem_het_syn21_light_sd,
                  rem_wt_pbs_dark_sd, rem_het_syn21_dark_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_rem, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs_light))), np.array(rem_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_syn21_light))), np.array(rem_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(rem_wt_pbs_dark))), np.array(rem_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(rem_het_syn21_dark))), np.array(rem_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_rem, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=70, xmin =0.518, xmax=1, color='k', linewidth=10, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/avg_bout_time_rem_lightdark' + '.png', dpi=100)

    return


def plot_average_bouts(data, output_path):
    df = data.loc[data['period'] == 'total']

    wake_het_syn21 = df.loc[df['Group'] == 'HET', 'bout_num_wake']
    wake_wt_pbs = df.loc[df['Group'] == 'WT', 'bout_num_wake']
    nrem_het_syn21 = df.loc[df['Group'] == 'HET', 'bout_num_nrem']
    nrem_wt_pbs = df.loc[df['Group'] == 'WT', 'bout_num_nrem']
    rem_het_syn21 = df.loc[df['Group'] == 'HET', 'bout_num_rem']
    rem_wt_pbs = df.loc[df['Group'] == 'WT', 'bout_num_rem']

    wake_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_wake']))
    wake_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_wake']))
    nrem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_nrem']))
    nrem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_nrem']))
    rem_het_syn21_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_rem']))
    rem_wt_pbs_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_rem']))

    wake_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_wake']))/math.sqrt(8)
    wake_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_wake']))/math.sqrt(8)
    nrem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_nrem']))/math.sqrt(8)
    nrem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_nrem']))/math.sqrt(8)
    rem_het_syn21_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_rem']))/math.sqrt(8)
    rem_wt_pbs_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_mean, wake_het_syn21_mean]
    average_sd = [wake_wt_pbs_sd, wake_het_syn21_sd]
    bins = np.arange(2)

    color = ['black', 'dodgerblue']
    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.7, high=0.3, size=(len(wake_wt_pbs))), np.array(wake_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.7, high=1.3, size=(len(wake_het_syn21))), np.array(wake_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout number', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_wake' + '.png', dpi=100)


    total_time_wake = [nrem_wt_pbs_mean, nrem_het_syn21_mean]
    average_sd = [nrem_wt_pbs_sd, nrem_het_syn21_sd]
    bins = np.arange(2)
    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.7, high=0.3, size=(len(nrem_wt_pbs))), np.array(nrem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.7, high=1.3, size=(len(nrem_het_syn21))), np.array(nrem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout number', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_nrem' + '.png', dpi=100)


    total_time_wake = [rem_wt_pbs_mean, rem_het_syn21_mean]
    average_sd = [rem_wt_pbs_sd, rem_het_syn21_sd]
    bins = np.arange(2)
    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.7, high=0.3, size=(len(rem_wt_pbs))), np.array(rem_wt_pbs), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.7, high=1.3, size=(len(rem_het_syn21))), np.array(rem_het_syn21), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout number', fontsize=12, labelpad=1)
    plt.locator_params(axis='x', nbins=3)
    ax.set_xticklabels(['', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_rem' + '.png', dpi=100)
    return


def plot_average_bouts_light_and_dark(data, output_path):
    df = data.loc[data['period'] == 'light']

    wake_het_syn21_light = df.loc[df['Group'] == 'HET', 'bout_num_wake']
    wake_wt_pbs_light = df.loc[df['Group'] == 'WT', 'bout_num_wake']
    nrem_het_syn21_light = df.loc[df['Group'] == 'HET', 'bout_num_nrem']
    nrem_wt_pbs_light = df.loc[df['Group'] == 'WT', 'bout_num_nrem']
    rem_het_syn21_light = df.loc[df['Group'] == 'HET', 'bout_num_rem']
    rem_wt_pbs_light = df.loc[df['Group'] == 'WT', 'bout_num_rem']

    wake_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_wake']))
    wake_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_wake']))
    nrem_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_nrem']))
    nrem_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_nrem']))
    rem_het_syn21_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_rem']))
    rem_wt_pbs_light_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_rem']))

    wake_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_wake']))/math.sqrt(8)
    wake_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_wake']))/math.sqrt(8)
    nrem_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_nrem']))/math.sqrt(8)
    nrem_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_nrem']))/math.sqrt(8)
    rem_het_syn21_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_rem']))/math.sqrt(8)
    rem_wt_pbs_light_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_rem']))/math.sqrt(8)



    df = data.loc[data['period'] == 'dark']

    wake_het_syn21_dark = df.loc[df['Group'] == 'HET', 'bout_num_wake']
    wake_wt_pbs_dark = df.loc[df['Group'] == 'WT', 'bout_num_wake']
    nrem_het_syn21_dark = df.loc[df['Group'] == 'HET', 'bout_num_nrem']
    nrem_wt_pbs_dark = df.loc[df['Group'] == 'WT', 'bout_num_nrem']
    rem_het_syn21_dark = df.loc[df['Group'] == 'HET', 'bout_num_rem']
    rem_wt_pbs_dark = df.loc[df['Group'] == 'WT', 'bout_num_rem']

    wake_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_wake']))
    wake_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_wake']))
    nrem_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_nrem']))
    nrem_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_nrem']))
    rem_het_syn21_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'HET', 'bout_num_rem']))
    rem_wt_pbs_dark_mean = np.nanmean(np.array(df.loc[df['Group'] == 'WT', 'bout_num_rem']))

    wake_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_wake']))/math.sqrt(8)
    wake_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_wake']))/math.sqrt(8)
    nrem_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_nrem']))/math.sqrt(8)
    nrem_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_nrem']))/math.sqrt(8)
    rem_het_syn21_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'HET', 'bout_num_rem']))/math.sqrt(8)
    rem_wt_pbs_dark_sd = np.nanstd(np.array(df.loc[df['Group'] == 'WT', 'bout_num_rem']))/math.sqrt(8)

    total_time_wake = [wake_wt_pbs_light_mean, wake_het_syn21_light_mean,
                       wake_wt_pbs_dark_mean, wake_het_syn21_dark_mean]
    average_sd = [wake_wt_pbs_light_sd, wake_het_syn21_light_sd,
                  wake_wt_pbs_dark_sd, wake_het_syn21_dark_sd]
    bins = np.arange(4)

    color = ['black', 'dodgerblue', 'black', 'dodgerblue']

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_wake, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(wake_wt_pbs_light))), np.array(wake_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(wake_het_syn21_light))), np.array(wake_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(wake_wt_pbs_dark))), np.array(wake_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(wake_het_syn21_dark))), np.array(wake_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_wake, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout number', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=240, xmin =0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_wake_lightdark' + '.png', dpi=100)


    total_time_nrem = [nrem_wt_pbs_light_mean, nrem_het_syn21_light_mean,
                       nrem_wt_pbs_dark_mean, nrem_het_syn21_dark_mean]
    average_sd = [nrem_wt_pbs_light_sd, nrem_het_syn21_light_sd,
                  nrem_wt_pbs_dark_sd, nrem_het_syn21_dark_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_nrem, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=1.2, size=(len(nrem_wt_pbs_light))), np.array(nrem_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(nrem_het_syn21_light))), np.array(nrem_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(nrem_wt_pbs_dark))), np.array(nrem_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(nrem_het_syn21_dark))), np.array(nrem_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_nrem, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout number', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=250, xmin =0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_nrem_lightdark' + '.png', dpi=100)


    total_time_rem = [rem_wt_pbs_light_mean, rem_het_syn21_light_mean,
                       rem_wt_pbs_dark_mean, rem_het_syn21_dark_mean]
    average_sd = [rem_wt_pbs_light_sd, rem_het_syn21_light_sd,
                  rem_wt_pbs_dark_sd, rem_het_syn21_dark_sd]
    bins = np.arange(4)

    percent_histogram = plt.figure(figsize=(1.5, 3))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.bar(bins, total_time_rem, color = color)
    ax.scatter(np.random.uniform(low=-0.2, high=0.2, size=(len(rem_wt_pbs_light))), np.array(rem_wt_pbs_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=0.8, high=1.2, size=(len(rem_het_syn21_light))), np.array(rem_het_syn21_light), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=1.8, high=2.2, size=(len(rem_wt_pbs_dark))), np.array(rem_wt_pbs_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    ax.scatter(np.random.uniform(low=2.8, high=3.2, size=(len(rem_het_syn21_dark))), np.array(rem_het_syn21_dark), edgecolors = "black", facecolors='white', linestyle='None', s=16)
    plt.errorbar(bins, total_time_rem, average_sd, fmt='none', ls='', marker='o', capsize=5, capthick=1, ecolor='black')
    plt.ylabel('Bout number', fontsize=12, labelpad=1)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        labelsize=8, length=5, width=1.5)
    plt.locator_params(axis='x', nbins=5)
    ax.set_xticklabels(['', 'WT', 'HET', 'WT', 'HET'])
    plt.xticks(rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    plt.axhline(y=70, xmin =0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color = 'White')
    ax.xaxis.set_ticks_position('bottom')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.2, left=0.4, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_num_rem_lightdark' + '.png', dpi=100)

    return


def plot_average_time_over_hours(df, output_path):
    wake_het_syn21 = df[(df['Group'] == 'HET')]
    wake_het_syn21_mean = np.array(wake_het_syn21.groupby('hour_of_day')['wake_minutes_per_hour'].mean())
    wake_het_syn21_sd = np.array(wake_het_syn21.groupby('hour_of_day')['wake_minutes_per_hour'].sem())
    wake_wt_pbs = df[(df['Group'] == 'WT')]
    wake_wt_pbs_mean = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_minutes_per_hour'].mean())
    wake_wt_pbs_sd = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_minutes_per_hour'].sem())

    nrem_het_syn21 = df[(df['Group'] == 'HET')]
    nrem_het_syn21_mean = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_minutes_per_hour'].mean())
    nrem_het_syn21_sd = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_minutes_per_hour'].sem())
    nrem_wt_pbs = df[(df['Group'] == 'WT')]
    nrem_wt_pbs_mean = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_minutes_per_hour'].mean())
    nrem_wt_pbs_sd = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_minutes_per_hour'].sem())

    rem_het_syn21 = df[(df['Group'] == 'HET')]
    rem_het_syn21_mean = np.array(rem_het_syn21.groupby('hour_of_day')['rem_minutes_per_hour'].mean())
    rem_het_syn21_sd = np.array(rem_het_syn21.groupby('hour_of_day')['rem_minutes_per_hour'].sem())
    rem_wt_pbs = df[(df['Group'] == 'WT')]
    rem_wt_pbs_mean = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_minutes_per_hour'].mean())
    rem_wt_pbs_sd = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_minutes_per_hour'].sem())

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, wake_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_syn21_mean - wake_het_syn21_sd, wake_het_syn21_mean + wake_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, wake_wt_pbs_mean, color = "black", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_wt_pbs_mean - wake_wt_pbs_sd, wake_wt_pbs_mean + wake_wt_pbs_sd, facecolor='black', alpha=0.2)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=24)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=15, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color='White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_hourly_wake' + '.png', dpi=100)

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, nrem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_syn21_mean - nrem_het_syn21_sd, nrem_het_syn21_mean + nrem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, nrem_wt_pbs_mean, color = "black", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_wt_pbs_mean - nrem_wt_pbs_sd, nrem_wt_pbs_mean + nrem_wt_pbs_sd, facecolor='black', alpha=0.2)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=24)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-5, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color='White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_hourly_nrem' + '.png', dpi=100)


    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, rem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_syn21_mean - rem_het_syn21_sd, rem_het_syn21_mean + rem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, rem_wt_pbs_mean, color = "black", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_wt_pbs_mean - rem_wt_pbs_sd, rem_wt_pbs_mean + rem_wt_pbs_sd, facecolor='black', alpha=0.2)
    plt.ylabel('Total time (minutes)', fontsize=12, labelpad=10)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=24)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-1, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color='White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/total_time_hourly_rem' + '.png', dpi=100)

    return



def plot_average_bouts_over_hours(df, output_path):
    wake_het_syn21 = df[(df['Group'] == 'HET')]
    wake_het_syn21_mean = np.array(wake_het_syn21.groupby('hour_of_day')['wake_bout_duration_per_hour'].mean())
    wake_het_syn21_sd = np.array(wake_het_syn21.groupby('hour_of_day')['wake_bout_duration_per_hour'].sem())
    wake_wt_pbs = df[(df['Group'] == 'WT')]
    wake_wt_pbs_mean = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_bout_duration_per_hour'].mean())
    wake_wt_pbs_sd = np.array(wake_wt_pbs.groupby('hour_of_day')['wake_bout_duration_per_hour'].sem())

    nrem_het_syn21 = df[(df['Group'] == 'HET')]
    nrem_het_syn21_mean = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_bout_duration_per_hour'].mean())
    nrem_het_syn21_sd = np.array(nrem_het_syn21.groupby('hour_of_day')['nrem_bout_duration_per_hour'].sem())
    nrem_wt_pbs = df[(df['Group'] == 'WT')]
    nrem_wt_pbs_mean = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_bout_duration_per_hour'].mean())
    nrem_wt_pbs_sd = np.array(nrem_wt_pbs.groupby('hour_of_day')['nrem_bout_duration_per_hour'].sem())

    rem_het_syn21 = df[(df['Group'] == 'HET')]
    rem_het_syn21_mean = np.array(rem_het_syn21.groupby('hour_of_day')['rem_bout_duration_per_hour'].mean())
    rem_het_syn21_sd = np.array(rem_het_syn21.groupby('hour_of_day')['rem_bout_duration_per_hour'].sem())
    rem_wt_pbs = df[(df['Group'] == 'WT')]
    rem_wt_pbs_mean = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_bout_duration_per_hour'].mean())
    rem_wt_pbs_sd = np.array(rem_wt_pbs.groupby('hour_of_day')['rem_bout_duration_per_hour'].sem())

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, wake_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_het_syn21_mean - wake_het_syn21_sd, wake_het_syn21_mean + wake_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, wake_wt_pbs_mean, color = "black", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, wake_wt_pbs_mean - wake_wt_pbs_sd, wake_wt_pbs_mean + wake_wt_pbs_sd, facecolor='black', alpha=0.2)
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=10)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=24)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-5, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color='White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_time_hourly_wake' + '.png', dpi=100)

    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, nrem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_het_syn21_mean - nrem_het_syn21_sd, nrem_het_syn21_mean + nrem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, nrem_wt_pbs_mean, color = "black", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, nrem_wt_pbs_mean - nrem_wt_pbs_sd, nrem_wt_pbs_mean + nrem_wt_pbs_sd, facecolor='black', alpha=0.2)
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=10)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=24)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-5, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color='White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_time_hourly_nrem' + '.png', dpi=100)


    bins = np.arange(24)
    percent_histogram = plt.figure(figsize=(4, 2))
    ax = percent_histogram.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
    ax.plot(bins, rem_het_syn21_mean, color = "dodgerblue", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_het_syn21_mean - rem_het_syn21_sd, rem_het_syn21_mean + rem_het_syn21_sd, facecolor='dodgerblue', alpha=0.2)
    ax.plot(bins, rem_wt_pbs_mean, color = "black", markersize = 2, marker = 'o', linewidth=1)
    ax.fill_between(bins, rem_wt_pbs_mean - rem_wt_pbs_sd, rem_wt_pbs_mean + rem_wt_pbs_sd, facecolor='black', alpha=0.2)
    plt.ylabel('Bout time (seconds)', fontsize=12, labelpad=10)
    plt.xlabel('Time since light on (hours)', fontsize=10, labelpad=5)
    plt.locator_params(axis='x', nbins=24)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.axhline(y=-5, xmin=0.518, xmax=1, color='k', linewidth=5, alpha=0.85, zorder=0)
    #text(0.25, 0.95, 'Light', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes)
    #text(0.75, 0.95, 'Dark', horizontalalignment='center',
         #verticalalignment='center', transform=ax.transAxes, color='White')
    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.25, left=0.2, right=0.87, top=0.92)
    plt.savefig(output_path + '/bout_time_hourly_rem' + '.png', dpi=100)

    return



def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    overall_data_path = '/Volumes/Sarah/GNU/analysis_all_animals.csv'
    hourly_data_path = '/Volumes/Sarah/GNU/analysis_hour_by_hour_all_animals.csv'
    output_path = '/Volumes/Sarah/GNU/'

    # LOAD DATA
    overall_data = process_dir(overall_data_path) # overall data
    hourly_data = process_dir(hourly_data_path) # overall data

    # BAR GRAPHS
    plot_average_time(overall_data, output_path)
    plot_average_time_light_and_dark(overall_data, output_path)

    plot_average_bout_time(overall_data, output_path)
    plot_average_bout_time_light_and_dark(overall_data, output_path)

    plot_average_bouts(overall_data, output_path)
    plot_average_bouts_light_and_dark(overall_data, output_path)

    # HOURLY PLOTS
    plot_average_time_over_hours(hourly_data, output_path)
    plot_average_bouts_over_hours(hourly_data, output_path)
    #plot_average_bouts_over_hours(hourly_data, output_path)




if __name__ == '__main__':
    main()


