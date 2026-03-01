import json
import os.path
import tkinter as tk
from tkinter import messagebox

tasks = []


def show_popup():
    task_text = "\n".join(tasks)
    messagebox.showinfo("任务列表", task_text)


def add_task(entry_widget, list_box_widget):
    task = entry_widget.get().strip()

    if not task:
        messagebox.showerror("错误", "任务列表不能为空")
        return

    tasks.append(task)
    # 将输入框内容清空
    entry_widget.delete(0, tk.END)  # 从第0个字符刷新到最后
    # 将内容添加到输入框
    list_box_widget.insert(tk.END, task)


def delete_task(list_box_widget):
    selected = list_box_widget.curselection()
    if not selected:
        messagebox.showerror("提示", "请选中一个任务")
        return

    index = int(selected[0])
    tasks.pop(index)
    list_box_widget.delete(index)


# bind() 绑定的函数 必须接收一个参数event，
def show_task_detail(event):
    # bind 的函数可以通过 event 拿到组件本身
    listbox_widget = event.widget
    selected = listbox_widget.curselection()
    if not selected:
        return

    index = selected[0]
    task = tasks[index]
    messagebox.showinfo("任务详情", task)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("获取任务")
    root.geometry("500x500")

    # 先给个单行输入框
    entry = tk.Entry(root)
    entry.pack(pady=10)

    # 创建列表组件
    list_box = tk.Listbox(root, height=10)
    list_box.pack(pady=10, fill="both", expand=True)
    # 组件绑定一个事件 widget.bind("事件", 处理函数)，当事件发生时执行这个函数
    list_box.bind("<Double-Button-1>", show_task_detail)

    add_button = tk.Button(root, text="获取task", command=lambda: add_task(entry, list_box))
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="删除task", command=lambda: delete_task(list_box))
    delete_button.pack(pady=5)

    root.mainloop()
