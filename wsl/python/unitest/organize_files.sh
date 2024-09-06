#!/bin/bash

echo "当前目录下文件为："
echo $(realpath .)
read -p "是否继续？(y/n)" opt;

if [[ "$opt" == "y" ]]; then
    # 遍历当前目录下的文件
    for file in *; do
        # 检查是否为文件且是否有后缀
        if [ -f "$file" ] && [[ "$file" == *.* ]]; then
            # 提取文件后缀名
            extension="${file##*.}"
            target_dir="$extension"
            # 创建目录（如果不存在）
            if [ ! -d "$target_dir" ]; then
                mkdir "$target_dir"
            fi

            # 移动文件到对应目录
            mv "$file" "$target_dir/"
        fi
    done
fi