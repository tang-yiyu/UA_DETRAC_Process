# UA_DETRAC_Process

## Description
Preprocess the UA-DETRAC dataset and create a dataset for YOLOv5.

## Instructions
1. Download the UA-DETRAC dataset from [here](https://detrac-db.rit.albany.edu/download) and unzip it.
2. Use `rename_image.py` to rename the images in the dataset.
3. Use `xml2txt.py` to convert the xml files in the dataset to txt files.
4. Use `rename_txt.py` to rename the txt files in the dataset.
5. (Optional)Use `split_data.py` to reorganize the dataset and divide it into training, validation, and testing sets according to a certain proportion. The method I adopted is to keep the original training set unchanged, and the original test set is divided into a new validation set and a test set in a 1:1 ratio.

## Reference
1. [使用yolov5训练UA-DETRAC车辆数据集](https://zhuanlan.zhihu.com/p/373096271)
2. [yolov5_UA_DETRAC](https://github.com/zigangzhao-ai/yolov5_UA_DETRAC/blob/main/yolov5_UA_DETRAC/utils/datasets_ori.py)
3. [YoloV5数据集自动划分训练集、验证集、测试集](https://blog.csdn.net/qq_43443001/article/details/125947785)
