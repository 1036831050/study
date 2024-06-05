# 业务空间模型调用请参考文档传入workspace信息: https://help.aliyun.com/document_detail/2746874.html    
        
from http import HTTPStatus
from dashscope import Generation

def call_with_stream(prompt=None):
    messages = [
        {'role': 'user', 'content': prompt}]
    responses = Generation.call("qwen-max",
                                messages=messages,
                                result_format='message',  # 设置输出为'message'格式
                                stream=True, # 设置输出方式为流式输出
                                incremental_output=True,  # 增量式流式输出
                                api_key="sk-dd2b41e59ccc4f6086c681da68ae5e6e",
                                )
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            print(response.output.choices[0]['message']['content'],end='')
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))


def main():
    """主函数，处理用户输入并调用相应功能."""
    quit_commands = {'exit', 'quit', 'q'}  # 使用集合提高查询效率

    print("欢迎使用对话系统！输入内容开始对话，或输入'exit', 'quit', 'q'之一退出。")

    while True:
        user_input = input("您：").strip()  # 去除输入前后空白
        if user_input.lower() in quit_commands:  # 不区分大小写
            print("系统：再见！期待再次为您服务。")
            break
        else:
            try:
                # 假设call_with_stream是处理用户输入的函数，这里调用它
                response = call_with_stream(user_input)
                print(f"系统：{response}")
            except Exception as e:  # 捕获并友好提示异常
                print(f"系统错误：{e}. 请尝试重新输入。")

if __name__ == '__main__':
    main()