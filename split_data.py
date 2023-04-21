'''
split the dataset into three groups according to a certain proportion (training set, validation set, and testing set)
'''
import os
import shutil
import random

# Ensure random reproducibility
random.seed(0)

"""
@brief: Divide the dataset into three groups according to a certain proportion (training set, validation set, and testing set)
@param: file_path: original dataset path
@param: new_file_path: new dataset path
@param: train_rate: training set ratio
@param: val_rate: validation set ratio
@return: None
"""
def split_data(file_path, new_file_path, xmlpath, train_rate, val_rate):

        eachclass_image = []
        for image in os.listdir(file_path):
            eachclass_image.append(image)
        total = len(eachclass_image)
        random.shuffle(eachclass_image)
        train_images = eachclass_image[0:int(train_rate * total)]  # Pay attention to left closing and right opening
        val_images = eachclass_image[int(train_rate * total):int((train_rate + val_rate) * total)]
        test_images = eachclass_image[int((train_rate + val_rate) * total):]

        # train
        for image in train_images:
            print(image)
            old_path = file_path + '/' + image
            new_path1 = new_file_path + '/' + 'train' + '/' + 'images'
            if not os.path.exists(new_path1):
                os.makedirs(new_path1)
            new_path = new_path1 + '/' + image
            # print(new_path)
            shutil.copy(old_path, new_path)
        new_name = os.listdir(new_file_path + '/' + 'train' + '/' + 'images')
        # print(new_name[1][:-4])
        for im in new_name:
            old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
            print('old',old_xmlpath)
            new_xmlpath1 = new_file_path + '/' + 'train' + '/' + 'labels'
            if not os.path.exists(new_xmlpath1):
                os.makedirs(new_xmlpath1)
            new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
            print('xml name',new_xmlpath)
            if not os.path.exists(f'{old_xmlpath}'):
                open(f'{old_xmlpath}', 'w')
            shutil.copy(old_xmlpath, new_xmlpath)

        # valid
        for image in val_images:
            old_path = file_path + '/' + image
            new_path1 = new_file_path + '/' + 'val' + '/' + 'images'
            if not os.path.exists(new_path1):
                os.makedirs(new_path1)
            new_path = new_path1 + '/' + image
            shutil.copy(old_path, new_path)
        new_name = os.listdir(new_file_path + '/' + 'val' + '/' + 'images')
        for im in new_name:
            old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
            new_xmlpath1 = new_file_path + '/' + 'val' + '/' + 'labels'
            if not os.path.exists(new_xmlpath1):
                os.makedirs(new_xmlpath1)
            new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
            if not os.path.exists(f'{old_xmlpath}'):
                open(f'{old_xmlpath}', 'w')
            shutil.copy(old_xmlpath, new_xmlpath)

        # test
        for image in test_images:
            old_path = file_path + '/' + image
            new_path1 = new_file_path + '/' + 'test' + '/' + 'images'
            if not os.path.exists(new_path1):
                os.makedirs(new_path1)
            new_path = new_path1 + '/' + image
            shutil.copy(old_path, new_path)
        new_name = os.listdir(new_file_path + '/' + 'test' + '/' + 'images')
        for im in new_name:
            old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
            new_xmlpath1 = new_file_path + '/' + 'test' + '/' + 'labels'
            if not os.path.exists(new_xmlpath1):
                os.makedirs(new_xmlpath1)
            new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
            if not os.path.exists(f'{old_xmlpath}'):
                open(f'{old_xmlpath}', 'w')
            shutil.copy(old_xmlpath, new_xmlpath)
        print('ok')

"""
@brief: Divide the dataset into two groups according to a certain proportion (validation set and testing set)
@param: file_path: original dataset path
@param: new_file_path: new dataset path
@param: rate: validation set ratio
@return: None
"""
def split_data(file_path, new_file_path, xmlpath, rate):

    eachclass_image = []
    for image in os.listdir(file_path):
        eachclass_image.append(image)
    total = len(eachclass_image)
    random.shuffle(eachclass_image)
    val_images = eachclass_image[0:int(rate * total)]
    test_images = eachclass_image[int(rate * total):]

    # valid
    for image in val_images:
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'val' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
    new_name = os.listdir(new_file_path + '/' + 'val' + '/' + 'images')
    for im in new_name:
        old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
        new_xmlpath1 = new_file_path + '/' + 'val' + '/' + 'labels'
        if not os.path.exists(new_xmlpath1):
            os.makedirs(new_xmlpath1)
        new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
        if not os.path.exists(f'{old_xmlpath}'):
            open(f'{old_xmlpath}', 'w')
        shutil.copy(old_xmlpath, new_xmlpath)

    # test
    for image in test_images:
        old_path = file_path + '/' + image
        new_path1 = new_file_path + '/' + 'test' + '/' + 'images'
        if not os.path.exists(new_path1):
            os.makedirs(new_path1)
        new_path = new_path1 + '/' + image
        shutil.copy(old_path, new_path)
    new_name = os.listdir(new_file_path + '/' + 'test' + '/' + 'images')
    for im in new_name:
        old_xmlpath = xmlpath + '/' + im[:-3] + 'txt'
        new_xmlpath1 = new_file_path + '/' + 'test' + '/' + 'labels'
        if not os.path.exists(new_xmlpath1):
            os.makedirs(new_xmlpath1)
        new_xmlpath = new_xmlpath1 + '/' + im[:-3] + 'txt'
        if not os.path.exists(f'{old_xmlpath}'):
            open(f'{old_xmlpath}', 'w')
        shutil.copy(old_xmlpath, new_xmlpath)
    print('ok')

if __name__ == '__main__':
    file_path = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/test_image"
    xmlpath = 'D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/test_label_txt'
    new_file_path = "D:/MyWork/github/My_Project/UA_DETRAC_Process/Data/test_and_val"
    split_data(file_path, new_file_path, xmlpath, rate = 0.5)

