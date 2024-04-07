# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/2/25--17:21
# @File    :down_novel.py
# @Software:PyCharm

from my_utls import spider as sp
from lxml import etree
import re


def chapter_link(url):  # 通过page获取章节链接
    result = get_etree(url)
    try:
        c_title = result.xpath('//tbody/tr/td/a[@class="subject" and @target="_blank"]/text()')
        d_link = result.xpath('//tbody/tr/td/a[@class="subject" and @target="_blank"]/@href')
    except Exception as e:
        print('error,fail to get link:{}'.format(e))

    d_link = sp.link2url(baseurl, d_link, result)
    return d_link
    # print(d_link, c_title)


def get_etree(url): # 转换到xpath模式
    html = sp.ask_url(url)
    result = etree.HTML(html)
    return result


def down_chapter(chapter_url):  # 根据url获取网页小说内容，返回内容和标题
    html = sp.ask_url(chapter_url)
    result = etree.HTML(html)
    content = []
    title = []
    try:
        title = result.xpath('//*[@id="subject_tpc"]/text()')
        content = result.xpath('//*[@id="read_tpc"]/text()')
    except Exception as e:
        print('\nerror:{},链接网页失败'.format(e))
        pass
    # print(content, title)
    return content, title


def save_novel(content, title, path='.'): # 保存小说内容
    with open("{}/{}.txt".format(path, title[0]), 'w', encoding='utf-8') as f:
        f.write(title[0] + '\n')
        for i in range(1, len(content)):
            f.write(content[i])
    return 0


def line(content):  # 为小说换行
    for i in range(len(content)):
        content[i] = re.sub(r'。', '。\n', content[i])
    return content


def down_novel(url, path, count): # 通过url和path下载到本地
    # 1、获取章节链接，链接为列表形式
    chapter_url = chapter_link(url)
    # 2、通过章节链接获取内容和标题
    j = 1
    for i in chapter_url:

        try:
            content, title = down_chapter(i)
            print("\r开始下载第{}页的第{}条,链接为：{},标题为：{}".format(count, j, i, title[0]), end="", flush=True)
        except Exception as e:
            print('内容获取失败：{},链接为{}'.format(e,i))
            continue
        # 3、加上换行符
        content = line(content)
        # 4、保存到本地
        save_novel(content, title, path)
        j += 1


def main(burl, fir, end):
    for count in range(fir, end):
        url = burl.format(count)
        down_novel(url, path, count)
    return url


if __name__ == '__main__':
    # url = "https://bbs23.zhaosheng5.com/2048/thread.php?fid-54-page-4.html"
    baseurl = "https://bbs23.zhaosheng5.com/2048/"
    burl1 = baseurl + "thread.php?fid-54-page-{}.html"
    print(burl1)
    burl = 'https://bbs23.zhaosheng5.com/2048/thread.php?fid-54-page-{}.html'
    path = './novel'
    main(burl, 2, 3)


