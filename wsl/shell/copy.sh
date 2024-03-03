#!/bin/bash
source /etc/profile
#定义查询列表
function display_help()
{
	echo "options 				        | descriptions"
	echo " -h [ --help ]          		| 【帮助】查看帮助列表"
	echo " -d [ --default] 			    | 【默认】更改默认车号"
}
##变量设定脚本默认配置
busid=009
name="梁明东"
city="广州"
location="科学城"
t_time=$(date +%M)
path_desk=/Users/v_liangmingdong/Desktop/
be_name=${city}${location}-BUS${busid}-${name}
af_name=${city}${location}-BUS${busid}-${name}
##更改默认配置
case "$1" in
	-d | --default)
	echo "请输入busid："
	read busid;
	echo "请输入名字:"
	read name;
	;;
	-h | --help)
	display_help
	exit 0
	;;
esac

function change_name(){
	n=`expr $(($1*86400))`
	cp ${path_desk}`date +%F`-${be_name}.xlsx ${path_desk}excel/
	mv ${path_desk}`date +%F`-${be_name}.xlsx ${path_desk}$(date -r $(expr $(date '+%s') + ${n}) +%Y%m%d)-${af_name}.xlsx
	echo "日期变更完成.当前表格为："
	n_name=`ls ~/Desktop/*-BUS*-*.xlsx`
	echo ${n_name##*/}
}


#流程开始
while :
do
##获取桌面上表格的名称
e_name=`ls ~/Desktop/*-BUS*-*.xlsx`
##读取今天要操作的表格名称
d_name=${path_desk}`date +%F`-${af_name}.xlsx
#echo $e_name
#echo $d_name
if [ $e_name = $d_name  ];then
	week=$(date +%w)
	hour=$(date +%H)
	echo "今天是周"${week}";现在是"${hour}"点"
	if [ ${week} -lt 5 ];then
		if [ ${hour} -lt 16 ];then 
			change_name 0
		else
			change_name 1
		fi
	elif [ ${week}  -eq 5 ];then
		if [ ${hour} -lt 16 ];then
			change_name 0
		else
			change_name 3
		fi
	elif [ ${week}  -eq 6 ];then
		change_name 2
	elif [ ${week}  -eq 7 ];then
		change_name 1
	fi
	say 表格已更新
	exit 0
else
	echo "日期错误,矫正中..."
	mv ~/Desktop/*-BUS*-*.xlsx  ${d_name}
fi
done
say 表格已更新
