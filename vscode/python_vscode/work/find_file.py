

def find_file_path(file_name, file_paths_file):
    """
    在包含文件绝对路径的文本文件中查找特定文件名对应的路径
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


# 示例用法
# file_name = "00015-2319064845-,,pureerosface_v1,extreme detail description,46-point diagonal bangs,(((1girl_1.3))),Cinematic  Lighting,46-point diagonal bangs"  # 要查找的文件名
# file_paths_file = r"F:\vscode\python_vscode\work\list.txt"  # 包含文件绝对路径的文本文件

# file_path = find_file_path(file_name, file_paths_file)
# if file_path:
#     print(f"文件 '{file_name}' 的路径为：{file_path}")
# else:
#     print(f"未找到文件 '{file_name}' 的路径。")
