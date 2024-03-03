#!/bin/bash
path=~/test

read -p "请输入目标日志:(例如planning相关日志就输入planning)" log_type;
read -p "请输入case时间：(例如12月10日14：32：34输入为1210143234)" all_time;
#read -p "当前用户名为：${user},是否更改用户名(只需要输入一次)：" back;
if [[ ${back} == y ]];then
    read -p "输入新的用户名：" suser;
    echo "当前用户名为：$user 目标用户名为：$suser";
    sed -i '.bak' "s/${user}/${suser}/" test.sh
fi
if [ ${#all_time} -ne 10 ];then
    echo "时间输入错误"
fi
day=${all_time:0:4}
log_time=${all_time:4:6}
#echo $day
#匹配并获取目标日志
function log_patch(){
    #echo $path
    log_list=$(ls -tr ${path}/ |grep  ${log_type}.log.*${day})
    #echo ${log_list}
    count=1
    for i in ${log_list}
    do
        #echo "第${count}次为"${i}
        let count++
        time=$(ls -tr ${path}/${i} |grep ${log_type}.log.*${day}|awk -F- '{print $2}' |awk -F. '{print $1}')
        #echo "时间为："${time}
        if [ ${time} -lt ${log_time} ];then
            log_name=${i}
        fi

    done
    echo ${log_name}
    #echo $tar_log
    #result=$tar_log
}

