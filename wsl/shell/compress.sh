#!/bin/bash

# 获取第一个命令行参数
first=$1

# 定义压缩函数
function compre(){
    file=$1
    # 提取文件名和路径
    name=${file##*/}
    path=${file%/*}
    echo "$name $path"
    # 压缩文件或目录为 tar.gz 格式
    tar -cvzPf  ${file}.tar.gz ${file}
}

# 输出第一个命令行参数
echo $first

# 如果第一个参数是目录
if [ -d ${first} ]; then
    # 列出目录中的文件
    list=$(ls -hl ${first} | awk '{print $9}')
    ls -l ${first} | awk '{print $9}'
    # 提示用户输入需要压缩的文件名
    read -p "请输入需要压缩的文件:" opt;
    echo ${first}/${opt}
    # 调用压缩函数对指定文件进行压缩
    compre ${first}/${opt}
# 如果第一个参数是文件
elif [ -f ${first} ]; then
    # 调用压缩函数对指定文件进行压缩
    compre ${first}
fi


