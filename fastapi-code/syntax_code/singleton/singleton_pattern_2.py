import threading


class AppConfigSingleton:
    """
        应用配置管理器
        加载配置文件，提供线程安全的配置访问
    """
    # 所有实例共享这些变量
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):  # cls：当前类本身（不是实例）
        # 构造函数：负责创建类的实例（早于 __init__ 执行）
        if not cls._instance: # 避免不必要的加锁
            with cls._lock:
                if not cls._instance: # 确保线程安全
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    # def __init__(self):
    #     # 初始化代码 （初始化实例属性）
    #     # 单例模式的陷阱：如果使用 __init__，每次获取实例时都会重新初始化
    #     # 自定义控制：通过 _initialize 确保初始化只执行一次
    #     # 其实每次创建实例都会在__new__之后调用__init__
    #     # 但是我们手动控制把初始化逻辑封装为一个函数，按需调用
    #     print("__init__")

    def _initialize(self):
        """从文件/环境加载配置"""
        self.config = {
            "debug_mode": False,
            "database_url": "postgresql://user:pass@localhost:5432/mydb",
            "max_connections": 20
        }
        if self.config:
            print("配置加载完成")
        else:
            print("加载失败")

    def get_config(self, key):
        # Python 字典的读操作是线程安全的
        return self.config.get(key, "没拿到")

    def update_config(self, key, value):
        """线程安全的配置更新"""
        with self._lock:
            self.config[key] = value


count = 0

def worker(flag, thread_id):
    config = AppConfigSingleton()
    global count
    count += 1
    print(f"flag:{flag}")
    print(f"thread_id:{thread_id}")
    config.update_config("debug_mode", flag)
    print(f"thread_{thread_id}"
          f"Worker get addr: {config.get_config('database_url')}"
          f"Worker get mode: {config.get_config('debug_mode')}")




def multiple_thread_test():
    main_config = AppConfigSingleton()
    flag = True
    global count
    main_config.update_config("debug_mode",flag)
    threads =[]
    for i in range(5):
        if flag:
            flag = False
        else:
            flag = True

        t = threading.Thread(target=worker, args=[flag,i])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(f"当前调试模式状态: {main_config.get_config('debug_mode')}")


if __name__ == '__main__':
    # SingletonTest1()
    multiple_thread_test()
    print(f"count:{count}")