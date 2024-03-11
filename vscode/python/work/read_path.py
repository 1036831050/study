import pandas as pd
import os


def find_files_with_extension(directory, extension):
    """
    找出指定目录中指定格式的文件
    :param directory: 目录路径
    :param extension: 文件格式（扩展名），如'.txt', '.csv'等
    :return: 包含符合条件文件绝对路径的列表
    """
    files_list: list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                files_list.append(os.path.abspath(os.path.join(root, file)))
    return files_list


def save_list_to_txt(lst, file_path):
    """
    将列表保存到文本文件中，每个元素单独一行
    :param lst: 要保存的列表
    :param file_path: 目标文本文件路径
    """
    with open(file_path, 'w') as f:
        for item in lst:
            f.write(str(item) + '\n')


def find_file_path(file_name, file_paths_file):
    """
    在已生成的绝对路径的文本文件中查找特定文件名对应的路径
    :param file_name: 要查找的文件名
    :param file_paths_file: 包含文件绝对路径的文本文件路径
    :return: 找到的文件路径（如果存在），否则返回 None
    """
    with open(file_paths_file, 'r') as f:
        for line in f:
            if file_name in line:
                return line.strip()  # 返回找到的文件路径并移除首尾的空格和换行符
    # 如果未找到对应文件名的路径，则返回 None
    return None


def write_url(excel_path,file_paths_file):
    """通过表格内的名称搜索路径并转换为超链接
    :param excel_path: 表格所在路径
    :param file_paths_file: 包含文件绝对路径的文本文件路径
    """
    # 读取 Excel 文件
    df = pd.read_excel(excel_path, sheet_name='Sheet1')
    encountered_file_names = set()
    # 遍历文件名和路径，并将路径转换为超链接
    for index, row in df.iterrows():
        file_name = row['文件名称']
        file_path = find_file_path(row['文件名称'], file_paths_file)
        print(file_name,file_path)
        if file_name in encountered_file_names:
            continue       
        # 将文件名添加到已经遇到的文件名集合中
        encountered_file_names.add(file_name)

        # 创建超链接字符串
        hyperlink = f'=HYPERLINK("{file_path}", "{file_name}")'

        # 更新路径列为超链接
        df.at[index, '文件名称'] = hyperlink

    # 保存修改后的 Excel 文件
    df.to_excel(excel_path, index=False)


def get_txt(directory,extention):
    if not os.path.exists('output.txt'):
        content = find_files_with_extension(directory, extention)   #寻找该目录下的指定格式文件
        save_list_to_txt(content, 'output.txt')   #保存到output文件内
    else:
        print("已存在output文件，请确认是否是需要的output")

def main():
    directory = r"F:\AndriodBackup\resiliosync\jpg\ai_generate\ai-pic\comfyui"  #要搜索的目录，视频所在目录
    get_txt(directory,'.png') #指定目录，搜索指定后缀的文件，并保存到output里
    excel_path = r"E:\desktop\用电记录.xlsx"  # 表格所在路径
    # 读取表格文件
    write_url(excel_path,'output.txt')

if __name__ == '__main__':
    main()