**The following steps are to train model** 
# Install the python => 3.8.0
# Download the yolo from github  
    !git clone https://github.com/ultralytics/yolov5  
notes: if you use the command window, delete the "!" and then run the above code  
# Download the requirement in yolo  
    !pip install -r requirements.txt  
notes: if there are some packages are not directly downloading, please search these packages by using search engine  
### The solutino of some errors when downloading  
**1.Description:  loading "\lib\site-packages\torch\lib\shm.dll" or one of its dependencies**  
    Solution: https://stackoverflow.com/questions/74594256/pytorch-error-loading-lib-site-packages-torch-lib-shm-dll-or-one-of-its-depen  

        
**2.Description: loading “\lib\site-packages\torch\lib\shm.dll” or one of its dependencie**  
    Solution: https://discuss.pytorch.org/t/error-loading-lib-site-packages-torch-lib-shm-dll-or-one-of-its-dependencie/201695  

  notes: for solving this problem, you should firstly know which version of CUDA, python and windows.  
  
**3.Description: This probably means that Tcl wasn‘t installed properly**  
    Solution: https://blog.csdn.net/baiyibin0530/article/details/116718596  
    
**4.Description:Torch not compiled with CUDA enabled**  
    Solution: https://blog.csdn.net/qq_40329272/article/details/105727722
  
  
#  Set up a training YAML file  
**The content as following:**  

        #@title Setup Training YAML File
        number_of_classes = 5 #@param {type:"integer"}
        with open('new_train_yaml', 'w+') as file:
            file.write(
                f"""
                # parameters
                nc: {number_of_classes}  # number of classes
                depth_multiple: 0.33  # model depth multiple
                width_multiple: 0.50  # layer channel multiple

                # anchors
                anchors:
                  - [10,13, 16,30, 33,23]  # P3/8
                  - [30,61, 62,45, 59,119]  # P4/16
                  - [116,90, 156,198, 373,326]  # P5/32

                # YOLOv5 backbone
                backbone:
                  # [from, number, module, args]
                  [[-1, 1, Focus, [64, 3]],  # 0-P1/2
                   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4
                   [-1, 3, BottleneckCSP, [128]],
                   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8
                   [-1, 9, BottleneckCSP, [256]],
                   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16
                   [-1, 9, BottleneckCSP, [512]],
                   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32
                   [-1, 1, SPP, [1024, [5, 9, 13]]],
                   [-1, 3, BottleneckCSP, [1024, False]],  # 9
                  ]
        
                # YOLOv5 head
                head:
                  [[-1, 1, Conv, [512, 1, 1]],
                   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
                   [[-1, 6], 1, Concat, [1]],  # cat backbone P4
                   [-1, 3, BottleneckCSP, [512, False]],  # 13

                   [-1, 1, Conv, [256, 1, 1]],
                   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
                   [[-1, 4], 1, Concat, [1]],  # cat backbone P3
                   [-1, 3, BottleneckCSP, [256, False]],  # 17 (P3/8-small)

                   [-1, 1, Conv, [256, 3, 2]],
                   [[-1, 14], 1, Concat, [1]],  # cat head P4
                   [-1, 3, BottleneckCSP, [512, False]],  # 20 (P4/16-medium)
        
                   [-1, 1, Conv, [512, 3, 2]],
                   [[-1, 10], 1, Concat, [1]],  # cat head P5
                   [-1, 3, BottleneckCSP, [1024, False]],  # 23 (P5/32-large)
        
                   [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
                  ]
                """
            )

# Set a new_data.ymal
        #@title Setup Dataset Configuration (Data.yaml)
        train_data_dir = rootdir + "/data/Object_Detection/yolo/train" #@param {type:"string"}
        val_data_dir = rootdir + "/data/Object_Detection/yolo/valid" #@param {type:"string"}
        class_names = ['0', '1', '2', '3', '4'] #@param {type:"raw"}
        with open('new_data_yaml', 'w+') as file:
            file.write(
                f"""
                train: {train_data_dir}
                val: {val_data_dir}
        
                nc: {number_of_classes}
                names: {class_names}
                """
            )
  
# Start training
      ## ENTER CODE TO START TRAINING ##
      !python train.py --img 416 --batch 16 --epochs 200 --data new_data_yaml --cfg new_train_yaml
  
notes: the "new_train_yaml" file is created by 'Set up a training YAML file' steps  















    
