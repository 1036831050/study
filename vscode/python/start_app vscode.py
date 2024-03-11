# -*- coding = utf-8 -*-
# @Auther:lmd
# @Time    :2023/3/3--16:03
# @File    :start_app.py
# @Software:PyCharm
import time
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
import random
# from ..appname import getpackages


class Mytest:

    def __init__(self, appname, activity, ip):
        self.caps = {
            "platformName": "Android",  # 被测手机是安卓
            "platformVersion": "9",  # 手机安卓版本
            f"deviceName": "{ip}",  # 设备名，安卓手机可以随意填写
            "appPackage": "com.kuaishou.nebula",  # 启动APP Package名称
            "appActivity": "com.yxcorp.gifshow.HomeActivity",  # 启动Activity名称
            "unicodeKeyboard": True,  # 使用自带输入法，输入中文时填True
            "resetKeyboard": True,  # 执行完程序恢复原来输入法
            "noReset": True,  # 不要重置App
            "newCommandTimeout": 6000,
            "automationName": "UiAutomator2"
        }

        # 连接Appium Server，初始化自动化环境
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.caps)
        # 设置缺省等待时间
        self.driver.implicitly_wait(5)
        self.driver.press_keycode(164)
        self.size = self.driver.get_window_size()

    def tearDown(self, ip):
        self.driver.quit()

    def text2click(self, text, class_name):
        position = f'new UiSelector().text("{text}").className("{class_name}")'
        # print(position)
        result = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, position)
        return result

    def duck(self):
        # 点红包按钮
        while True:
            try:
                red_package = self.driver.find_element(By.ID, 'circular_progress_bar')
                # red_package = self.driver.find_element(By.ID, 'piggy_bank_progress_bar')
                # red_package = self.driver.find_element(By.ID, 'expand_btn_text')
                if red_package:
                    red_package.click()                   
                    print("点击红包")
                    break
            except:
                print("except:未找到，开始上滑")
                self.re_swi(1, 1)
        # 处理跳出签到弹窗
        # try:
        #     sign_day = self.text2click("立即签到", "android.view.View")
        #     if sign_day:
        #         sign_day.click()
        #         self.driver.tap(self.size["width"]//2, self.size["height"]*791//1000, 500)
        #     print("success to click 'x'")
        # except Exception as e:
        #     print("pass签到")
        # 点duck按钮
        time.sleep(1)
        print("开始选找duck按钮...")
        i = 0
        while True:
            if i >= 20:
                break
            try:
                duck = self.text2click("duck", "android.widget.Image")
                if duck:
                    duck.click()
                    time.sleep(0.5)
                    print("成功点击duck！")
                    break
                else:
                    print("未找到")
            except:
                i += 1
        # duck签到
        try:
            duck_p = self.text2click("立即签到", "android.widget.Button")
            if duck_p: 
                print("开始签到")
                duck_p.click()
                print("点x")
                self.driver.find_element(AppiumBy.XPATH,
                                         '//*[@resource-id="com.kuaishou.nebula:id/webView"]/com.kuaishou.webkit'
                                         '.WebView/android.webkit.WebView/android.view.View[3]/android.view.View['
                                         '3]/android.view.View[1]/android.widget.Image[2]').click()
                print("success to click 'x'")
        except:
            print("无签到弹窗，pass")
            pass
        time.sleep(2)

    def duck_swi(self, counts) -> None: 
        for i in range(counts):
            # 点击领取饲料
            feed = self.text2click("领取饲料", "android.widget.Button")
            feed.click()
            # 点击去观看
            look = self.text2click("去观看", "android.widget.Button")
            look.click()
            time.sleep(1)
            print(f"第{i}次滑动")
            self.re_swi(38, 3)
            # 点击任务完成
            i = 0 
            while i <= 20:
                try:
                    commit = self.driver.find_element(By.ID, 'pendant_bg')
                    if commit:
                        commit.click()
                        break
                    else:
                        self.re_swi(1, 1)
                except:
                    i += 1

    def duck_advance(self, counts, ms) -> None:
        time.sleep(2)
        for i in range(counts):
            # 点击领取饲料
            feed = self.text2click("领取饲料", "android.widget.Button")
            feed.click()
            # 点击去观看
            print(f"点击第{i}次广告")
            look = self.text2click("去观看", "android.widget.Button")
            look.click()
            time.sleep(ms)
            back = self.driver.find_element(By.ID, 'com.kuaishou.nebula.neo_video:id/video_countdown_end_icon')
            if back:
                back.click()
        
    def feed_action(self, counts) -> None:
        time.sleep(2)
        self.re_swi(1, 4, "d")
        for i in range(counts):
            width = self.size["width"]*868//1000
            height =self.size["height"]*665//1000
            # print(self.size["width"], self.size["height"])
            # print(width, height)
            print(f"喂养第{i}次")
            self.driver.tap([(width, height)], 500)
            time.sleep(4)


    def other(self):
        # 青少年模式的“我知道了”按钮
        self.driver.find_element(By.ID, 'com.kuaishou.nebula:id/positive')

    def re_swi(self, counts, ms, ward="u"):
        self.driver.implicitly_wait(2)
        width = self.size["width"]
        height = self.size["height"]
        if ward == "d":
            for i in range(counts):
                print(f"第{i+1}次下拉")
                self.driver.swipe(width // 2, height // 10 * 3, width // 2, height // 10 * 9, duration=500)
                time.sleep(ms)
        else:
            for i in range(counts):
                print(f"第{i+1}次上滑")
                self.driver.swipe(width // 2, height // 10 * 9, width // 2, height // 10 * 4, duration=500)
                time.sleep(ms)


def testadb(ip):
    result = os.system(f"adb devices |grep {ip}")
    print(result)
    if result != 0:
        while True:
            try:
                print(os.system(f"adb connect {ip}:5555"))
                os.system(f"adb -s {ip} shell pm enable io.appium.settings")
                os.system(f"adb -s {ip} shell pm enable com.kuaishou.nebula")
                break
            except:
                print("未找到设备，请打开adb端口")
                time.sleep(3)
    


# appname, activity = getpackages.name2packages("快手极速版")
appname, activity = "com.kuaishou.nebula", "com.yxcorp.gifshow.HomeActivity"
ip = "192.168.1.105"
testadb(ip)
sign = Mytest(appname, activity, ip)
try:
    time.sleep(1) 
    sign.duck() # 进入duck页面
    # sign.duck_swi(5) #滑动5次
    # sign.duck_advance(5, 30) #看广告5次 
    # sign.re_swi(1,2,ward="d")
    # sign.feed_action(5) # 喂养10次
    sign.re_swi(200, 10)
    print("滑动完成")
    time.sleep(2)
except Exception as e:
    print(f"error:{e}")
finally:
    sign.tearDown(ip)
 
 