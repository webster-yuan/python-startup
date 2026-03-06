from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]  # 以第一个字符串为初始前缀
    for s in strs[1:]:
        # 不断缩短前缀，直到它是当前字符串的前缀
        while s.find(prefix) != 0:
            # prefix[:-1] 省略了起始索引（默认从 0 开始），结束索引是 -1（代表倒数第一个元素的位置）；
            # 切片规则是「左闭右开」：包含起始索引的元素，不包含结束索引的元素；
            # 因此 [:-1] 就是「从第一个元素取到倒数第一个元素的前一位」，也就是去掉最后一个元素。
            
            prefix = prefix[:-1] # 去掉前缀的最后一个字符
            if not prefix:  # 如果前缀已经空了，说明没有公共前缀
                return ""
            
    return prefix

# 测试
print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(longestCommonPrefix(["dog","racecar","car"]))    # ""