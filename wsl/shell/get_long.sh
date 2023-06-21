#!/bin/bash
export LANG=en_US.UTF-8
echo $1
# filename=$1
filename=$(echo $1 | iconv -f GBK -t UTF-8)
time=$(ffmpeg -i ${filename} 2>&1 | grep "Duration" | awk '{print $2}' | awk '{sub(",","",$NF); print $NF}')
echo $time
