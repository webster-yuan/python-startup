import threading


# 装饰器模式+线程安全

def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        nonlocal instances
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance # 装饰器要返回这个方法

@singleton
class AppManager:
    """
        线程安全的配置管理单例类
        功能：通过装饰器实现单例 + 类内部锁保证配置操作安全
    """

    def __init__(self):
        # 初始化方法仍会被调用多次（装饰器与 __new__ 的差异）
        # 因此需要保护初始化逻辑
        self._initialized = False
        self._init_lock = threading.Lock()
        self._config_lock = threading.Lock()
        self._safe_initialize()

    def _safe_initialize(self):
        """受保护的初始化方法"""
        if not self._initialized:
            with self._init_lock:
                if not self._initialized:
                    self._initialize()
                    self._initialized = True

    def _initialize(self):
        """实际初始化逻辑（仅执行一次）"""
        print("执行真正的配置初始化")
        self.config = {
            "debug_mode": False,
            "database_url": "postgresql://user:pass@localhost:5432/mydb",
            "max_connections": 20
        }

    def get_config(self, key):
        return self.config.get(key, None)

    def update_config(self, key, value):
        """线程安全的配置更新"""
        with self._config_lock:
            self.config[key] = value
            print(f"[安全更新] {key} = {value}")


def worker(thread_id, new_value):
    """工作线程：修改并读取配置"""
    config = AppManager()

    # 修改配置
    config.update_config("debug_mode", new_value)

    # 读取配置
    current_mode = config.get_config("debug_mode")
    print(f"线程 {thread_id} 读取到 debug_mode = {current_mode}")


def stress_test():
    """压力测试：启动10个线程竞争修改配置"""
    threads = []
    for i in range(10):
        t = threading.Thread(
            target=worker,
            args=(i, i % 2 == 0)  # 交替设置True/False
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    final_config = AppManager()
    print("\n最终配置状态:")
    print(f"debug_mode = {final_config.get_config('debug_mode')}")
    print(f"database_url = {final_config.get_config('database_url')}")


if __name__ == '__main__':
    print("=== 单例初始化测试 ===")
    s1 = AppManager()
    s2 = AppManager()
    print(f"单例有效性验证: {s1 is s2}")

    print("\n=== 多线程压力测试 ===")
    stress_test()

# 装饰器在第一次生效后，针对装饰的类：MySingleton 不再指向原始类，而是指向get_instance函数。
# 装饰器的返回值类型：
#
# 装饰器可以返回任意类型，但需根据被装饰目标的类型决定。
#
# 当装饰类时，装饰器可以返回一个类或函数。
#
# 在此案例中，@Singleton装饰器返回的是get_instance函数，替换了原本的类构造函数。
#
# 为什么能返回函数：
#
# 装饰器生效后，MySingleton不再指向原始类，而是指向get_instance函数。
#
# 当调用MySingleton()时，实际调用的是get_instance()，该函数控制实例的创建逻辑。
#
# 通过闭包变量instances字典保存每个类的唯一实例，实现单例模式。
#
# 关键机制：
#
# Python中类本身是对象，可以被替换为其他可调用对象（如函数）。
#
# get_instance函数通过检查instances字典确保每个类只有一个实例
