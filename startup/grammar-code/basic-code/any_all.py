class User:
    def __init__(self, name, age, is_admin=False):
        self.name = name
        self.age = age
        self.is_admin = is_admin


def any_all_main():
    users = [User('tom', 23, True), User('john', 34, False), User('john', 35, False)]
    has_admin = any(u.is_admin for u in users)  # 是否任一满足
    all_adult = all(u.age > 18 for u in users)  # 是否所有都满足
    print('has admin:', has_admin)  # True
    print('all adult:', all_adult)  # True


any_all_main()
