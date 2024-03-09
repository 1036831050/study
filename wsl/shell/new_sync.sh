# 定义输入参数: 源文件夹路径和目标文件夹路径
file_path=$1
tofile_path=$2

# 定义文件同步函数nsync
function nsync() {
  # 使用find命令查找比temp_file更新的文件或文件夹
  file=$(find ${file_path}/* -newer ${file_path}/temp_file)

  # 判断是否找到新文件
  if [[ -z ${file} ]]; then
    echo "目标文件夹内无更新文件"
    # 没有找到新文件时，更新temp_file的时间戳
    touch ${file_path}/temp_file
  else
    echo -e "更新文件为\n${file}"
    # 将找到的新文件或文件夹复制到目标文件夹
    cp -r ${file} ${tofile_path}
    # 更新temp_file的时间戳
    touch ${file_path}/temp_file
  fi
}

# 调用nsync函数执行同步
nsync
