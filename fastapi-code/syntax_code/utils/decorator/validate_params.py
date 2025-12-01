from functools import wraps


def validate_params(func):
    @wraps(func)
    def wrapper(age, name):
        if not isinstance(age , int) or age < 0 :
            raise ValueError("Invalid age")
        if not name.isalpha():  # isalpha() 是字符串（str）对象的内置方法，用于检查字符串是否全部由字母组成且至少包含一个字符
            raise ValueError("Name must be alphabetic")
        return func(age, name)
    return wrapper


@validate_params
def create_user(age, name):
    print(f"User {name} (age : {age}) created")

if __name__ == '__main__':
    create_user(25, "Alice")  # 正常 User Alice (age : 25) created
    create_user(-5, "Bob123")  # 抛出 ValueError 没有打印，因为raise错写为了return