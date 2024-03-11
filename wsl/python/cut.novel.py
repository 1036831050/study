import re
import os
from chardet.universaldetector import UniversalDetector

def get_encoding(file_path):
    detector = UniversalDetector()
    with open(file_path, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done: break
    detector.close()
    return detector.result['encoding']

def split_novel(file_path):
    ''' 
    将指定小说文本按章节分割，并分别保存为新的文本文件。
    :param file_path: 小说文件的路径 
    '''
    file_encoding = get_encoding(file_path)
    # 获取小说名称和所在目录
    dir_path, full_name = os.path.split(file_path)
    novel_name, _ = os.path.splitext(full_name)
    target_dir = os.path.join(dir_path, novel_name)
    # 设置章节文件保存目录
    # 如果章节文件保存目录不存在，则创建该目录
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    
    # 正则表达式匹配章节标题
    section_pattern = re.compile(r'.*第.{1,3}章(?![\u4e00-\u9fa5]).*')
    sec_count = 0  # 章节计数F:\AndriodBackup\resiliosync\novel\《熟女之殇》、《母爱的光辉》.txt
    sec_cache = []  # 存放当前章节内容
    title_cache = []  # 存放所有章节标题，用于生成目录文件
    # section_pattern = re.compile(r'.*第.+章.*')

    
    # 读取原小说内容，按章节分割并保存到新文件中
    with open(file_path, 'r', encoding=file_encoding,errors='replace') as input_file:
        chapter_title = "Chapter_Start"  # Default title or empty string
        for line in input_file:
            if re.match(section_pattern, line):
                # Now, if this is not the first chapter,
                # `chapter_title` will already have a sensible value.
                if sec_cache:
                    save_chapter(sec_count, sec_cache, target_dir, chapter_title)
                sec_count += 1
                chapter_title = re.sub(r'[\s~*+?,?，？]+', '_', line.strip())
                title_cache.append(chapter_title + '\n')
                sec_cache = [line]
            else:
                sec_cache.append(line)
        # After the loop to save the last chapter
        if sec_cache:
            save_chapter(sec_count, sec_cache, target_dir, chapter_title)
    
    # 生成目录文件
    generate_contents(title_cache, target_dir, novel_name)
    print('完成。共处理 %d 章。' % sec_count)

def save_chapter(sec_count, sec_cache, target_dir, chapter_title):
    ''' 
    保存单独的章节为文本文件。
    :param sec_count: 章节编号
    :param sec_cache: 章节内容
    :param target_dir: 目标文件夹路径
    :param chapter_title: 章节标题 
    '''
    chapter_file_path = os.path.join(target_dir, f'{sec_count:03d}_{chapter_title}.txt')  # 构建文件名，包括章节编号
    with open(chapter_file_path, 'w', encoding='utf-8') as f:
        f.writelines(sec_cache)

def generate_contents(title_cache, target_dir, novel_name):
    ''' 
    根据收集到的章节标题生成目录文件。
    :param title_cache: 章节标题列表
    :param target_dir: 目标文件夹路径
    :param novel_name: 小说名字 
    '''
    contents_file_path = os.path.join(target_dir, '目录.txt')
    with open(contents_file_path, 'w', encoding='utf-8') as f:
        f.write(novel_name + ' 目录\n')
        f.writelines(title_cache)

if __name__ == '__main__':
    source_path = input("请输入小说的绝对路径：")
    split_novel(source_path)
