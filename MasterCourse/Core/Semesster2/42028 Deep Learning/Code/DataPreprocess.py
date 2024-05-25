import os
from shutil import copyfile

# 定义数据集的路径
data_path = "Z:\CodeSaving\Pycharm\DL_AT3\DL_AT3_Data\KITTI_TrainData"
output_dir = "Z:\CodeSaving\Pycharm\DL_AT3\DL_AT3_Data"

# 获取训练数据的路径
train_image_dir = os.path.join(data_path, "image_2")
train_label_dir = os.path.join(data_path, "label_2")

# 创建存放筛选后数据的目录结构
output_train_dir = os.path.join(output_dir, "AfterScreened")
output_image_dir = os.path.join(output_train_dir, "image")
output_label_dir = os.path.join(output_train_dir, "label")
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 筛选出标签为"Car"、"Van"、"Truck"的数据并保存
for image_file in os.listdir(train_image_dir):
    image_path = os.path.join(train_image_dir, image_file)
    label_file = image_file.replace(".png", ".txt")  # 根据图片文件名得到标签文件名
    label_path = os.path.join(train_label_dir, label_file)

    # 读取标签数据
    filtered_labels = []
    with open(label_path, 'r') as f:
        for line in f:
            label = line.strip().split(' ')
            # 仅保留 Car、Van 和 Truck 类别的物体信息
            if label[0] in ["Car", "Van", "Truck"]:
                filtered_labels.append(label)

    # 如果筛选后的标签信息不为空，则保存对应的图片和标签
    if filtered_labels:
        # 拷贝图片文件到输出目录
        output_image_path = os.path.join(output_image_dir, image_file)
        copyfile(image_path, output_image_path)

        # 保存筛选后的标签文件到输出目录
        output_label_path = os.path.join(output_label_dir, label_file)
        with open(output_label_path, 'w') as f:
            for label in filtered_labels:
                f.write(' '.join(label) + '\n')


