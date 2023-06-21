import re
import os
def splitnovel(file_path):
    with open(file_path,'rb',encoding='utf-8')as f1:
        content = f1.readlines();
        return content;
'''
path = input("请输入文件路径：")
print(path)
content = splitnovel('/home/liang/novel.txt')

for i,j,k in os.walk('/home/liang/python'):
    print("path:",i)
    print('dirs:',j)
    print('files:',k)
'''
 
# -*- coding: utf-8 -*-
# @Date     : 2018-11-02 17:38:53
# @Author   : Jimy_Fengqi (jmps515@163.com)
# @Link     : https://blog.csdn.net/qiqiyingse
# @Version  : V1.0
 
'''
将txt小说分割转换成单个章节文件
文件名字以章节命名
本文运行在python3上面，
处理小说的时候，需要将小说的格式以utf-8保存
（处理以ANSI编码格式的txt文本会出现错误）
'''
 
import re
import os
import sys
 
# txt book's path.
novel_name='' #小说名字
source_path = input("请输入小说的绝对路径：")
 
path_pieces = os.path.split(source_path)
print(path_pieces)
novel_title = re.sub(r'\.(txt)$', '', path_pieces[1])
target_path = '%s/%s' % (path_pieces[0], novel_title)#小说分章目录
section_re = re.compile(r'^第.+章.*$')


def main():
    print(path_pieces)
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    output = open('%s/前言.txt' % (target_path), 'w',encoding='utf-8')
    preface_title = '%s 前言' % novel_title
    output.writelines(preface_title)

    input = open(source_path, 'r',encoding='utf-8')
    sec_count = 0
    sec_cache = []
    title_cache=[]


    for line in input:
        if re.match(section_re,line):
            line = re.sub(r'\s+','',line)
            print('转换中... %s...' % line)
            output.writelines(sec_cache)
            output.flush()
            output.close()
            sec_cache = []
            sec_count +=1
            chapter_name=re.sub('(~+|\*+|\,+|\?+|\，+|\?+|\d+)','_',line)
            output = open('%s/%s.txt' % (target_path, chapter_name), 'w',encoding='utf-8')
            output.writelines(line)
            title_cache.append(line+'\n')
        else:
            sec_cache.append(line)
    output.writelines(sec_cache)
    output.flush()
    output.close()
    sec_cache = []

    output = open('%s\\目录.txt' % (target_path), 'w',encoding='utf-8')
    menu_head = '%s 目录' % novel_title
    output.writelines(menu_head)
    output.writelines(title_cache)
    output.flush()
    output.close()
    inx_cache = []

    print ('completed. %d chapter(s) in total.' % sec_count)


if __name__ == '__main__':
    main()