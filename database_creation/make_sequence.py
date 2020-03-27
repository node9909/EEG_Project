import os
import random
import numpy as np
from shutil import copyfile


# deletes every file in the given folder
def empty_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


cross_type = '4'

load_folder = '..\\database\\labeled_gr'
sequence_folder = '..\\database\\sequence'
cross_path = '..\\database\\cross' + cross_type + '.png'

# delete previous sequence
empty_folder(sequence_folder)

# load the numpy array containing the labels
labels = np.load(load_folder+'\\'+'labels.npy')
image_paths = []
views = []
# get all labeled png files
for root, dirs, files in os.walk(load_folder):
    for file in files:
        if file.endswith(".png"):
            image_paths.append(os.path.join(root, file))

# Shuffle the images along with their labels
lit = list(zip(labels.ravel(order='F'), image_paths))  # ravel() : unravels the labels in a 1-d array
random.shuffle(lit)
labels, image_paths = zip(*lit)
object_name = []

# save the new shuffled labels and views
for i in range(0, len(image_paths)):
    view_int = image_paths[i][len(image_paths[i])-6:len(image_paths[i])-4]  # get the view from the filename
    views.append(int(view_int))
np.save(sequence_folder+'\\labels', labels)
np.save(sequence_folder+'\\views', views)

# Create the sequence of random labeled images
for ind, img in enumerate(image_paths):
    file_name = os.path.basename(img)
    object_name.append(file_name)
    dst = os.path.join(sequence_folder, file_name)
    copyfile(img, dst)
    os.rename(dst, os.path.join(sequence_folder, str(ind) + '.png'))

# add the first cross
copyfile(cross_path, os.path.join(sequence_folder, '-.png'))

# create the list of object names and save it as ndarray
object_name = [''.join(filter(str.isalpha, on[:len(on)-3])) for on in object_name]
np.save(sequence_folder+'\\object_classes', np.asarray(object_name))



