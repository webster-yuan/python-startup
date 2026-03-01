import tkinter as tk
from task_manager import TaskManager
from ui import TaskApp

if __name__ == "__main__":
    root = tk.Tk()
    manager = TaskManager()
    app = TaskApp(root, manager)
    root.mainloop()
