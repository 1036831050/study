#!/home/lmd/miniconda3/bin/python
# 业务空间模型调用请参考文档传入workspace信息: https://help.aliyun.com/document_detail/2746874.html    
        
from http import HTTPStatus
import os
import sys
from dashscope import Generation
import logging
from datetime import datetime
from model import setup_logger


def call_with_stream(prompt=None, logger=None):
    if logger is None:
        logger = setup_logger()
    
    messages = [{'role': 'user', 'content': prompt}]
    full_response = ""  # 初始化一个变量来累积完整的响应内容
    responses = Generation.call("qwen-max",
                                messages=messages,
                                result_format='message',
                                stream=True,
                                incremental_output=True,
                                api_key="sk-dd2b41e59ccc4f6086c681da68ae5e6e",
                                )
    
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            increment = response.output.choices[0]['message']['content']
            full_response += increment  # 累积每次的增量输出
            # 注意：这里暂时不打印，等待完整响应累积完毕后再统一处理
            
        else:
            error_message = 'Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            )
            print(error_message)
            logger.error(error_message)
            break  # 遇到错误停止累积响应
    
    # 所有响应累积完成后，一次性打印和记录日志
    print(full_response, end='')
    logger.info(full_response)


def main():
    """主函数，处理用户输入并调用相应功能."""

    print("欢迎使用对话系统！输入内容开始对话，或输入'exit', 'quit', 'q'之一退出。")

    while True:
        print("\n用户输入:")
        user_input = sys.stdin.read() 
        try:
            # 假设call_with_stream是处理用户输入的函数，这里调用它
            print("GPT:", end="")
            call_with_stream(user_input)
        except Exception as e:  # 捕获并友好提示异常
            print(f"系统错误：{e}. 请尝试重新输入。")

if __name__ == '__main__':
    main()
