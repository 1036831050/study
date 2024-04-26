import re
import os
import sys
 

# 作用是将txt格式的小说文件，按照章节切分成单独的txt文件，并生成目录文件。
# txt book's path.
novel_name='' #小说名字
source_path = input("请输入小说的绝对路径：")
 
path_pieces = os.path.split(source_path)
print(path_pieces)
novel_title = re.sub(r'\.(txt)$', '', path_pieces[1])
target_path = '%s/%s' % (path_pieces[0], novel_title)#小说分章目录
section_re = re.compile(r'\s*第.{1,3}章.*$')


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
            chapter_name=re.sub('(~+|\*+|\,+|\?+|\，+|\?+)','_',line)
            output = open('%s/%s.txt' % (target_path, chapter_name), 'w',encoding='utf-8')
            # 创建章节对应目录
            # os.makedirs(os.path.join(target_path, chapter_name))
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