#!/system/bin/sh
export LANG=en_US.UTF-8
VEDIO_PATH=/storage/emulated/0/hmi/feedback/video
D_TIME=$(date +%m%d)

if [ -d "${VEDIO_PATH}/${D_TIME}" ];then
    echo "info: 今天目录已存在"
else
    mkdir -p ${VEDIO_PATH}/${D_TIME}
fi

if [ -f "${VEDIO_PATH}/*.mp4" ];then
    echo "start move movie..."
    mv ${VEDIO_PATH}/*.mp4 ${VEDIO_PATH}/${D_TIME}
else
    echo "无相关视频"
fi