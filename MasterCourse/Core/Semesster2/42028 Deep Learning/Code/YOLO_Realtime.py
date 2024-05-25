
import cv2
import torch
import time
import numpy as np
import yolov5.hubconf

from torchvision.transforms import functional as F


class RealTimeDetector:
    def __init__(self, model_path, conf_thresh=0.4, device='cuda'):
        self.device = torch.device(device)
        self.model = torch.hub.load(r'Z:\CodeSaving\Pycharm\DL_WebCam\yolov5', 'custom', path=r"Z:\CodeSaving\Pycharm\DL_WebCam\yolov5\runs\train\exp13\weights\best.pt",
                       source='local')
        self.model.conf = conf_thresh
        self.model.eval()

    def detect_and_draw(self, frame):
        with torch.no_grad():
            results = self.model(frame)  # 使用模型进行推理

        # 检测结果现在返回为列表，其中每个元素是一个字典，包含框、置信度和标签
        for result in results.pred[0]:
            box = result[:4].int()  # 提取框坐标
            conf = result[4]  # 提取置信度
            label = int(result[5])  # 提取标签
            box = [int(coord) for coord in box.tolist()]  # 转换为整数坐标
            x1, y1, x2, y2 = box  # 获取框的坐标
            # 调整框的大小
            box_width = x2 - x1
            box_height = y2 - y1
            x1_new = max(0, x1 - int(0.1 * box_width))  # 调整框左上角 x 坐标
            y1_new = max(0, y1 - int(0.1 * box_height))  # 调整框左上角 y 坐标
            x2_new = min(frame.shape[1], x2 + int(0.1 * box_width))  # 调整框右下角 x 坐标
            y2_new = min(frame.shape[0], y2 + int(0.1 * box_height))  # 调整框右下角 y 坐标
            cv2.rectangle(frame, (x1_new, y1_new), (x2_new, y2_new), (0, 255, 0), 2)  # 绘制调整后的框
            cv2.putText(frame, f"Label: {label}, Score: {conf:.2f}", (x1_new, y1_new - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        return frame


def main():
    video = cv2.VideoCapture(0)
    detector = RealTimeDetector(r"Z:\CodeSaving\Pycharm\DL_WebCam\yolov5\runs\train\exp13\weights\best.pt",
                                conf_thresh=0.5)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame_with_detection = detector.detect_and_draw(frame)

        cv2.imshow('Real-time Object Detection', frame_with_detection)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

