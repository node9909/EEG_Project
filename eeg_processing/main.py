import numpy as np
import utilities
import mne
import matplotlib.pyplot as plt
import os
from mne.preprocessing import ICA, corrmap
from mne.channels.layout import read_layout


subject_folder = "D:\\Apostolis\\Programming\\Python\\Athena_project\\EEG_Project\\data\\subjects"

subjects = os.listdir(subject_folder)
layout = read_layout('EEG1005')
drops = ['TIME_STAMP_s', 'TIME_STAMP_ms', 'COUNTER', 'INTERPOLATED', 'RAW_CQ', 'BATTERY', 'MarkerIndex', 'MarkerType',
         'MarkerValueInt', 'MARKER_HARDWARE', 'CQ_AF3', 'CQ_F7', 'CQ_F3', 'CQ_FC5', 'CQ_T7', 'CQ_P7', 'CQ_O1', 'CQ_O2',
         'CQ_P8', 'CQ_T8', 'CQ_FC6', 'CQ_F4', 'CQ_F8', 'CQ_AF4', 'CQ_CMS', 'STI 014']
for sub in subjects:
    sub_path = os.path.join(subject_folder, sub)

    # Create events
    events = np.load(os.path.join(sub_path, 'events.npy'))
    events = np.insert(events, 1, 0, axis=1).astype(np.uint)
    events[:, 0] = events[:, 0]*128/1000
    event_id = {"correct": 0, "wrong": 2}

    # Read and filter
    edf = os.path.join(sub_path, sub + '.edf')
    edf_data = mne.io.read_raw_edf(edf, preload=True)
    # mne.filter.notch_filter(edf_data, edf_data.info['sfreq'], freqs=50)
    edf_data.drop_channels(drops)
    edf_data.plot(events=events, title=sub)
    edf_data.filter(l_freq=0.2, h_freq=40)

    # ICA stuff
    ica = ICA(n_components=7, random_state=97)
    ica.fit(edf_data)
    ica.plot_sources(edf_data)
    ica.plot_components(layout=layout)

    epochs = mne.Epochs(edf_data, events, event_id=event_id, tmin=-0.5, tmax=1.5, preload=True)
    correct = epochs['correct']
    wrong = epochs['wrong']
    # correct.plot_image()
    # plt.show()
