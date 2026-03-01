import json
import os
from datetime import datetime
from config import FILE_NAME


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_tasks(self):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

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

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    def toggle_complete(self, index):
        self.tasks[index]["is_completed"] = not self.tasks[index]["is_completed"]
        self.save_tasks()

    def reset_daily_status(self):
        today = datetime.now().strftime("%Y-%m-%d")
        for task in self.tasks:
            if task.get("last_remind_date") != today:
                task["today_reminded"] = False
        self.save_tasks()
