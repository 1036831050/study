import tkinter as tk
from tkinter.scrolledtext import ScrolledText
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
    chat_output.insert(tk.END, response.json()['choices'][0]['message']['content'] + "\n")
    logger.info(response.json()['choices'][0]['message']['content'])

def handle_input():
    user_input = input_entry.get().strip()
    if user_input.lower() in quit_commands:
        chat_output.insert(tk.END, "GPT: 再见！期待再次为您服务。\n")
        root.quit()
    try:
        call_with_stream(user_input)
    except Exception as e:
        chat_output.insert(tk.END, f"系统错误：{e}. 请尝试重新输入。\n")
    input_entry.delete(0, tk.END)

def main():
    global root, input_entry, chat_output, quit_commands
    root = tk.Tk()
    root.title("对话系统")

    # 设置中文字体
    font = ("Microsoft YaHei", 12)

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    input_entry = tk.Entry(input_frame, width=50, font=font)
    input_entry.pack(side=tk.LEFT, padx=5)
    input_entry.bind("<Return>", lambda event: handle_input())
    input_entry.focus()

    send_button = tk.Button(input_frame, text="发送", command=handle_input, font=font)
    send_button.pack(side=tk.LEFT, padx=5)

    chat_output = ScrolledText(root, width=60, height=20, font=font)
    chat_output.pack(padx=10, pady=10)

    quit_commands = {'exit', 'quit', 'q'}

    root.mainloop()

if __name__ == '__main__':
    main()
