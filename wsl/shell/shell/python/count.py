# coding:UTF-8
# coding=<encoding name>
import os
import pandas as pd
import numpy as np

#定义方法获取目录下的csv文件
def workOn(path):
    filePaths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            if 'csv' in file:
                filePaths.append(os.path.join(root, file))
            else:
                continue
    count = 0
    for filename in filePaths:
        count +=1
        print(filename)
    return filePaths,count

def skip_to(filename,**kwargs):
    if os.stat(filename).st_size == 0:
        raise ValueError("File is empty")
    with open(filename) as f:
        pos = 0
        cur_line = f.readline()
        while not cur_line.find('Precision')>=0:
            pos = f.tell()
            cur_line = f.readline()
        f.seek(pos)
        return pd.read_csv(f, **kwargs)
def merge_file(file_lst):
    all_lst = []
    for file in file_lst:
        df = skip_to(file)
        single_file_lst = []
        matrix_lst = []
        obobstacle_type_lst = []
        for line in range(df.shape[0]):
            obstacle_type = df.iloc[line, 0]
            precision_hit = df.loc[line, ["Precision_hit"]].astype(int)[0]
            precision_all = df.loc[line, ["Precision_all"]].astype(int)[0]
            recall_hit = df.loc[line, ["Rcall_hit"]].astype(int)[0]
            recall_all = df.loc[line, ["Rcall_all"]].astype(int)[0]
            loc_loss = df.loc[line,["loc_loss"]].astype(int)[0]
            single_file_lst.append([precision_hit, precision_all, recall_hit, recall_all,loc_loss])
            matrix_lst.append([0, 0, 0, 0,0])
            obobstacle_type_lst.append(obstacle_type)
        all_lst.append(single_file_lst)
    for matrix_lst_single in all_lst:
        matrix_lst += np.array(matrix_lst_single)
    print(matrix_lst)
    result_lst = []
    for value_lst in matrix_lst:
        precision_hit = value_lst[0]
        precision_all = value_lst[1]
        recall_hit = value_lst[2]
        recall_all = value_lst[3]
        loc_loss = value_lst[4]
        precision = round(precision_hit / precision_all, 9)
        recall = round(recall_hit / recall_all, 9)
        LOC_loss = round(loc_loss / count,9)
        result_lst.append([precision, recall,LOC_loss, precision_hit, precision_all, recall_hit, recall_all])
    data = pd.DataFrame(result_lst, columns = ['precision', 'recall', 'LOC_loss','precision_hit', 'precision_all', 'recall_hit', 'recall_all'])
    data.insert(0, "obstacle_type", None)
    for line in range(data.shape[0]):
        data.loc[line, "obstacle_type"] = obobstacle_type_lst[line]
    data.to_csv("汇总.csv", index = False)


if __name__ == '__main__':
    path = input("请输入路径：")
    file_lst,count = workOn(path)
    merge_file(file_lst)

