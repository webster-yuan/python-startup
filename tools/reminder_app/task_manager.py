import json
import os.path
from config import FILE_NAME, REMIND_BEFORE_MINUTES


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

    def add_task(self, title, deadline_str):
        task = {
            "title": title,
            "deadline": deadline_str,
            "remind_before_minutes": REMIND_BEFORE_MINUTES,
            "is_completed": False,
            "last_remind_date": ""
        }
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()
