''' @Author: liangmingdong  
 @Date: 2023-06-30 21:10:37  
 @Last Modified by:   liangmingdong  
 @Last Modified time: 2023-06-30 21:10:37 
 '''
import codecs


def tran(path):
# 读取 GB2312 编码的文件内容
    with codecs.open(path, 'r', 'gb2312') as file:
        content = file.read()

    # 将内容以 UTF-8 编码写入新文件
    with codecs.open(path, 'w', 'utf-8') as file:
        file.write(content)

tran(r"F:\AndriodBackup\resiliosync\tts-vue\novel\催眠眼镜.txt")