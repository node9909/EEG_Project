import utilities
import numpy as np
import os
import re
import sys

answer_fol = "..\\..\\data\\answers"
save_fol = "..\\..\\data\\subjects"

answer_files = utilities.get_files(answer_fol)

file = sys.argv[1]
# Get subject names from file name
sub_name = utilities.get_filename(file, start=4)

# Get time zero (t0) of the subject from the info.csv file.
# t0 represents the exact ms that the eeg recording started according to iMotions export file
with open(os.path.join(save_fol, sub_name, 'info.csv')) as csv:
    lines = csv.readlines()
    line = lines[2].split(',')
    t0 = int(re.sub("[^0-9]", "", line[2]))

f = open(file)
text = f.readlines()
f.close()
time_zero = 0
for ind, line in enumerate(text):
    # Search in text for this particular line which marks the start of the web application
    if "NavigateComplete\thttp://localhost/exp/main.php" in line:
        line = text[ind-2].split('\t')
        time_zero = int(line[9])
        break

# Time zero represents the ms of the first cross, thus the first label appears at
# time_zero + 3500ms(cross) + 3500ms(item without label)
labels = list()
labels.append(time_zero + 7000 - t0)
for i in range(1, 39):
    labels.append(labels[i-1] + 10000)

# Get answers from answer files
answer_ind = utilities.search_string_in_list(answer_files, sub_name)
answers = []
if answer_ind or answer_ind == 0:
    with open(answer_files[answer_ind], 'r') as f1:
        txt = f1.readlines()
    # Check if the first line is the dataset name ("subject_1")
    if len(txt) == 3:
        answers = txt[0].split(',')
    else:
        answers = txt[1].split(',')

    # Put answers and labels in one array
    events = np.column_stack([labels, answers])
    events = np.insert(events, 1, 0, axis=1).astype(np.uint)
    events[:, 0] = events[:, 0] * 128 / 1000
    # Save times in a npy file
    np.save(os.path.join(save_fol, sub_name, 'events'), events)
