import pyttsx3 
import datetime
import time

def speak(text):
    # 创建一个语音引擎对象
    engine = pyttsx3.init()

    # 播报文本
    engine.say(text)

    # 等待播报结束
    engine.runAndWait()

def get_current_time():
    # 获取当前时间
    current_time = datetime.datetime.now()

    # 将当前时间格式化为字符串
    time_str = current_time.strftime("%H:%M")

    return time_str

def main():
    while True:
        # 获取当前时间
        current_time = get_current_time()

        # 播报当前时间
        speak("现在的时间是：" + current_time)

        # 每隔一段时间再次播报
        time.sleep(60)  # 每隔 60 秒播报一次

if __name__ == "__main__":
    main()
