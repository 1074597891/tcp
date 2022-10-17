import keyboard
import pyperclip


def ky():
    while True:
        keyboard.wait(hotkey="ctrl+c")
        keyboard.wait("enter")
        a = pyperclip.paste()
        return a


if __name__ == '__main__':
    while True:
        ky()
