import numpy as np
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2
import torch
from torchvision.transforms import functional as F
import cv2
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

class YourClass:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = fasterrcnn_resnet50_fpn_v2(pretrained=False)
        in_features = self.model.roi_heads.box_predictor.cls_score.in_features
        self.model.roi_heads.box_predictor = FastRCNNPredictor(in_features, 4)
        checkpoint = torch.load(
            r'Z:\CodeSaving\Pycharm\DL_WebCam\ObjectDetection-FasterRCNN\outputs\training\FinalEP50BZ\best_model.pth',
            map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.model.to(self.device)
        self.model.eval()

    def detect_and_draw(self, image):
        with torch.no_grad():
            tensor_image = F.to_tensor(image).unsqueeze(0).to(self.device)
            predictions = self.model(tensor_image)

        for box, score, label in zip(predictions[0]['boxes'], predictions[0]['scores'], predictions[0]['labels']):
            box = [int(coord) for coord in box.tolist()]
            cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(image, f"Label: {label}, Score: {score:.2f}", (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return image


def main():
    video = cv2.VideoCapture(0)
    detector = YourClass()

    while True:
        success, frame = video.read()
        if not success:
            break

        frame_with_detection = detector.detect_and_draw(frame)

        cv2.imshow('Object Detection', frame_with_detection)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
