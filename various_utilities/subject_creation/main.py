import os
import utilities
from shutil import copy
import csv
import numpy as np

# Get current answer files
ans_fol = "..\\..\\data\\answers"
ans_paths = utilities.get_files(ans_fol)
subs = [utilities.get_filename(i) for i in ans_paths]

# Get export files (iMotion file)
exp_fol = "..\\..\\data\\export"
exp_paths = utilities.get_files(exp_fol)

# Create subject folders if they do not exist
sub_fol = "..\\..\\data\\subjects"
for ans_path, sub in zip(ans_paths, subs):
    folder = os.path.join(sub_fol, sub)

    # Check if folder already exists
    if not os.path.isdir(folder):
        # Create folder
        os.mkdir(folder)

        # Copy answer file to subject folder
        copy(ans_path, os.path.join(folder, 'answers.txt'))

        # Find and copy the correct export file to subject folder
        exp_ind = utilities.search_string_in_list(exp_paths, sub)
        copy(exp_paths[exp_ind], os.path.join(folder, 'export.txt'))

        # Create info file
        with open(os.path.join(folder, 'info.csv'), mode='w') as csv_file:

            # Load datasets and t0s and get the corresponding index of the subject
            datasets = np.load('..\\..\\data\\datasets.npy')
            d_ind = utilities.search_string_in_list(datasets, sub)
            time_zero = np.load('..\\..\\data\\eeg_t0.npy')
            t_ind = utilities.search_string_in_list(time_zero, sub)

            # Write to the info file
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(['Subject', 'Dataset', 'Time zero'])
            csv_writer.writerow([sub, datasets[d_ind][1], time_zero[t_ind][1]])

        # Run event creator
        exp_file = exp_paths[exp_ind]
        print(exp_file)
        os.system('conda activate mne & python event_detector.py %s' % exp_file)

        # Get edf and csv files
        edf_files = utilities.get_files('..\\..\\data\\eeg', 'edf')[0::2]
        csv_files = utilities.get_files('..\\..\\data\\eeg', 'csv')

        # Names.npy contains the subject names along with their edf and csv file names
        names = np.load('..\\..\\data\\names.npy')
        ind = utilities.search_string_in_list(names, sub)
        edf_ind = utilities.search_string_in_list(edf_files, names[ind, 0])
        csv_ind = utilities.search_string_in_list(csv_files, names[ind, 0])
        copy(edf_files[edf_ind], folder)
        copy(csv_files[csv_ind], folder)

