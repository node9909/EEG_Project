import os
import random
import numpy as np
from shutil import copyfile


load_folder = 'C:\\Users\\User01\\Desktop\\Αποστόλης\\Programming\\Python\\Athena\\Picture_labeling\\pictures' \
              '\\labeled_gr'
sequence_folder = 'C:\\Users\\User01\\Desktop\\Αποστόλης\\Programming\\Python\\Athena\\Picture_labeling\\pictures' \
                  '\\sequence'
cross = 'C:\\Users\\User01\\Desktop\\Αποστόλης\\Programming\\Python\\Athena\\cross.jpg'

labels = np.load(load_folder+'\\'+'labels.npy')
image_paths = []
for root, dirs, files in os.walk(load_folder):
    for file in files:
        if file.endswith(".png"):
            image_paths.append(os.path.join(root, file))

lit = list(zip(labels.ravel(), image_paths))
random.shuffle(lit)

labels, image_paths = zip(*lit)
np.save(sequence_folder+'\\labels', labels)
sequence = ["" for x in range(len(image_paths)*2)]
for j, i in enumerate(range(0, len(image_paths)*2, 2)):
    sequence[i] = image_paths[j]

for ind, img in enumerate(sequence):

    if img:
        file_name = os.path.basename(img)
        dst = os.path.join(sequence_folder, file_name)
        copyfile(img, dst)
        os.rename(dst, os.path.join(sequence_folder, str(ind)+'.png'))
    else:
        copyfile(cross, os.path.join(sequence_folder, str(ind)+'.png'))
