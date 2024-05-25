**The following steps are to train model** 
# Install the python => 3.8.0
# Download the Faster-RCNN from github  
    !git clone https://github.com/nabinsharmaUTS/ObjectDetection-FasterRCNN.git
notes: if you use the command window, delete the "!" and then run the above code  

# Install the requirement packages
    # Install the Requirements
    !pip install -r requirements.txt
notes: if there are some packages are not directly downloading, please search these packages by using search engine  
You can see the soluton in YOLO folder, in the file 'Steps For using.md'.  
  
# Create a custom dataset YMAL file
The content as following:    
    %%writefile data_configs/custom_data.yaml  
    # Images and labels direcotry should be relative to train.py  
    TRAIN_DIR_IMAGES: Z:/CodeSaving/Pycharm/DL_AT3/DL_AT3_Data/Data/RCNN/train  
    TRAIN_DIR_LABELS: Z:/CodeSaving/Pycharm/DL_AT3/DL_AT3_Data/Data/RCNN/train  
    VALID_DIR_IMAGES: Z:/CodeSaving/Pycharm/DL_AT3/DL_AT3_Data/Data/RCNN/valid  
    VALID_DIR_LABELS: Z:/CodeSaving/Pycharm/DL_AT3/DL_AT3_Data/Data/RCNN/valid  
    
    # Class names.  
    CLASSES:  
    - __background__  
    - Car  
    - Van  
    - Truck  
      
    # Number of classes (object classes + 1 for background class in Faster RCNN).  
    NC: 4  
      
    # Whether to save the predictions of the validation set while training.  
    SAVE_VALID_PREDICTION_IMAGES: true  

# Train model
    !python train.py --config data_configs/custom_data.yaml --epochs 25 --model fasterrcnn_resnet50_fpn_v2 --project-name ObjectEP25 --batch-size 2 --no-mosaic




