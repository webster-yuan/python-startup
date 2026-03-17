# 找到第一个出现一次的元素的索引
# 给定一个字符串 s，找到第一个只出现一次的字符，并返回它的索引。如果没有，则返回 -1。

def firstUniqChar(s: str) -> int:
    if not s:
        return -1
    
    char_count = {}
    dumplicates = set()

    for char in s:
        if char in char_count:
            dumplicates.add(char)
        else:
            char_count[char] = 1
    
    for char in s:
        if char not in dumplicates:
            return s.index(char)
    
    return -1
