import os
import xlwt
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
    df.to_excel(excel_path, index=False)


def create_index(directory, size):
    # 创建 Excel 文件
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("索引")

    # 添加标题行
    sheet.write(0, 0, "文件名")
    sheet.write(0, 1, "路径")

    # 遍历目录下的文件并填写信息到 Excel 文件
    row = 1
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # breakpoint()
            if os.path.getsize(file_path) > size:
                file_size = round(os.path.getsize(file_path)/1024/1024)
                # sheet.write(row, 0, f"{file},大小为:{file_size}M")
                sheet.write(row, 0, file)
                sheet.write(row, 1, file_path)
                row += 1

    # 保存 Excel 文件
    workbook.save("file_to_path.xls")

# 调用函数并传入目录路径
excemple = create_index(r"F:\AndriodBackup\resiliosync\jpg", size=10485760)
write_url("file_to_path.xls")

