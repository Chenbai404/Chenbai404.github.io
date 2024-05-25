import os

# 定义KITTI标签文件和输出目录的路径
label_dir = "Z:/CodeSaving/Pycharm/DL_AT3/DL_AT3_Data/AfterScreened/label"
output_dir = "Z:/CodeSaving/Pycharm/DL_AT3/DL_AT3_Data/AfterScreened/YOLO"
"""
 In the YOLO folder:
    0 --> Car
    1 --> Van
    2 --> Truck
 
"""
# 假设类别名称和对应的类别编号的映射关系为：

allowed_classes = ["Car", "Van", "Truck"]  # 允许的类别名称
class_mapping = {class_name: idx for idx, class_name in enumerate(allowed_classes)}

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 遍历KITTI标签文件夹中的每个文件
for label_file in os.listdir(label_dir):
    label_path = os.path.join(label_dir, label_file)
    output_path = os.path.join(output_dir, label_file)

    # 读取KITTI标签文件，并转换成YOLO格式
    yolo_lines = []
    with open(label_path, 'r') as f:
        for line in f:
            # 解析KITTI标签文件中的每一行
            line = line.strip().split(' ')
            class_name = line[0]

            # 如果该类别在允许的类别列表中，则转换成YOLO格式
            if class_name in allowed_classes:
                class_num = class_mapping[class_name]
                box_x_min, box_y_min, box_x_max, box_y_max = map(float, line[4:8])
                picture_width, picture_height = 1280, 720  # 假设图片尺寸为1280x720，你需要根据实际情况修改
                x_center = (box_x_min + box_x_max) / (2 * picture_width)
                y_center = (box_y_min + box_y_max) / (2 * picture_height)
                width = (box_x_max - box_x_min) / picture_width
                height = (box_y_max - box_y_min) / picture_height

                # 将转换后的YOLO格式信息保存到列表中
                yolo_lines.append(f"{class_num} {x_center} {y_center} {width} {height}")

    # 将转换后的YOLO格式信息写入输出文件
    with open(output_path, 'w') as f:
        for line in yolo_lines:
            f.write(line + '\n')
