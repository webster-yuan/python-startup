import json
import os
from datetime import datetime

# =========================
# 1️⃣ 定义软件数据存储目录
# =========================

APP_DIR = os.path.join(os.getenv("LOCALAPPDATA"), "ReminderApp")
FILE_NAME = os.path.join(APP_DIR, "tasks.json")


class TaskManager:
    def __init__(self):
        # 第一次运行自动创建目录
        os.makedirs(APP_DIR, exist_ok=True)
        self.tasks = self.load_tasks()

    # =========================
    # 加载任务
    # =========================
    def load_tasks(self):
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    # =========================
    # 保存任务
    # =========================
    def save_tasks(self):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    # =========================
    # 添加任务
    # =========================
    def add_task(self, title, remind_time):
        task = {
            "title": title,
            "remind_time": remind_time,
            "is_completed": False,
            "last_remind_date": "",
            "today_reminded": False
        }
        self.tasks.append(task)
        self.save_tasks()

    # =========================
    # 删除任务
    # =========================
    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    # =========================
    # 切换完成状态
    # =========================
    def toggle_complete(self, index):
        self.tasks[index]["is_completed"] = not self.tasks[index]["is_completed"]
        self.save_tasks()

    # =========================
    # 每日状态重置
    # =========================
    def reset_daily_status(self):
        today = datetime.now().strftime("%Y-%m-%d")
        for task in self.tasks:
            if task.get("last_remind_date") != today:
                task["today_reminded"] = False
        self.save_tasks()
