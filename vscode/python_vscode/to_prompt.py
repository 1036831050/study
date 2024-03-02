import os
import datetime
import shutil
import re
import colorama
from colorama import Fore, Style
import sys


colorama.init()
PATH = r"E:\novelai\novelai-webui-aki"
name = "styles.csv"
pattrn1 = r"(\".+\")"


def r_csv(path, mode="r"):
    with open(path, mode=mode, encoding="utf-8") as f:
        content = f.readlines()
        return content
    
out = r_csv(f"{PATH}/{name}")
# print(out[5])

# 转换str为list
def slpit(content):
    tag = []
    pattern = r'"(.*?)"'  
    name_p = r'^[^,]*'
    try:
        matches = re.findall(pattern, content)
        ac_prompt = matches[0]
        ne_prompt = matches[1]
        tag.append(ac_prompt)
        tag.append(ne_prompt)
    except Exception as e:
        print(e)
    matches = re.findall(name_p,content)
    name = matches[0]
    return name, tag

c = 1
all = {}
for i in out:
    name, tag = slpit(i)
    all.update({name:tag})
    # print(Fore.GREEN + f"行数{c},名称：{name}")
    # print(Fore.MAGENTA  + f"{all[name]} \n")
    c = c + 1

# print(all[input("输入名称:")])
for n in list(all.keys()):
    print(Fore.YELLOW  + n)

while True:
    option = input("请输入名称：")
    keyword = ["q", "quit", "exit", "bye"]
    if option in keyword:
        sys.exit()
    print(all[option])
 