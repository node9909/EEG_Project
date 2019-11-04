import os
from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np


def get_name(folder_path):
    # d, pnf = os.path.splitdrive(folder_path)
    parts = os.path.normpath(folder_path).split(os.path.sep)
    return parts[len(parts)-2]


load_folder = '.\\true'
# load_folder = 'C:\\Users\\User01\\Desktop\\Αποστόλης\\Programming\\Python\\Athena\\Picture_labeling\\pictures\\test'
save_folder = '.\\labeled_gr'

object_folders = [x for x, _, _ in os.walk(load_folder)]

# test folders occur every 2 folders
test_folders = [object_folders[i] for i in range(2, len(object_folders), 2)]

# stores the answer to the question: "Is the label correct?"
correct = np.zeros(shape=(20, len(test_folders)), dtype=np.bool)

# object names: 'airplane', 'bottle', ... 'xbox'
labels = [get_name(path) for path in test_folders]

# transform names like tv_stand to tv stand
labels = [l.replace('_', ' ') for l in labels]

labels_gr = ['Αεροπλάνο', 'Μπανιέρα', 'Κρεβάτι', 'Παγκάκι', 'Βιβλιοθήκη', 'Μπουκάλι', 'Μπολ', 'Αυτοκίνητο', 'Καρέκλα',
             'Κόνος', 'Κούπα', 'Κουρτίνα', 'Γραφείο', 'Πόρτα', 'Συρταριέρα', 'Βάζο λουλουδιών', 'Γυάλινο κουτί',
             'Κιθάρα', 'Πληκτρολόγιο', 'Λάμπα', 'Λάπτοπ', 'Οθόνη', 'Κομοδίνο', 'Άνθρωπος', 'Πιάνο', 'Φυτό', 'Ράδιο',
             'Νεροχύτης', 'Καναπές', 'Σκάλες', 'Σκαμπό', 'Τραπέζι', 'Σκηνή', 'Τουαλέτα', 'Έπιπλο τηλεόρασης',
             'Βάζο', 'Ντουλάπα', 'Xbox']

im_size = (1024, 1024)
box_height = round(1/3*im_size[1])
# begin drawing labels to pictures
# for every test folder
for i, im in enumerate(test_folders):
    # take each file that ends with png
    objects = [x for x in os.listdir(test_folders[i]) if x.endswith('.png')]
    object_name = labels[i]
    # each object has 12 views, take only one random view
    for k, j in enumerate(range(0, len(objects), 12)):
        # random view to take
        view = random.randint(0, 11)
        # path to currently processed image
        image_path = os.path.join(test_folders[i], objects[j+view])
        image = Image.open(image_path)
        # extend image from bottom (it may be .crop but we use bigger height value)
        image = image.crop((0, 0, im_size[0], im_size[1] + box_height))

        font_type = ImageFont.truetype('arial.ttf', 70)
        draw = ImageDraw.Draw(image)
        # add a white rectangle to cover the extended black portion of the image (.crop)
        draw.rectangle((0, im_size[0], im_size[1], im_size[1] + box_height), fill='white')
        # random variable 0<x<1 to define whether the image should have a correct or wrong label
        # rand >= 0.5 label = correct, rand < 0.5 label = wrong
        rand = random.random()
        if rand >= 0.5:
            # text to be written on image
            txt = labels_gr[labels.index(object_name)]
            correct[k, i] = True
        else:
            flag = True
            # be sure to pick a wrong label and not the correct one
            while flag:
                randInt = random.randint(0, len(labels)-1)
                # check if it is not the correct one
                if labels[randInt] != object_name:
                    # text to be written on image
                    txt = labels_gr[randInt]
                    flag = False
                    correct[k, i] = False
        # take the width of the text to be written, we want to center the text
        w, _ = draw.textsize(txt, font=font_type)
        # draw the text
        draw.text(xy=((im_size[0]-w)/2, im_size[1]+box_height/2), text=txt, fill=(0, 0, 0), font=font_type)
        if not os.path.exists(os.path.join(save_folder, object_name)):
            os.makedirs(os.path.join(save_folder, object_name))
        image.save(os.path.join(save_folder, object_name, objects[j+view]))

np.save(save_folder+"\\labels", correct)
