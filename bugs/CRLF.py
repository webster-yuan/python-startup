# 漏洞示例
def log_user_action(user_input):
    with open("user_actions.log", "a") as log_file:
        log_file.write(f"User action: {user_input}\n")

# 防御措施
def safe_log_user_action(user_input):
    # 替换CRLF字符，防止日志注入
    safe_input = user_input.replace("\r", "\\r").replace("\n", "\\n")
    with open("user_actions.log", "a") as log_file:
        log_file.write(f"User action: {safe_input}\n")

# 模拟用户输入
user_input = "Viewed page /index.html\r\nUser action: Deleted file /etc/passwd"

# 执行漏洞示例
log_user_action(user_input)

# 执行防御措施
safe_log_user_action(user_input)
