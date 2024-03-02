import os
import xlwt

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
                sheet.write(row, 0, f"{file},大小为:{file_size}M")
                sheet.write(row, 1, file_path)
                row += 1

    # 保存 Excel 文件
    workbook.save("文件索引.xls")

# 调用函数并传入目录路径
create_index(r"F:\AndriodBackup\resiliosync\jpg", size=1048576)

