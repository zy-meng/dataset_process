# -*- coding: UTF-8 -*-
import os
import sys
import random
import shutil


"""
    仅需修改root_path、dataset_path和train_percent
"""

dataset_path = "../orchard/data_2"
train_percent = 0.8


def split_train_val():
    image_file_path = os.path.join(dataset_path, "images")
    label_file_path = os.path.join(dataset_path, "labels")

    save_path = dataset_path + "TrainVal"
    save_path_images_train = os.path.join(save_path, "images/train")
    save_path_images_val = os.path.join(save_path, "images/val")
    save_path_labels_train = os.path.join(save_path, "labels/train")
    save_path_labels_val = os.path.join(save_path, "labels/val")

    if not os.path.exists(save_path):
        os.makedirs(save_path)
        os.makedirs(save_path_images_train)
        os.makedirs(save_path_images_val)
        os.makedirs(save_path_labels_train)
        os.makedirs(save_path_labels_val)

    total_images = os.listdir(image_file_path)

    total_names = []

    for image in total_images:
        index = image.rfind('.')
        if image[index:] == ".jpg":  # 去除非图片文件，尤其是一些隐藏文件的影响
            total_names.append(image[:index])


    num = len(total_names)
    train_size = int(num * train_percent)

    train = random.sample(total_names, train_size)
    val = []
    for name in total_names:
        if name not in train:
            val.append(name)

    for name in train:
        shutil.copyfile(image_file_path+'/'+name+'.jpg', save_path_images_train+'/'+name+'.jpg')
        shutil.copyfile(label_file_path + '/' + name + '.txt', save_path_labels_train + '/' + name + '.txt')
        print("convert"+name+"to train")

    for name in val:
        shutil.copyfile(image_file_path+'/'+name+'.jpg', save_path_images_val+'/'+name+'.jpg')
        shutil.copyfile(label_file_path + '/' + name + '.txt', save_path_labels_val + '/' + name + '.txt')
        print("convert"+name+"to val")


if __name__ == "__main__":
    split_train_val()
