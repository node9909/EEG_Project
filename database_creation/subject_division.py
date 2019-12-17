import os
from shutil import copyfile
import numpy as np
from natsort import natsorted

load_folder = '..\\database\\sequence'
save_folder = '..\\database\\subjects'

image_paths = []

# Get paths of all images
for root, dirs, files in os.walk(load_folder):
    for file in files:
        if file.endswith(".png"):
            image_paths.append(os.path.join(root, file))

# Get the cross path
cross_path = image_paths[0]
# Apply natural sorting to the rest image list
image_paths = natsorted(image_paths[1:])

num_obj = len(image_paths)
num_img = 76
num_subj = int(num_obj/num_img)

for i in range(0, num_subj):
    labels = np.load(os.path.join(load_folder, 'labels.npy'))
    object_classes = np.load(os.path.join(load_folder, 'object_classes.npy'))
    views = np.load(os.path.join(load_folder, 'views.npy'))
    dst = os.path.join(save_folder, 'subject_' + str(i))

    if not os.path.exists(dst):
        os.makedirs(dst)

    copyfile(cross_path, os.path.join(dst, '-.png'))
    start = 0 + i*num_img
    for ind, img in enumerate(image_paths[start:start+76]):
        np.save(os.path.join(dst, 'labels'), labels[start:start+76])
        np.save(os.path.join(dst, 'object_classes'), object_classes[start:start+76])
        np.save(os.path.join(dst, 'views'), views[start:start+76])
        copyfile(img, os.path.join(dst, str(ind)+'.png'))
