#!/bin/bash
export LANG=en_US.UTF-8
# echo $1
ip=$1
# rsync -Pavh --delete -e 'ssh -p 8022' ${ip}:/sdcard/hmi/feedback/video/ /Users/v_liangmingdong/Desktop/hmi_feedback/video
ANDROID_PATH=/sdcard/hmi/feedback/video/
MAC_PATH=/Users/v_liangmingdong/Desktop/hmi_feedback/
while true
do
if [ $# -eq 0 ];then
    echo "请输入ip"
fi
if [ $# -eq 1 ] && [[ $1 =~ ^[0-9] ]];
then
    echo "start convert..."
    ip=$1
    rsync -Pavh --delete -e 'ssh -p 8022' ${ip}:${ANDROID_PATH} ${MAC_PATH}
    exit 0
else
    case $1 in
        -h)
        echo "display help list..."
        echo "-d --------------------base mac delete android"
        echo "-dn -------------------display base mac delete android"
        echo "-n --------------------display base android delete mac"
        echo "ip --------------------base android delete mac"
        exit 0
    esac
fi
if [ $# -eq 2 ] && [[ $1 =~ ^[0-9] ]];then
    case $2 in
        -d)
            echo "start delete..."
            rsync -Pavh --delete -e 'ssh -p 8022' ${MAC_PATH} ${ip}:${ANDROID_PATH} 
            exit 0
            ;;
        -dn)
            echo "prew..."
            rsync -Pavhn --delete -e 'ssh -p 8022' ${MAC_PATH} ${ip}:${ANDROID_PATH} 
            exit 0
            ;;
        -n)
            echo "prew..."
            rsync -Pavhn --delete -e 'ssh -p 8022' ${ip}:${ANDROID_PATH}  ${MAC_PATH}
            exit 0
        esac
fi

echo "参数错误，请输入正确参数"
exit 1
done