#!/usr/bin/bash

write_csv(){
    local name="scence_cfg.csv"
    [ -f $name ] && rm $name
    echo "$(dirname $(pwd))" | sed 's#/$##' >> $name
    echo "$(basename $(pwd)),all" >> $name
}

data_path=$1

if [ $# -lt 1 ]; then
    echo "bash simple.sh <bagfile_path>"
    exit 1
fi

count=0
suffix="*.sh"
# 获取指定目录下所有指定文件的文件名并进行排序和去重处理
file_names=$(find "$data_path" -name $suffix -type f -exec basename {} \; | tr ' ' '\n' | sort -u)

cd "$data_path"
echo -e "\033[34m data path:${PWD}正在写入中:\033[0m"

if [[ -e scenes.csv ]]
then
  rm scenes.csv
fi

for file_name in $file_names
do

  original_string=$file_name
  IFS="_" read -ra parts <<< "$original_string"
  unset parts[${#parts[@]}-1]
  unset parts[${#parts[@]}-1]
  new_string=$(IFS="_"; echo "${parts[*]}")
  
  # echo "最新的字符串为： $new_string"
  # processed_name=$(echo "$file_name" | rev | cut -d '_' -f3-5 | rev)
  file_path=$(find "$data_path" -name "$file_name" -type f | sed "s|$data_path/||")
  echo "$file_path,$new_string" >> scenes.csv
  echo -e "\033[0;32msuccessfully writting to csv：$((count+=1)),$file_name \033[0m"
done

# 添加序号列
awk 'NF > 0 {print NR "," $0}' scenes.csv > tmp.csv
mv tmp.csv scenes.csv

echo -e "\033[34m ====== 写入完成 ====== \033[0m"
