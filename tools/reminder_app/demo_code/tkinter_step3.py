import json
import os
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.json"


def load_tasks():
    """从JSON文件中加载任务"""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(to_save_tasks):
    """保存到JSON文件"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(to_save_tasks, f, ensure_ascii=False, indent=4)


def show_popup_detail(event):
    listbox_widget = event.widget
    selected = listbox_widget.curselection()
    if not selected:
        messagebox.showerror("提示", "请先选中一个任务")
        return

    index = selected[0]
    task_text = tasks[index]
    messagebox.showinfo("选中任务为:", task_text)


def add_task():
    t = entry.get().strip()
    if not t:
        messagebox.showerror("错误", "任务不能为空")
        return
    tasks.append(t)
    save_tasks(tasks)
    entry.delete(0, tk.END)
    list_box.insert(tk.END, t)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("任务管理器")
    root.geometry("300x300")

    tasks = load_tasks()
    entry = tk.Entry(root)
    entry.pack(pady=10)

    list_box = tk.Listbox(root, height=10)
    list_box.pack(pady=10, fill="both", expand=True)
    # 启动时将任务加载进界面
    for task in tasks:
        list_box.insert(tk.END, task)

    add_button = tk.Button(root, text="添加任务", command=add_task)
    add_button.pack(pady=10)

    list_box.bind("<Double-Button-1>", show_popup_detail)

    root.mainloop()
