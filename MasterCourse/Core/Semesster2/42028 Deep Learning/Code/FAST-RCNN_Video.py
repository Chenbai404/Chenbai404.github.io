import torch
import cv2
import numpy as np
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2

from torchvision.transforms import functional as F

from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

def load_faster_rcnn_model(weights_path, num_classes):
    # 构建 Faster R-CNN 模型
    model = fasterrcnn_resnet50_fpn_v2(pretrained=False)
    # 修改分类器的输出类别数
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    # 加载模型权重文件
    checkpoint = torch.load(weights_path)
    model.load_state_dict(checkpoint['model_state_dict'])
    # 设置模型为评估模式
    model.eval()

    return model

def detect_objects_in_video(video_path, output_path, model, threshold=0.5):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: Unable to open video")
        return
    else:
        print("open seccess")
    # 获取视频帧率和尺寸
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # 循环处理视频帧
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 将帧转换为 PyTorch 张量
        img_tensor = F.to_tensor(frame).unsqueeze(0)

        # 使用模型进行推断
        with torch.no_grad():
            predictions = model(img_tensor)

        # 绘制预测框和标签
        for box, label, score in zip(predictions[0]['boxes'], predictions[0]['labels'], predictions[0]['scores']):
            if score > threshold:
                box = box.to(torch.int64).numpy()
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                cv2.putText(frame, f'Class: {label.item()}, Score: {score.item():.2f}', (box[0], box[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 写入帧到输出视频
        out.write(frame)

    # 释放资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()




# 加载模型
weights_path = r'Z:\CodeSaving\Pycharm\DL_WebCam\ObjectDetection-FasterRCNN\outputs\training\FinalEP50BZ\best_model.pth'  # 模型权重文件路径
num_classes = 4  # 你的数据集的类别数
model = load_faster_rcnn_model(weights_path, num_classes)

# 在这里你可以使用加载的模型进行推断或者继续训练

# 视频输入和输出路径
video_path = r'Z:\CodeSaving\Pycharm\DL_WebCam\ObjectDetection-FasterRCNN\data\test_1.mp4'  # 输入视频文件路径
output_path = r'Z:\CodeSaving\Pycharm\DL_WebCam\ObjectDetection-FasterRCNN\data\test_1.avi'  # 输出视频文件路径

# 运行目标检测并保存结果视频
detect_objects_in_video(video_path, output_path, model)





