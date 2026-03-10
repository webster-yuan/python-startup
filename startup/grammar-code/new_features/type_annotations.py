# 3.10+，用int|str 替代 Union[int, str]，更简洁
def print_value(value:int | str)->None:
    print(f"Value: {value}")

print(123)
print("Hello")
# 123
# Hello