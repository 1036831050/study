#!/bin/bash


if  [ $# -eq 0 ];then
    echo "无参数"
    read -p $'请输入产出目录，例如(/Users/v_liangmingdong/Downloads/6.3.2.220): \n' path
    read -p $'主板ip:\n' tar_ip
    read -p $'从板ip:\n' tar_ip2
elif [ $# -eq 2 ];then
    path=$1
    tar_ip=$2
    echo "2参数,参数为：$@"
elif [ $# -eq 3 ];then
    path=$1
    tar_ip=$2
    tar_ip2=$3
    echo "3参数,参数为：$@"
fi
# path="/Users/v_liangmingdong/Downloads/6.3.2.220"
echo "产出路径:${path},主板ip:${tar_ip},从板ip:${tar_ip2}"
tar_path=/mnt/vblkdev3
user=caros
filename=${path##*/}

if [ -z ${tar_ip} ];then
    echo "无ip信息,请重新运行脚本"
    exit 1
fi
if scp -r ${path} ${user}@${tar_ip}:${tar_path}
then
#产出传输到从板
    if [ -n ${tar_ip2} ];then
        ssh ${user}@${tar_ip} "scp -r ${tar_path}/${filename} ${user}@${tar_ip2}:${tar_path}"
    fi
#远程执行解压操作
    ssh ${user}@${tar_ip} "tar -xzvf ${tar_path}/${filename}/output.tar.gz -C ${tar_path}/${filename}/"
    if [ -n ${tar_ip2} ];then
        ssh ${user}@${tar_ip2} "tar -xzvf ${tar_path}/${filename}/output.tar.gz -C ${tar_path}/${filename}/"
    fi
fi