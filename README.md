## Summary analysis of EEG data 

This script loads a single recording file using the MNE package (v1.6.1) in python (v3.12), performs various calculations and plots data using Matplotlib (v3.8.3). The output files of the script should appear as the figures below saved as a .png into the output folder specified in the script. 

### Abbreviations/meanings : 
swd = spike wave discharge i.e. seizure  
epoch = 5 seconds  
bout = uninterrupted period or episode - calculated by adding consecutive epochs of the same state 


### What the script does:

1. Calculates total time/epochs/percentage the animal spent in each sleep state (wake, nrem, rem, swd) over the 24 hour recording

![total_epochs_per_state](https://github.com/user-attachments/assets/89ea5838-c252-43b2-84fb-e487f67a2252)

2. Calculates total time/epochs/percentage the animal spent in each sleep state (wake, nrem, rem, swd) for each hour of the 24 hour recording

![epochs_per_hour](https://github.com/user-attachments/assets/e47f54fd-1cd7-4198-abb4-ea66932ab5b0)

3. Contains the durations in seconds for each bout/episode of each sleep state (wake, nrem, rem) across the whole recording. I.e. There might be 100 epochs of rem but it could be 10 bouts each 10 epochs long or 2 bouts of 50 epochs long so this is a way to describe the states more than just total time/epochs. 

Note : seizures are not included in this because counting the duration of seizures from epoched data would be inaccurate as some seizures occur within the same epoch and thus are counted as one seizure bout.  

![average_bout_duration](https://github.com/user-attachments/assets/af692216-ceb7-4b77-8014-a7e5b1071204)

4. Same as above but for every hour of the recording.

![bout_duration_per_hour](https://github.com/user-attachments/assets/e8e659fc-6acc-40cf-8e5e-8627c7ea8ecc)

5. The number of seizures in each duration bin (1 second bins over 60 seconds)

![seizure_durations](https://github.com/user-attachments/assets/7be87343-892a-4838-9cd9-8474d8658d67)

6. Number of seizures over each hour of the 24 hour recording

![seizure_start_times](https://github.com/user-attachments/assets/8fed67fc-6392-4c70-8111-3c5458436755)


### Instructions:

1. Navigate to the main function in the Control_Post_Analysis.py script and enter the .csv file that contains the sleep score for the animal you want to analyse

```ruby
sleep_state_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/SYNGAPE8_3131_BL1-dge_swd.csv'
```

2. In the line underneath, enter the path to the .csv file that contains the start and end times of each seizure and the seizure durations 

```ruby
seizure_times_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_3131/24h/seiz/SYNGAPE8_3131_BL1_Seizures.csv'
```

3. Edit the output path to the desired folder you want to save the output figure into 

```ruby
output_figure_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_2780/'
```

4. Run the Control_Post_Analysis.py script

5. To change the color scheme in any plot, simply navigate to the plot and edit the color mapping i.e for plots which are not stacked such as total epochs across the whole recording, edit the following line to the preferred colors 

```ruby
color = ['LightSkyBlue', 'DodgerBlue', 'Blue']
```

If a stacked plot, the colours are added in the plt.bar() line of code and can be changed to the preferred colours.

```ruby
ax.bar(bins, rem, color = "Blue")
ax.bar(bins, nrem, bottom = rem, color = "DodgerBlue")
ax.bar(bins, wake, bottom = rem + nrem, color = "LightSkyBlue")
```

6. To change the output name of .png files, navigate to the plt.savefig() line of code for the given plot and change the given name.

```ruby
plt.savefig(output_path + '/bout_duration_per_hour' + '.png', dpi=200)
```





