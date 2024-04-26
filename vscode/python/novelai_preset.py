from my_utls.novel_opera import openfile


preset_name = r"E:\novelai\novelai-webui-aki\styles.csv"
content = openfile.main(preset_name)
# 把content每个元素以第一个逗号分隔两部分
preset_dict = {}
for line in content:
    # 按照第一个逗号分割字符串
    split_data = line.split(",", 1)
    # 提取分割后的两部分字符
    first_part = split_data[0]
    second_part = split_data[1]
    preset_dict[first_part] = second_part
    print("第一部分字符:", first_part)
    print("第二部分字符:", second_part)

# print(preset_dict)