# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/3/24--22:17
# @File    :get_image_url.py
# @Software:PyCharm
import requests
from lxml import etree
import os
from datetime import datetime

def writing(content, name="html.txt"):
    with open(name, "w+", encoding="utf-8")as f:
        f.write(content)


def get_link(url, head, cookies):
    result = requests.get(url, cookies)
    print(result.status_code)
    html = etree.HTML(result.content)
    # print(result.encoding)
    writing(result.content.decode('ISO-8859-1'))
    title_link = html.xpath('//*[@id="read_tpc"]/text()')
    if len(title_link) == 0:
        print("title获取失败")
    return title_link


head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"}

cookies = {
       'Cookie': '__utmc=1; __utmz=1.1692974895.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cdb3_smile=1D1; cdb3_sid=hyMSWW; cdb3_cookietime=315360000; cdb3_auth=zxqLiokkviVFzNdmapsHbZPOaYYQxqJzs26lG9zMkKlnBTfEuV2C7SJrmKWyuckMEIY; cdb3_fid322=1693318200; cdb3_fid71=1693221536; __utma=1.900019185.1692974895.1693318287.1693393295.4; cdb3_oldtopics=D9626955D7004613D9632483D; __utmt=1; __utmb=1.7.10.1693393295'
}
# url = "http://174.127.195.180/bbs/forum-322-1.html"
url = "https://pbs.8jva2.org/2048/state/p/51/2304/9736635.html"
# url = "http://174.127.195.180/bbs/thread-9626955-1-1.html"
print(get_link(url, head, cookies))


# def combine_path(p1, p2):
#     path = os.path.join(p1, p2)
#     if not os.path.exists(path):
#         os.mkdir(path)
#     return path


# def down_image(pic_list, title_list, path):
#     i = 0
#     path = combine_path(path, title_list[0])
#     for item in pic_list:
#         i += 1
#         now = datetime.now().strftime('%H%M%S')
#         filename = f"{i}.jpg"
#         if os.path.exists(os.path.join(path, filename)):
#             continue
#         else:
#             print(f"{title_list[0]}的{i}个已存在，跳过")
#         response = requests.get(item)
#         print(f"开始下载{title_list[0]}的第{i}个,网页：" + url)
#         with open(f"{path}/{filename}", "wb") as f:
#             f.write(response.content)
#     with open(f"{path}/url.txt", "w") as f:
#         f.write(url)


# def main(get_url, down_path):
#     head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                           "Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"}
#     pic_list, title_link = get_link(get_url)
#     down_image(pic_list, title_link, down_path)


# if __name__ == "__main__":
#     url = input("url:")
#     main(url, down_path=r"E:\desktop\pic")
