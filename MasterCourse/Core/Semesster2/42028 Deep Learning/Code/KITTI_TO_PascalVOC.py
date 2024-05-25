
# encoding:utf-8
# 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML 这段删除
# Generate an XML from a blank file using a DOM tree based on a given XML Schema.
from xml.dom.minidom import Document
import cv2
import glob
import os
def generate_xml(name, split_lines, img_size):
    doc = Document()
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    title = doc.createElement('folder')
    title_text = doc.createTextNode('KITTI')
    title.appendChild(title_text)
    annotation.appendChild(title)
    img_name=name+'.jpg'
    title = doc.createElement('filename')
    title_text = doc.createTextNode(img_name)
    title.appendChild(title_text)
    annotation.appendChild(title)
    source = doc.createElement('source')
    annotation.appendChild(source)
    title = doc.createElement('database')
    title_text = doc.createTextNode('The KITTI Database')
    title.appendChild(title_text)
    source.appendChild(title)
    title = doc.createElement('annotation')
    title_text = doc.createTextNode('KITTI')
    title.appendChild(title_text)
    source.appendChild(title)
    size = doc.createElement('size')
    annotation.appendChild(size)
    title = doc.createElement('width')
    title_text = doc.createTextNode(str(img_size[1]))
    title.appendChild(title_text)
    size.appendChild(title)
    title = doc.createElement('height')
    title_text = doc.createTextNode(str(img_size[0]))
    title.appendChild(title_text)
    size.appendChild(title)
    title = doc.createElement('depth')
    title_text = doc.createTextNode(str(img_size[2]))
    title.appendChild(title_text)
    size.appendChild(title)
    for split_line in split_lines:
        line = split_line.strip().split()
        if line[0] in ('Car', 'Van', 'Truck'):  # 仅处理属于 Car, Van, Truck 类别的标注信息
            object = doc.createElement('object')
            annotation.appendChild(object)

            title = doc.createElement('name')
            title_text = doc.createTextNode(line[0])
            title.appendChild(title_text)
            object.appendChild(title)
            bndbox = doc.createElement('bndbox')
            object.appendChild(bndbox)
            title = doc.createElement('xmin')
            title_text = doc.createTextNode(str(int(float(line[4]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymin')
            title_text = doc.createTextNode(str(int(float(line[5]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('xmax')
            title_text = doc.createTextNode(str(int(float(line[6]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymax')
            title_text = doc.createTextNode(str(int(float(line[7]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
    # 将DOM对象doc写入文件
    save_path = "Z:\CodeSaving\Pycharm\DL_AT3\DL_AT3_Data\AfterScreened\pascalVOC"
    f = open(os.path.join(save_path, name + '.xml'), 'w')  # xml
    f.write(doc.toprettyxml(indent=''))
    f.close()


if __name__ == '__main__':
    image_dir = "Z:\CodeSaving\Pycharm\DL_AT3\DL_AT3_Data\AfterScreened\image"
    labels_dir = "Z:\CodeSaving\Pycharm\DL_AT3\DL_AT3_Data\AfterScreened\label"

    for parent, dirnames, filenames in os.walk(labels_dir):
        for file_name in filenames:
            full_path = os.path.join(parent, file_name)
            f = open(full_path)
            split_lines = f.readlines()
            name = file_name[:-4]
            img_name = name + '.png'
            img_path = os.path.join(image_dir, img_name)
            img_size = cv2.imread(img_path).shape
            generate_xml(name, split_lines, img_size)
            print('txts has converted into xmls')

