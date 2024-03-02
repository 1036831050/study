import os
import json
import download

def geturl():
    # 通过空格将两个参数连接起来
    user_input = input("请输入两个参数，用空格分隔：")
    # 使用空格分割参数
    try:
        param1, param2 = user_input.split()
        return param1, param2
    except:
        print("输入格式错误，退出脚本")

with open("list.txt", "r")as f:
    content = json.load(f)


# content[f"{param1}"] = f"{param2}"
newdict = {}
while True:
    try:
        title,url = geturl()
    except:
        break
    newdict[f"{title}"] = f"{url}"

print(newdict)
# print(content)
content.update(newdict)
# print(content)

with open("list.txt", "w")as f:
    json.dump(content, f)

download.main()