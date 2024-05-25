
# Different .py files function  
    Note: we only use the train dataset, which means the total images and labels are 7481 


     
**The present folder structure:**  
  
After unzip the data from KITTI official website:  
--../DL_AT3_Data/KITTI_TrainData  
---- label_2  
---- image_2  
  
## 1.DataPreprocess.py:  
  It is mainly function is to select the label document, which contains "Van", "Car", "Truck" in the txt files. Then transfering these files into another document.  
                                  And then transfer the same file name with label file in image document to another   
  **There will create a new folder -- AfterScreened, and its structure:**  
    
  --../DL_AT3_Data/AfterScreened  
  ----label  ## contain 6789 images  
  ----image  ## contain 6789 labels  
    
      
## 2.KITTI_TO_PascalVOC.py:   
It is maily function is to transfer the label file in KITTI into Pascal VOC format which is benifit in Faster-RCNN model.
    
    Notes: Pascal VOC format files will be copied into new document for model training  
  
**The present folder structure:**  
    
  --../DL_AT3_Data/AfterScreened    
  ----label  
  ----image  
  ----pascalVOC  
    
## 3.KITTI_TO_YOLO.py: 
    This is the first mehod to transfer the label format from KITTI to yolo  
  
    Notes: for this method, we process 3 classes seperately. Specifically, 0 --> Car   1 --> Van    2 --> Truck  

**The present folder structure:**  
    
  --../DL_AT3_Data/AfterScreened    
  ----label  
  ----image  
  ----pascalVOC  
  ----YOLO
## 4. Second Method for KITTI to YOLO:
### KITTITOYOLO.py:   
    This is to process 3 classes into 1 class, which means there is only 1 class. 
      We define classes of "Van", "Car", "Truck" are same class, "Car"

### PyTXTtoXML.py: 
    It is to transfer processed label fiels by KITTIYOLO.py into XML format.

### XMLToYOLO.py: 
    It is to transfer the XML files into yolo format

  
## Note: 
We also supply the code for testing model by images, videos and real time.  
  
    1."Faster-RCNN-Image": using RCNN model to testing the image results.  
    2."Faster-RCNN-Video": using RCNN model to testing the video results.  
    3."Faster-RCNN-RealTime":  using RCNN model to testing by real time.  
    4."YOLO_Realtime":  using yolo model to testing by real time  
  



