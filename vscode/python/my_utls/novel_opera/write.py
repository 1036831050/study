import pandas as pd

def write_url(excel_path):
    # 读取 Excel 文件
    df = pd.read_excel(excel_path)

    # 遍历文件名和路径，并将路径转换为超链接
    for index, row in df.iterrows():
        file_path = row['路径']
        file_name = row['文件名']

        # 创建超链接字符串
        hyperlink = f'=HYPERLINK("{file_path}", "{file_path}")'

        # 更新路径列为超链接
        df.at[index, '路径'] = hyperlink

    # 保存修改后的 Excel 文件
    df.to_excel("new.xls", index=False)

write_url("file_to_path.xls")
