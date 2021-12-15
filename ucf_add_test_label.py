import os

def main():
    classInd_path = "classInd.txt"
    testlist_path = "testlist01.txt"
    save_path = "testlist.txt"
    class2id = {}
    with open(classInd_path, 'r') as f:
        class_id = f.readlines()
        for item in class_id:
            id = item.split(' ')[0]
            label = item.split(' ')[1].strip()
            class2id[label] = id
        f.close()

    with open(testlist_path, 'r') as f:
        video_paths = f.readlines()
        f.close()

    with open(save_path, 'a') as f:
        for i in range(len(video_paths)):
            video_path = video_paths[i]
            video_label = video_path.split('/')[0]
            video_paths[i] = video_path.strip() + " " + class2id[video_label] + "\n"
        f.writelines(video_paths)
        f.close()

if __name__ == '__main__':
    main()
