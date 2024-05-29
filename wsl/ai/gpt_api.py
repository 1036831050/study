import sys
import requests
from model import setup_logger


def call_with_stream(prompt="Hello!", logger=None):
    if logger is None:
        logger = setup_logger()
    url = "https://api.deepbricks.ai/v1/chat/completions"
    full_response = "" 
    body = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = requests.post(url, headers={
        "Authorization": "Bearer sk-2dZObLpOgdlb5AE9GJXwnEUd5ocLGY90nDnhp2TQmErRDW8m"
        }, json=body)
    print(response.json()['choices'][0]['message']['content'])
    logger.info(response.json()['choices'][0]['message']['content'])


def main():
    """主函数，处理用户输入并调用相应功能."""
    quit_commands = {'exit', 'quit', 'q'}  # 使用集合提高查询效率
    print("欢迎使用对话系统！输入内容开始对话，或输入'exit', 'quit', 'q'之一退出。")

    while True:
        print("用户输入:")
        lines = sys.stdin.read()  # 读取用户输入
        # lines = [line.strip() for line in lines]  # 去除每行前后空白    
        # user_input = custom_input().strip()  # 去除输入前后空白
        if lines.strip() in quit_commands:  # 不区分大小写
            print("GPT:再见！期待再次为您服务。")
            break
        try:
            # 假设call_with_stream是处理用户输入的函数，这里调用它
            print("GPT:", end="")
            call_with_stream(' '.join(lines))
        except Exception as e:  # 捕获并友好提示异常
            print(f"系统错误：{e}. 请尝试重新输入。")

if __name__ == '__main__':
    main()
