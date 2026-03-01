import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from config import TIME_FORMAT
from reminder_service import ReminderService


class TaskApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.manager = task_manager

        self.root.title("定时任务提醒器")
        self.root.geometry("400x450")

        self.create_ui()
        self.load_listbox()

        self.reminder = ReminderService(root, task_manager)
        self.reminder.start()

    def create_ui(self):
        tk.Label(self.root, text="任务标题").pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack(pady=5)

        tk.Label(self.root, text="截止时间 (2026-03-05 14:00)").pack()
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=5)

        tk.Button(self.root, text="添加任务", command=self.add_task).pack(pady=5)
        tk.Button(self.root, text="删除选中任务", command=self.delete_task).pack(pady=5)

        self.list_box = tk.Listbox(self.root)
        self.list_box.pack(fill="both", expand=True, pady=10)

        self.list_box.bind("<Double-Button-1>", self.show_detail)

    def load_listbox(self):
        self.list_box.delete(0, tk.END)
        for task in self.manager.tasks:
            display = f"{task['title']} | {task['deadline']}"
            self.list_box.insert(tk.END, display)

    def add_task(self):
        title = self.title_entry.get().strip()
        deadline = self.time_entry.get().strip()

        if not title or not deadline:
            messagebox.showerror("错误", "请输入完整信息")
            return

        try:
            datetime.strptime(deadline, TIME_FORMAT)
        except ValueError:
            messagebox.showerror("错误", "时间格式错误")
            return

        self.manager.add_task(title, deadline)
        self.title_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.load_listbox()

    def delete_task(self):
        selected = self.list_box.curselection()
        if not selected:
            messagebox.showerror("提示", "请选择任务")
            return

        index = selected[0]
        self.manager.delete_task(index)
        self.load_listbox()

    def show_detail(self, event):
        selected = self.list_box.curselection()
        if not selected:
            return

        index = selected[0]
        task = self.manager.tasks[index]
        detail = f"任务: {task['title']}\n截止时间: {task['deadline']}"
        messagebox.showinfo("任务详情", detail)
