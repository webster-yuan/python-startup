import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
from config import TIME_FORMAT
from reminder_service import ReminderService


class TaskApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.manager = task_manager

        self.root.title("定时提醒工具")
        self.root.geometry("1000x1000")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6)
        style.configure("TLabel", font=("Microsoft YaHei", 10))

        self.create_ui()
        self.load_listbox()

        self.reminder = ReminderService(root, task_manager)
        self.reminder.start()

    def create_ui(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        input_frame = ttk.LabelFrame(main_frame, text="添加提醒", padding=15)
        input_frame.pack(fill="x")

        ttk.Label(input_frame, text="任务标题").grid(row=0, column=0, sticky="w")
        self.title_entry = ttk.Entry(input_frame, width=40)
        self.title_entry.grid(row=0, column=1, columnspan=3, pady=5)

        ttk.Label(input_frame, text="提醒日期").grid(row=1, column=0)
        self.date_entry = DateEntry(input_frame, date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=1, column=1)

        ttk.Label(input_frame, text="小时").grid(row=1, column=2)
        self.hour_spin = ttk.Spinbox(input_frame, from_=0, to=23, width=5)
        self.hour_spin.set("12")
        self.hour_spin.grid(row=1, column=3)

        ttk.Label(input_frame, text="分钟").grid(row=1, column=4)
        self.minute_spin = ttk.Spinbox(input_frame, from_=0, to=59, width=5)
        self.minute_spin.set("00")
        self.minute_spin.grid(row=1, column=5)

        ttk.Button(input_frame, text="添加提醒", command=self.add_task).grid(
            row=2, column=0, columnspan=6, pady=10
        )

        list_frame = ttk.LabelFrame(main_frame, text="提醒列表", padding=10)
        list_frame.pack(fill="both", expand=True, pady=15)

        self.list_box = tk.Listbox(
            list_frame,
            font=("Microsoft YaHei", 10),
            height=12
        )
        self.list_box.pack(fill="both", expand=True)

        self.list_box.bind("<Double-Button-1>", self.show_detail)

        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill="x")

        ttk.Button(
            bottom_frame,
            text="标记完成 / 取消完成",
            command=self.toggle_complete
        ).pack(pady=5)

        ttk.Button(
            bottom_frame,
            text="删除选中提醒",
            command=self.delete_task
        ).pack(pady=5)

    def load_listbox(self):
        self.list_box.delete(0, tk.END)

        for task in self.manager.tasks:
            status = "✅ " if task["is_completed"] else "⬜ "
            display = f"{status}{task['title']} | {task['remind_time']}"
            self.list_box.insert(tk.END, display)

    def add_task(self):
        title = self.title_entry.get().strip()
        date = self.date_entry.get()
        hour = self.hour_spin.get().zfill(2)
        minute = self.minute_spin.get().zfill(2)

        if not title:
            messagebox.showerror("错误", "请输入任务标题")
            return

        remind_time = f"{date} {hour}:{minute}"

        try:
            datetime.strptime(remind_time, TIME_FORMAT)
        except ValueError:
            messagebox.showerror("错误", "时间格式错误")
            return

        self.manager.add_task(title, remind_time)
        self.title_entry.delete(0, tk.END)
        self.load_listbox()

    def toggle_complete(self):
        selected = self.list_box.curselection()
        if not selected:
            messagebox.showerror("提示", "请选择任务")
            return

        index = selected[0]
        self.manager.toggle_complete(index)
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
        detail = (
            f"任务: {task['title']}\n"
            f"提醒时间: {task['remind_time']}\n"
            f"状态: {'已完成' if task['is_completed'] else '未完成'}"
        )
        messagebox.showinfo("提醒详情", detail)
