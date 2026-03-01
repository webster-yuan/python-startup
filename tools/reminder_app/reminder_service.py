from datetime import datetime, timedelta
from tkinter import messagebox
from playsound import playsound
from config import TIME_FORMAT, CHECK_INTERVAL, ALERT_SOUND


class ReminderService:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager

    def start(self):
        self.task_manager.reset_daily_status()
        self.daily_summary_check()
        self.check_tasks()

    def play_sound(self):
        """统一播放提示音"""
        try:
            playsound(ALERT_SOUND)
        except:
            pass

    # --------------------------
    # ✅ 每日总览提醒（加提示音）
    # --------------------------
    def daily_summary_check(self):
        today = datetime.now().strftime("%Y-%m-%d")
        pending_tasks = []

        for task in self.task_manager.tasks:
            if task["is_completed"]:
                continue

            if not task.get("today_reminded", False):
                pending_tasks.append(task["title"])
                task["today_reminded"] = True

        if pending_tasks:
            self.play_sound()  # 🔊 加提示音
            message = "今天的任务：\n\n" + "\n".join(pending_tasks)
            messagebox.showinfo("今日任务总览", message)
            self.task_manager.save_tasks()

    # --------------------------
    # ✅ 提前1小时提醒
    # --------------------------
    def check_tasks(self):
        now = datetime.now()
        today_str = now.strftime("%Y-%m-%d")

        for task in self.task_manager.tasks:
            if task["is_completed"]:
                continue

            remind_time = datetime.strptime(task["remind_time"], TIME_FORMAT)

            # ⏰ 关键修改：提前1小时
            remind_time = remind_time - timedelta(hours=1)

            if remind_time <= now:
                if task["last_remind_date"] != today_str:
                    self.play_sound()  # 🔊 统一声音

                    messagebox.showinfo(
                        "提醒",
                        f"{task['title']}\n将在1小时后开始"
                    )

                    task["last_remind_date"] = today_str
                    task["today_reminded"] = True
                    self.task_manager.save_tasks()

        self.root.after(CHECK_INTERVAL, self.check_tasks)
