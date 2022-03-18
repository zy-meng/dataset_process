import os
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
old_label_dir = "../labels/train"
new_label_dir = "../labels/new_train"
# old_label_dir = "../labels/val"
# new_label_dir = "../labels/new_val"

if not os.path.exists(new_label_dir):
    os.mkdir(new_label_dir)

def main():
    label_name_list = os.listdir(old_label_dir)
    for label_name in label_name_list:
        drop_label(label_name) 
        print(label_name,"finished")

def drop_label(file_name):
    old_file_path = os.path.join(old_label_dir,file_name)
    with open (old_file_path, "r") as f:
        labels = f.readlines()
    labels = [label.strip() for label in labels]
    new_labels = []

    for label in labels:
        if int(label.split()[0]) == 0:  # 0=person
            new_labels.append(label)
    new_label_path = os.path.join(new_label_dir,file_name)

    with open(new_label_path, 'w') as f:
        for new_label in new_labels:
            f.writelines(new_label+'\n')


if __name__ == "__main__":
    main()

