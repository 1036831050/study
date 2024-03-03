
file_path=$1
tofile_path=$2
function nsync(){
	file=$(find ${file_path}/* -newer ${file_path}/temp_file)
	if [[ -z ${file} ]];then
		echo "目标文件夹内无更新文件"
		touch ${file_path}/temp_file
	else	
		echo -e "更新文件为\n${file}"
		cp -r ${file} ${tofile_path}
		touch ${file_path}/temp_file
	fi
}
nsync
