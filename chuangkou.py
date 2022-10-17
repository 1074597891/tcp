import tkinter as tk  # 使用Tkinter前需要先导入


def ck(a, b):

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title(a)

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x

    # 第4步，在图形界面上设定标签

    l2 = tk.Label(window, text=b, bg='green', font=('Arial', 12), width=30, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    b1 = 0
    if b1 != b:
        b1 = b
        l2 = tk.Label(window, text=b, bg='green', font=('Arial', 12), width=30, height=2)

    # 第5步，放置标签
    l2.pack()  # Label内容content区域放置位置，自动调节尺寸
    # 放置lable的方法有：1）l.pack(); 2)l.place();

    # 第6步，主窗口循环显示
    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
    # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。


if __name__ == '__main__':
    # a是进程，b是按键
    ck("a", "b")
