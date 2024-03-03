#!/usr/bin/bash
# 作用是遍历指定目录下的所有文件，将每个文件的完整路径写入到指定目录下的 output.txt 文件中

while :
do
	file_path=$1
	nu=$(ls ${file_path}|wc -l)
	for ((num=1;num<=${nu};num++));
	do
		rows=$(ls ${file_path} |awk "NR == ${num} {print}")
		#echo $rows
		filename=${file_path}/${rows}
		echo ${filename}
		echo "${filename}" >> ${file_path}/output.txt 
	done
	break
done


