import keyboard
import time
from PIL import ImageGrab


def scap():
    while True:
        # 1、利用QQ截图到剪贴板
        # 输入键盘的触发事件
        keyboard.wait(hotkey="ctrl+alt+a")
        keyboard.wait(hotkey="enter")
        time.sleep(0.1)

        # 2、保存截图
        image = ImageGrab.grabclipboard()
        image.save("screen.png")


if __name__ == '__main__':
    scap()
