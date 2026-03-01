from tkinter import messagebox

import winsound
from datetime import datetime, timedelta

from tools.reminder_app.config import TIME_FORMAT, CHECK_INTERVAL


class ReminderService:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager

    def start(self):
        self.check_tasks()

    def check_tasks(self):
        now = datetime.now()
        today_str = now.strftime("%Y-%m-%d")

        for task in self.task_manager.tasks:
            if task["is_completed"]:
                continue

            deadline = datetime.strptime(task["deadline"], TIME_FORMAT)
            remind_time = deadline - timedelta(minutes=task["remind_before_minutes"])

            # 快到提醒日期了
            if remind_time <= now <= deadline:
                # 今天还没提醒过
                if task["last_remind_date"] != today_str:
                    winsound.Beep(1000, 1000)
                    messagebox.showinfo("提醒", f"{task['title']}即将开始！")
                    task["last_remind_date"] = today_str
                    self.task_manager.save_tasks()

            if deadline.date() == now.date():
                if task["last_remind_date"] != today_str:
                    winsound.Beep(800, 800)
                    messagebox.showinfo("今日任务", f"今天有任务：{task['title']}")
                    task["last_remind_date"] = today_str
                    self.task_manager.save_tasks()

        self.root.after(CHECK_INTERVAL, self.check_tasks)
