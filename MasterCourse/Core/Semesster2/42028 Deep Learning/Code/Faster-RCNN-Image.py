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


def detect_objects_in_image(image, model, threshold=0.5):
    # 将图像转换为 PyTorch 张量
    img_tensor = F.to_tensor(image).unsqueeze(0)

    # 使用模型进行推断
    with torch.no_grad():
        predictions = model(img_tensor)

    detected_objects = []

    # 提取预测结果并在图像上绘制框
    result_image = image.copy()
    for box, label, score in zip(predictions[0]['boxes'], predictions[0]['labels'], predictions[0]['scores']):
        if score > threshold:
            box = box.cpu().numpy().astype(int)
            cv2.rectangle(result_image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(result_image, f'Class: {label.item()}, Score: {score.item():.2f}', (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            detected_objects.append({
                'label': label.item(),
                'score': score.item(),
                'box': box.tolist()
            })

    return result_image, detected_objects



# 加载模型
weights_path = r'Z:\CodeSaving\Pycharm\DL_WebCam\ObjectDetection-FasterRCNN\outputs\training\FinalEP50BZ\best_model.pth'  # 模型权重文件路径
num_classes = 4  # 你的数据集的类别数
model = load_faster_rcnn_model(weights_path, num_classes)

# 在这里你可以使用加载的模型进行推断或者继续训练

# 视频输入和输出路径

image_path = r'Z:\CodeSaving\Pycharm\DL_WebCam\KITTIdata\testRunning\YOLO\train\images\000001.png'
image = cv2.imread(image_path)
result_image, detected_objects = detect_objects_in_image(image, model, threshold=0.5)

# 显示处理后的图片
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

