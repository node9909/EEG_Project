import os
import random
import numpy as np
from shutil import copyfile

load_folder = '.\\labeled_gr'
sequence_folder =  '.\\sequence'
cross_path = '.\\cross.png'

# load the numpy array containing the labels
labels = np.load(load_folder+'\\'+'labels.npy')
image_paths = []
# get all labeled png files
for root, dirs, files in os.walk(load_folder):
    for file in files:
        if file.endswith(".png"):
            image_paths.append(os.path.join(root, file))

# Shuffle the images along with their labels
lit = list(zip(labels.ravel(order='F'), image_paths))
random.shuffle(lit)
labels, image_paths = zip(*lit)
object_name = []
# save the new shuffled labels
np.save(sequence_folder+'\\labels', labels)
# the new random sequence of images
sequence = ["" for x in range(len(image_paths)*2)]
# fill the odd indices of sequence with the labeled image paths
for j, i in enumerate(range(0, len(image_paths)*2, 2)):
    sequence[i] = image_paths[j]

# Create the sequence of random labeled images with a cross between each pair of images for the resting period
for ind, img in enumerate(sequence):

    if img:
        file_name = os.path.basename(img)
        object_name.append(file_name)
        dst = os.path.join(sequence_folder, file_name)
        copyfile(img, dst)
        os.rename(dst, os.path.join(sequence_folder, str(ind)+'.png'))
    else:
        copyfile(cross_path, os.path.join(sequence_folder, str(ind)+'.png'))

# create the list of object names and save it as ndarray
object_name = [''.join(filter(str.isalpha, on[:len(on)-3])) for on in object_name]
np.save(sequence_folder+'\\object_classes', np.asarray(object_name))
