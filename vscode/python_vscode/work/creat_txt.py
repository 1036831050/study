import os

def find_files_with_extension(directory, extension):
    """
    找出指定目录中指定格式的文件
    :param directory: 目录路径
    :param extension: 文件格式（扩展名），如'.txt', '.csv'等
    :return: 包含符合条件文件绝对路径的列表
    """
    files_list = []
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

if __name__ == '__main__':
    directory = r"F:\AndriodBackup\resiliosync\jpg\ai_generate\ai"
    script_path = os.getcwd()
    # print(txt_path)
    content = find_files_with_extension(directory, '.png')
    save_list_to_txt(content, 'output.txt')