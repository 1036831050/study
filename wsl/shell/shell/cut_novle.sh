#!/usr/bin/bash

name=${1##*/}
path=${1%/*}
#echo $path
#echo $name
num=$(nl ${path}/${name} |sed -n '/第.章/p' |wc -l)
echo $num
row=$(cat -n ${path}/${name}  |grep '第.章'|awk '{print $1}')
echo ${row}
function tran(){
n=1
for i in $1;
do
	echo $i
	list[n]=$i;
	n=$(expr $n + 1 )
done
}
tran $row
echo $list
for ((i=1;i<=${num};i++));
do
	echo ${list[${i}]};
done
