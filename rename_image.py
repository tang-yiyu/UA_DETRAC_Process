'''
rename image files in a directory
'''

import os.path as osp
import os
import numpy as np
import shutil
import re
import sys

FLAG = 0 # 0: test 1: train
if FLAG == 1:

    ##train
    src_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/UA-DETRAC/Insight-MVT_Annotation_Train/" # image root
    dst_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/train_image" #new image root

else:
    ##test
    src_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/UA-DETRAC/Insight-MVT_Annotation_Test/" # image root
    dst_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/test_image" #new image root

def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)

mkdirs(dst_dir)

# This operation will modify the original file name and can only be run once
seqs = [s for s in os.listdir(src_dir)]

for seq in seqs: 
    path = osp.join(src_dir, seq)
    # print(path)
    fileList = os.listdir(path)  
    os.chdir(path)  

    for fileName in fileList: 
        pat = ".+\.(jpg|jpeg|JPG)"  
        pattern = re.findall(pat, fileName)  
        image_name = fileName.split(".")[0]  

        os.rename(fileName, ('{}_{}.jpg'.format(image_name, str(seq)))) 
       
    sys.stdin.flush()  
    print("after rename：" + str(os.listdir(path))) 

print("step1 finished!-----")

j = 0
for seq in seqs: 
    path = osp.join(src_dir, seq)

    for root, dirs, files in os.walk(path):
        files = sorted(files)
        for i in range(len(files)):
            if (files[i][-3:] == 'jpg' or files[i][-3:] == 'JPG') or files[i][-4:]=='jpeg':
                file_path = path + '/' + files[i]
                new_file_path = dst_dir + '/' + files[i]
                shutil.copy(file_path, new_file_path)
                j += 1
                print(j)
print("step2 finished!------")