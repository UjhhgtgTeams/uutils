#!/usr/bin/python
# -*- coding: utf-8 -*-

# Module Config Zone
SPAM_DISABLE_LIMIT = False
# End of Module Config Zone

"""
An error class for my util lib.
"""
class UutilsModuleError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

"""
A class about messing with two-dimensional lists.
"""
class twoDimList():
    def generate(x, y):
        result = []
        for i in range(x):
            subResult = []
            for j in range(y):
                subResult.append(0)
            result.append(subResult)
        return result

"""
Just a weird test inspired by the 'light bulb problem'.
"""
def lightBulb(interval, duration):
    from time import sleep, strftime, localtime
    if interval >= duration:
        raise UutilsModuleError("interval cannot be bigger or equals duration")
    light_time = 0
    start_time = int(strftime("%S", localtime()))
    current_time = int(strftime("%S", localtime()))
    while current_time != start_time + duration:
        sleep(interval)
        light_time += 1
        current_time = int(strftime("%S", localtime()))
        interval /= 2
    return light_time
        
"""
Clears the screen.
"""
def cls():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Checks whether a number is odd or even.
"""
def isOddNum(num):
    if num % 2 == 0:
        return True
    else:
        return False

"""
Returns the position of the mouse after a set delay.
"""
def getMouseCord(delay = 2):
    import time
    try:
        import pyautogui
    except:
        raise UutilsModuleError("pyautogui module is missing")
    time.sleep(delay)
    return [pyautogui.position().x, pyautogui.position().y]

"""
A multi-usage spam module that uses pyautogui.
Spams emojis (for wemeet app), texts or clicks.

To force stop spamming when bad things happen,
move your mouse to a corner of the screen.
(So do not set 'pause' value to a very low number.)
"""
def spam(interval = 0.1, mode = "click", button = "left", emoji = "clapHands", text = "", setLocation = False, cord = [None, None]):
    import time
    try:
        import pyautogui
    except:
        raise UutilsModuleError("pyautogui module is missing")
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = interval
    if mode == "click":
        while True:
            if setLocation == True:
                gotCord = getMouseCord()
                pyautogui.click(gotCord[0], gotCord[1], button=button)
            else:
                if cord == [None, None]:
                    pyautogui.click(button=button)
                else:
                    pyautogui.click(cord[0], cord[1], button=button)
    elif mode == "text":
        while True:
            pyautogui.typewrite(text, 0.02)
            pyautogui.press("enter")
            time.sleep(interval)
    elif mode == "wemeetEmoji":
        if interval < 0.1 and SPAM_DISABLE_LIMIT == False:
            raise UutilsModuleError("cannot set 'pause' value to lower than 0.1. Set SPAM_DISABLE_LIMIT=True to override this limit.")
        interval = interval / 6
        while True:
            pyautogui.moveTo(93, 943, duration=interval)        # 移到表情选择按钮
            pyautogui.click()                                   # 点开表情选择界面 
            pyautogui.moveTo(274, 793, duration=interval)       # 移到滚动条上
            pyautogui.dragTo(274, 887, duration=interval)       # 拖到界面最下面
            if emoji == "clapHands":                            # "拍手"表情
                pyautogui.moveTo(102, 855, duration=interval)   # 移到表情上
            elif emoji == "ringClock":                          # "闹钟"表情
                pyautogui.moveTo(100, 890, duration=interval)   # 移到表情上
            elif emoji == "raiseHands":                         # "举手"表情
                pyautogui.moveTo(176, 820, duration=interval)   # 移到表情上
            elif emoji == "raiseThumb":                         # "大拇指"表情
                pyautogui.moveTo(211, 820, duration=interval)   # 移到表情上
            elif emoji == "raiseOk":                            # "OK"表情
                pyautogui.moveTo(250, 820, duration=interval)   # 移到表情上
            elif emoji == "dogFace":                            # "狗头"表情
                pyautogui.moveTo(173, 890, duration=interval)   # 移到表情上
            elif emoji == "shockedFace":                        # "不可置信"表情
                pyautogui.dragTo(274, 793, duration=interval)   # 拖回界面最上面
                pyautogui.moveTo(104, 890, duration=interval)   # 移到表情上
            pyautogui.click()                                   # 点击表情
