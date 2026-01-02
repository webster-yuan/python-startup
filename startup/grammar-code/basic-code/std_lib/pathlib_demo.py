# 面向对象的文件路径
from pathlib import Path

root = Path('/tmp/')
log = root / 'log.txt'
log.parent.mkdir(parents=True, exist_ok=True)
log.write_text("hello\n")
