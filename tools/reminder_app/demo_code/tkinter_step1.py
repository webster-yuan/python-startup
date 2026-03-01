import tkinter as tk
from tkinter import messagebox


def say_hello():
    print("按钮被打印了")


def get_text():
    # 因为 Python 是动态语言：
    # 变量类型是运行时确定的。
    # entry 变量不是参数，不是局部变量，来自外部作用域，会动态推断它的类型
    content = entry.get()
    print(f"输入的内容是：{content}")


def get_text2(entry_param):
    content = entry_param.get()
    print(f"输入的内容是：{content}")


def show_popup():
    messagebox.showinfo("提示", "任务时间到了")


if __name__ == '__main__':
    # 创建主窗口，创建窗口对象
    root = tk.Tk()
    # 设置窗口主题
    root.title("first window")
    # 设置窗口大小
    root.geometry("300x300")
    # 创建一个label组件
    label = tk.Label(root, text="第一个GUI程序")
    # 把它放进窗口里面
    label.pack()
    button = tk.Button(root, text="点我", command=say_hello)  # 传入函数名，作为回调函数时才会触发
    button.pack()

    # 单行输入框组件
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(root, text="获取内容", command=get_text)
    button.pack()

    button1 = tk.Button(root, text="获取内容", command=lambda: get_text2(entry))
    # 使用lambda将一个有参数的函数，创建了一个新的函数，延迟执行
    # lambda记住了外部的变量，叫做闭包
    # 否则使用command= get_text2(entry) 会立即执行get_text2(entry)，和预期出发button时回调get_text2(entry)时不符
    button1.pack()

    # 弹窗
    button2 = tk.Button(root, text="弹窗提示", command=show_popup)
    button2.pack()
    root.mainloop()
