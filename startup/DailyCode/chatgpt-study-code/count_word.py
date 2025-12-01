# 统计单词在字符串中的出现次数，并输出词频最高的单词和出现次数
import re


def counts_word(text):
    words = re.split('[ ,.]', text.lower())  # 先将字符串转换为小写，然后使用正则表达式将字符串分割为单词列表
    word_count = {}  # 定义一个字典用于存储单词及其出现次数
    for word in words:  # 遍历单词列表
        if word in word_count:  # 如果单词已存在于字典中，则增加出现次数
            word_count[word] += 1
        else:  # 如果单词不存在于字典中，则添加到字典中并设置出现次数为1
            word_count[word] = 1
    return word_count


def most_frequent_word(word_count):
    max_word = max(word_count, key=word_count.get)  # word_count.get(key)返回字典中key对应的value值
    max_count = word_count[max_word]
    return max_word, max_count  # 返回词频最高的单词和出现次数


text = "Hello world,hello Python. Python is great; great Python!"
word_counts = counts_word(text)
max_word, max_count = most_frequent_word(word_counts)
print(f"The most frequent word is {max_word} and its count is {max_count}.")
