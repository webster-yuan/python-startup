import re
# 栈的方式
def valid_str(string):
    if len(string) %2==1:
        return False
    stack=[]
    char_dict={
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in string:
        # 遍历的字符在字典中说明是右括号
        if char in char_dict:
            # 遇到右括号,如果发现此时栈为空,说明之前并没有遇到左括号,返回False
            # 右括号对的左括号是否是栈里面的左括号
            if not stack or char_dict[char] !=stack.pop():
                return False
        else:
            # 说明是左括号
            stack.append(char)
    return not stack # 栈为空说明括号匹配成功

print(valid_str('()'))
print(valid_str('()[]{}'))
print(valid_str('(}'))
        
# 正则表达式的方式
def valid_str_re(string):
    if len(string)%2 ==1:
        return False
    while '()' in string or '{}' in string or '{}' in string:
        string =re.sub(r'\(\)|\[\]|{}','',string)
    return string == ''
print(valid_str_re('()'))
print(valid_str_re('()[]{}'))
print(valid_str_re('(}'))