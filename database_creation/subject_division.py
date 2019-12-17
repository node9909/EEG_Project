import os
from shutil import copyfile

load_folder = '..\\database\\sequence'
save_folder = '..\\database\\subjects'

image_paths = []

for root, dirs, files in os.walk(load_folder):
    for file in files:
        if file.endswith(".png"):
            image_paths.append(os.path.join(root, file))

num_obj = len(image_paths) - 1
num_img = 76
num_subj = int(num_obj/num_img)

for i in range(0, num_subj):

    dst = os.path.join(save_folder, 'subject_' + str(i))

    if not os.path.exists(dst):
        os.makedirs(dst)

    copyfile(image_paths[0], os.path.join(dst, '-.png'))
    start = 1 + i*num_img
    for ind, img in enumerate(image_paths[start:start+76]):
        copyfile(img, os.path.join(dst, str(ind)+'.png'))
