#!/usr/bin/bash

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


