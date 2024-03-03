#!/bin/bash
base=6.4.2204.104
read -p " 当前 base 包为：$base,是否重新输入 base 包？(y/n)" back;
if [[ ${back} == y ]];then
    read -p "输入新的base：" sbase;
    echo $base $sbase;
    sed -i "s/${base}/${sbase}/" upgrade.sh
fi

read -p  "请输入目标产出：" tar;
echo "目标产出的差分包名称为：${base}_patch_${tar}"
otaclient --rebase robobus,${base}  && otaclient -i robobus,${base}_patch_${tar}
if [ $? == 0 ];then
    echo "产出更新成功！"
else
    echo "产出更新失败，请检查产出是否输入正确。"
fi
