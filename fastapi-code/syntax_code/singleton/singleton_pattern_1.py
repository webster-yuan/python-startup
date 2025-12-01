
def Singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@Singleton
class MySingleton:
    def __init__(self):
        print("Initializing MySingleton")


def SingletonTest1():
    a = MySingleton()
    b = MySingleton()
    print(a is b)

if __name__ == '__main__':
    SingletonTest1()