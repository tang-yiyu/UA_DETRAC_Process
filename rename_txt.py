'''
rename label files in a directory
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
    src_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/Train_DETRAC_TXT"
    dst_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/train_label_txt"

else:
    ##test
    src_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/Test_DETRAC_TXT"
    dst_dir = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/test_label_txt"

def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)

mkdirs(dst_dir)

seqs = [s for s in os.listdir(src_dir)]

for seq in seqs: 
    path = osp.join(src_dir, seq)
    # print(path)
    fileList = os.listdir(path)  
    os.chdir(path)  

    for fileName in fileList: 
        pat = ".+\.(txt|xml|json)"  
        pattern = re.findall(pat, fileName)  
        image_name = fileName.split(".")[0]  

        os.rename(fileName, ('{}_{}.txt'.format(image_name, str(seq)))) 
       
    sys.stdin.flush()  
    print("after rename：" + str(os.listdir(path))) 

print("step1 finished!-----")

j = 0
for seq in seqs: 
    path = osp.join(src_dir, seq)

    for root, dirs, files in os.walk(path):
        files = sorted(files)
        for i in range(len(files)):
            if files[i][-3:] == 'txt':
                file_path = path + '/' + files[i]
                new_file_path = dst_dir + '/' + files[i]
                shutil.copy(file_path, new_file_path)
                j += 1
                print(j)
print("step2 finished!------")
# print(str(os.listdir(dst_dir)))