import cv2
import os
from mask import create_mask

folder_path = "./trial/mask/"
variety_mask_path = "./images/"
image_path = "./trial/mask/"

folder = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
variety = [os.path.join(variety_mask_path, f) for f in os.listdir(variety_mask_path) if os.path.isfile(os.path.join(variety_mask_path, f))]

print('{} and {}'.format(folder, variety))

for k in range(len(folder)):
    print('#####################################################################################')
    image_path = folder[k]
    images = [os.path.join(image_path, f) for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
    for j in range(len(variety)):    
        for i in range(len(images)):
            print(f'Editing {os.path.split(folder[k])[1]} with {os.path.split(variety[j])[1]} at {images[i]}')
            # print('image path: {} and mask variety path: {} '.format(images[i], variety[j]))
            create_mask(images[i], variety[j])