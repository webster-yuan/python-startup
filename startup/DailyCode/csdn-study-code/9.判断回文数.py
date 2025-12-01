# 随意找一个十进制的数，把它倒过来成另一个数，再把这两个数相加，得一个和数，这是第一步;
# 然后把这个和数倒过来，与原来的和数相加，又得到一个新的和数，这是第二步。
# 照此方法，一步步接续往下算，直到出现一个“回文数”为n。
# 例如:28+82=110,110+011=121，两步就得出了一个“回文数”。
# 如果接着算下去，还会得到更多的“回文数”。这个过程称为“196算法”。

# 方式一: 通过逆序字符串的方式判断(Python使用的是切片)

def is_palindrome1(n):
    s =str(n)
    return s == s[::-1]  # 切片操作，[::-1]表示逆序

# 方式二: 反转一半的数字
# 将整数后半部分reverted,每次循环x%10拿到末尾数字
# 然后x/10去除末尾的数字,循环结束条件是x <= reverted

def is_palindrome2(x):
    # 不写这个,会导致110这种情况出现漏判
    if x<0 or x >0 and x%10==0:
        return False
    
    reverted =0
    while x> reverted:
        reverted = reverted * 10 + x%10
        x //=10 # 整除10才能去掉末尾数字
    return x == reverted or x ==reverted//10

print(is_palindrome1(121))
print(is_palindrome1(110))
print(is_palindrome2(1221))
print(is_palindrome2(1130))
print(is_palindrome2(110))

