#1. 已知一个字符串为 “hello_world_yoyo”，如何得到一个队列 [“hello”,”world”,”yoyo”] ？
test1='hello_world_yoyo'
print(test1.split('_'))

# 2. 有个列表 [“hello”, “world”, “yoyo”]，如何把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”？
test2=['hello', 'world', 'yoyo']
print("_".join(test2))
# 如果不依赖 python 提供的 join 方法，还可以通过 for 循环，然后将字符串拼接，但是在用“+”连接字符串时，结果会生成新的对象，
# 使用 join 时结果只是将原列表中的元素拼接起来，所以 join 效率比较高。
myTuple = ("Bill", "Steve", "Elon")
x = "#".join(myTuple)
print(x)

j=''
for i in test2:
    j=j+"_"+i
print(j.lstrip('_'))#将左边的_清掉

# 3. 把字符串 s 中的每个空格替换成”%20”，
# 输入：s = “We are happy.”，输
# 出：“We%20are%20happy.”。
s ='We are happy.'
print(s.replace(' ','%20'))

# 4. Python 如何打印 99 乘法表？
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print("%d*%d=%-2d"%(i,j,i*j),end=' ')
#         j+=1
#     print()
#     i+=1

# 5. 从下标 0 开始索引，找出单词 “welcome”
# 在字符串“Hello, welcome to my world.” 中出现的位置，
# 找不到返回 -1。
def test1():
    message='Hello, welcome to my world.'
    world='welcome'
    if world in message:
        return message.find(world)
    else:
        return -1

print(test1())

# 6. 统计字符串“Hello, welcome to my world.” 中字母 w 出现的次数。
def test2():
    str='Hello, welcome to my world.'
    num=0
    for i in str:
        if 'w' in i:
            num+=1
    return num
print(test2())
# 7. 输入一个字符串 str，输出第 m 个只出现过 n 次的字符，
# 如在字符串 gbgkkdehh 中，
# 找出第 2 个只出现 1 次的字符，输出结果：d
def test3(str_test,num,counts):
    '''
    :param str_test: 字符串
    :param num: 出现次数
    :param counts: 第几个出现num次的字符
    :return:
    '''
    list=[]
    for i in str_test:
        #使用count函数,统计出所有字符出现的次数
        count = str_test.count(i,0,len(str_test))

        if count==num:
            list.append(i)
    return str_test[counts-1]

print(test3('gbgkkdehh',1,2))

# 8. 判断字符串 a = “welcome to my world”
# 是否包含单词 b = “world”，
# 包含返回 True，不包含返回 False。

def test4():
    message1='welcome to my world'
    word='world'
    if word in message1:
        return True

    return False
print(test4())
# 9. 从 0 开始计数，输出指定字符串 A = “hello”
# 在字符串 B = “hi how are you hello world, hello yoyo!”
# 中第一次出现的位置，如果 B 中不包含 A，则输出 -1。
def test6():
    message2='hi how are you hello world, hello yoyo!'
    word='hello'
    return message2.find(word)
print(test6())

# 10. 从 0 开始计数，输出指定字符串 A = “hello”在字符串
# B = “hi how are you hello world, hello yoyo!”中最后出现的位置，
# 如果 B 中不包含 A，则输出 -1。
def test5(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)# 目的str,begin的位置
        if position==-1:
            return last_position
        last_position=position
print(test5('hi how are you hello world, hello yoyo!','hello'))