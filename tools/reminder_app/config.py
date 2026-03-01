import os
import sys

TIME_FORMAT = "%Y-%m-%d %H:%M"
CHECK_INTERVAL = 60000  # 每分钟检查一次


def resource_path(relative_path):
    """兼容 PyInstaller 打包路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


ALERT_SOUND = resource_path("alert.mp3")
