# 匹配电子邮件地址

import re

# 定义一个正则表达式模式，用于匹配电子邮件地址
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# 测试字符串
text = "Please contact us at support@example.com for further assistance."

# 使用正则表达式搜索电子邮件地址
match = re.search(email_pattern, text)
if match:
    print(f"Found email address: {match.group()}")
else:
    print("No email address found.")

# 电子邮件地址：support@example.com
# support：匹配 [a-zA-Z0-9._%+-]+，即一个或多个合法字符。
# @：匹配 @ 字符。
# example：匹配 [a-zA-Z0-9.-]+，即一个或多个字母、数字、点或破折号。
# .：匹配 \. 字符。
# com：匹配 [a-zA-Z]{2,}，即两个或多个字母。