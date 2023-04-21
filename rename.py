import os
#定义来源文件夹
path_src = r'D:/MyWork/Project/UA-DETRAC/scripts/train_image'
#定义目标文件夹
path_dst = r'D:/MyWork/Project/UA-DETRAC/scripts/train_image_rename'
#自定义格式，例如“报告-第X份”，第一个{}用于放序号，第二个{}用于放后缀
#rename_format = '报告-第{}份{}'
#初始序号
begin_num = 1
def doc_rename(path_src,path_dst,begin_num):
    for i in os.listdir(path_src):
        #获取原始文件名
        doc_src = os.path.join(path_src, i)
        #重命名
        doc_name = i[0:18]
        doc_name = doc_name + '.jpg'
        #确定目标路径
        doc_dst = os.path.join(path_dst, doc_name)
        begin_num += 1
        os.rename(doc_src,doc_dst)
#运行函数
doc_rename(path_src,path_dst,begin_num)
#img02481_MVI_40172