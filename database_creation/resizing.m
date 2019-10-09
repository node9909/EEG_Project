clear;
clc;

load_folder = 'C:\Users\User01\Desktop\Apostolis\Programming\Python\Athena\Picture_labeling\pictures\labeled_gr';
save_folder = 'C:\Users\User01\Desktop\Apostolis\Programming\Python\Athena\Picture_labeling\pictures\resized_gr'

sub_folders = dir(load_folder);

for i=3:length(sub_folders)
  sfolder = strcat(sub_folders(i).folder, '\', sub_folders(i).name, '\');
  save_sub_folder = strcat(save_folder, '\', sub_folders(i).name);
  images = dir(sfolder);
  mkdir(save_sub_folder);
  for j=3:length(images)
    img = imread(strcat(sfolder, images(j).name));
    img = rgb2gray(img);
    img = imresize(img, 3, 'bicubic');
    imwrite(img, strcat(save_sub_folder, '\', images(j).name));
  endfor
endfor
