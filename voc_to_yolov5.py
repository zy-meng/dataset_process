import xml.etree.ElementTree as ET
import pickle
import os
from os.path import join

classes = ['window_shielding', 'multi_signs', 'non_traffic_sign']

root_path = 'datasets'
xml_path = root_path + '/VOC/Annotations'
txt_path = root_path + '/labels'  # 生成的.txt文件会被保存在labels目录下
if not os.path.exists(txt_path):
    os.makedirs(txt_path)


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    if w >= 1:
        w = 0.99
    if h >= 1:
        h = 0.99
    return x, y, w, h


def convert_annotation(xml_full_path, xml_name):
    with open(xml_full_path, "r", encoding='UTF-8') as in_file:
        txt_name = xml_name[:-4] + '.txt'
        txt_full_path = os.path.join(txt_path, txt_name)
        with open(txt_full_path, "w+", encoding='UTF-8') as out_file:
            tree = ET.parse(in_file)
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)
            out_file.truncate()
            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('txt_name').text
                if cls not in classes or int(difficult) == 1:
                    continue
                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                     float(xmlbox.find('ymax').text))
                bb = convert((w, h), b)
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == "__main__":
    xml_names = os.listdir(xml_path)
    for xml_name in xml_names:
        xml_full_path = os.path.join(xml_path, xml_name)
        if ('.xml' in xml_full_path) or ('.XML' in xml_full_path):
            convert_annotation(xml_full_path,xml_name)
