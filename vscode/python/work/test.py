import re

# 给定的字符串
text = "target_id_jump-tool_v0.7_track_6.2g_v1420_fusion_6.2g_v1280_app_030-tuan_ETC882_2024-01-29-12-07-21_3.bag-9163-fr"

# 使用正则表达式匹配目标部分
# match = re.search(r'(?<=-)((tuan|sikeda)_\w+_\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}_\d{1,2}\.bag)', text)
match = re.search(r'(?<=-)((tuan|sikeda)_\w+_\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}_\d{1,2})(\.bag)?', text)


if match:
    target = match.group(0)
    print("匹配到的目标部分:", target)
else:
    print("未找到匹配的目标部分")
