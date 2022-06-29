import os
from tqdm import tqdm
import shutil
"""
--Annotations
 |-yolo_select_label.py
--images
 |-train
 |-val
--labels
 |-train
 |-val
"""
root_dir = "/home/mzy/datasets/COCO"
old_label_dir = os.path.join(root_dir, "labels/train")
new_label_dir = os.path.join(root_dir, "labels/new_train")
old_image_dir = os.path.join(root_dir, "images/train")
new_image_dir = os.path.join(root_dir, "images/new_train")

# old_label_dir = "../labels/val"
# new_label_dir = "../labels/new_val"

TOTAL_NUM = 0
DEPRECATE_NUM = 0


def drop_label(file_name):
    """ Select label for specific class 
    """
    global TOTAL_NUM
    global DEPRECATE_NUM

    old_file_path = os.path.join(old_label_dir,file_name)
    with open (old_file_path, "r") as f:
        labels = f.readlines()
    labels = [label.strip() for label in labels]
    new_labels = []

    for label in labels:
        if int(label.split()[0]) == 0:  # 0=person
            new_labels.append(label)
    new_label_path = os.path.join(new_label_dir,file_name)
    
    if len(new_labels) == 0:
        DEPRECATE_NUM += 1
        return 0
    
    with open(new_label_path, 'w') as f:
        for new_label in new_labels:
            f.writelines(new_label+'\n')
    TOTAL_NUM += 1


def transport_image(image_name):
    """ Transport image to new directory
    """
    old_image_path = os.path.join(old_image_dir, image_name)
    new_image_path = os.path.join(new_image_dir, image_name)
    shutil.copyfile(old_image_path, new_image_path)


def mkdir_if_not_exist(dirs):
    """make directories if not exist, support dir list 
    """
    if not isinstance(dirs, list):
        dirs = [dirs]
    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)
            print("create directory:{}".format(dir))

def main():

    mkdir_if_not_exist([new_label_dir, new_image_dir])

    label_name_list = os.listdir(old_label_dir)
    for label_name in tqdm(label_name_list):
        drop_label(label_name)
    
    image_name_list = os.listdir(new_label_dir)
    for i in range(len(image_name_list)):
        image_name_list[i] = image_name_list[i][:-3] + "jpg"

    for image_name in tqdm(image_name_list):
        transport_image(image_name)
    
    print("TOTAL_NUM:{}".format(TOTAL_NUM))
    print("DEPRECATE_NUM:{}".format(DEPRECATE_NUM))




if __name__ == "__main__":
    main()

