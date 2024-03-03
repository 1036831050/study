#!/bin/bash

file3p=~/Desktop/logs/hmi_30/
file4p=~/Desktop/logs/hmi_40/
logs6=/sdcard/hmi_logs/
logs20=/data/data/com.baidu.adt.hmi.robobus.hud32/files/hmi_logs/
file40_name=com.baidu.adt.hmi.robobus.hud32.txt
#/data/data/com.baidu.adt.hmi.robobus.hud/files/hmi_logs/

#排查本地路径
function file3 {
if [ -d ~/Desktop/logs/hmi_30 ];then
        echo "路径已存在，准备获取日志"
else
        echo "路径不存在，创建该路径。"
        mkdir -p  ~/Desktop/logs/hmi_30
        if [ $? != 0 ];then
                echo "创建失败"
        else
                echo "创建成功"
        fi
fi
}

#排查本地路径
function file4 {
if [ -d ~/Desktop/logs/hmi_40 ];then
        echo "路径已存在，准备获取日志"
else
        echo "路径不存在，创建该路径。"
        mkdir -p  ~/Desktop/logs/hmi_40
        if [ $? != 0 ];then
                echo "创建失败"
        else
                echo "创建成功"
        fi
fi
}

#获取当天日志
function Dlogs(){
while :
do
    read -p " 请输入安卓ip:(默认为司机端日志)" ops1;
    if [[ ${ops1} == "30.6" ]] || [ -z ${ops1} ]; then
	file3
        scp root@192.168.30.6:${logs6}hmi_panel-20`date '+%y-%m-%d'`.txt  ${file3p}
	if [ $? == 0 ];then 
		echo "日志已保存到${file3p}目录"
	else
		echo "日志下载失败。"
	fi	
        break
    elif [ $ops1 == "40.21" ];then
	file4
	adb connect 192.168.40.21
	adb root
	if [ $? == 0 ];then
		sleep 1s
        	adb pull ${logs20}hmi_hud_main_20`date '+%y_%m_%d'`_${file40_name} ${file4p}
                if [ $? == 0 ];then
                        ehco "日志获取成功！
                        已保存到${file4p}目录！"
                fi
	fi
        break
    elif [ $ops1 == "40.20" ];then
	file4
	adb connect 192.168.40.20
	adb root
	if [ $? == 0 ];then
		sleep 1s
                adb pull ${logs20}hmi_hud_main_20`date '+%y_%m_%d'`_${file40_name} ${file4p}
                if [ $? == 0 ];then
                        echo "日志获取成功!目录为：\n${file4p}"
                fi
	fi
        break
    else 
	echo "ip 输入错误，请重新输入。参考格式为（30.6）"
    fi
done
}

#获取指定日期日志
function dlogs(){
while :
do
        month=$1
        day=$2
        echo $month $day
        echo " 请输入安卓ip:"
        read ops1;
        if [ $ops1 == "30.6" ]; then
                file3
                scp root@192.168.30.6:${logs6}hmi_panel-20`date '+%y'`-${month}-${day}.txt  ${file3p}
	        if [ $? == 0 ];then 
	        	echo "日志已保存到${file3p}目录"
	        else
	        	echo "日志下载失败。"
	        fi	
               break
        elif [ $ops1 == "40.21" ];then
        	file4
        	adb connect 192.168.40.21
        	adb root
        	if [ $? == 0 ];then
        		sleep 1s
                	adb pull ${logs20}hmi_hud_main_20`date '+%y'`_${month}_${day}_${file40_name} ${file4p}
                        if [ $? == 0 ];then
                                ehco "日志获取成功！
                                已保存到${file4p}目录！"
                        fi
        	fi
                break
        elif [ $ops1 == "40.20" ];then
        	file4
        	adb connect 192.168.40.20
        	adb root
        	if [ $? == 0 ];then
        		sleep 1s
                        adb pull ${logs20}hmi_hud_main_20`date '+%y'`_${month}_${day}_${file40_name} ${file4p}
                        if [ $? == 0 ];then
                                echo "日志获取成功!已保存到${file4p}目录！"
                        fi
        	fi
                break
        else 
        	echo "ip 输入错误，请重新输入。参考格式为（30.6）"
        fi
done
}
#定义压缩方法
function ta(){
    if [ -z $1 ] && [ -z $2 ];then
        month=$(date +%m)
        day=$(date +%d)
    elif [ $1 -ge 20 ];then
        month=$(date +%m)
        day=$(date +%d)
    else
        month=$1
        day=$2
    fi
    if [[ $3 == 30 ]] || [[ $1 == 30 ]];then
        tar -cvzPf ${file3p}hmi_panel-20`date '+%y'`-${month}-${day}.tar.gz  ${file3p}hmi_panel-20`date '+%y'`-${month}-${day}.txt
    elif [[ $3 == 40 ]] || [[ $1 == 40 ]];then
        tar -cvzPf ${file4p}hmi_hud_main_20`date '+%y'`_${month}_${day}_com.baidu.adt.hmi.robobus.hud.tar.gz  ${file4p}hmi_hud_main_20`date '+%y'`_${month}_${day}_com.baidu.adt.hmi.robobus.hud.txt
    fi
}
#定义列表
function display_help()
{
	echo "options 				        | descriptions"
	echo " -h [ --help ]          		        | 【帮助】查看帮助列表"
	echo " -d [ --default] 			        | 【默认】更改默认日期"
        echo " -t [ --tar] 			        | 【压缩】默认压缩当天日志(-t 30/40)，指定日志格式：-t 月 日 30/40"
}


#流程开始
#判断后置参数是否为空，为空则默认当天日志
if [ -z $1 ];then
        Dlogs
    	read -p "是否直接打开目录？(y/n)" opt;
	if [[ ${opt} ==  "y" ]];then 
		echo ${opt}
		open ${file4p}
	else
		echo ${opt}
		echo "日志获取结束"
    	fi
fi
#更改默认配置
case "$1" in
#获取指定日期日志
	-d | --default)
        read -t 5 -p "请输入需要的日志日期：" ops
        month=${ops:0:2}
        day=${ops:2:3}
        dlogs $month $day
        exit 0
	;;
        #获取帮助列表
	-h | --help)
	display_help
	exit 0
	;;
        -t | --tar)
	if [ -z $2 ];then
                ta $2;
        else
                month=$2
                day=$3
                ch=$4
                ta $month $day $ch;
        fi
	exit 0
	;;
        -* | --*)
        echo "参数错误，请重新输入"
        ./hmi_log.sh
        exit 0
        ;;
esac

