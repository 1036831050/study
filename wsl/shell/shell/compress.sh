#!/bin/bash
first=$1
function compre(){
    file=$1
    name=${file##*/}
    path=${file%/*}
    echo $name $path
    tar -cvzPf  ${file}.tar.gz ${file}
}

#compre $1
echo $first
if [ -d ${first} ];then
    list=$(ls -hl ${first} |awk '{print $9}')
    ls -l ${first}|awk '{print $9}' 
    read -p "请输入需要压缩的文件:" opt;
    echo ${first}/${opt}
    compre ${first}/${opt}
elif [ -f ${first} ];then
    compre ${first}
fi