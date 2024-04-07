# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/2/25--17:26
# @File    :spider.py
# @Software:PyCharm
import urllib.request
import os
import time


def make_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def ask_url(url):  # 获取页面源码
    head = {"User-Agent": "pan.baidu.com"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        res = urllib.request.urlopen(request, timeout=3)
        html = res.read().decode("utf-8")
        # print("获取网页源码成功")
    except Exception as e:
        print("error")
        print(e)
        pass
    return html


def link2url(baseurl, d_link, result):
    dlink = []
    for i in range(len(d_link)):
        print("\r当前进度为--第{}条".format(i + 1), end="", flush=True)
        time.sleep(0.01)
        dlink.append(baseurl + d_link[i])

    return dlink
