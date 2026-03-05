def task1():
    yield 'a'

def task2():
    yield 'b'

def test1():
    t1 = task1()
    t2 = task2()

    while True:
        try:
            print(next(t1))
            print(next(t2))
        except Exception:
            break
    # a
    # b

# 协程
# 试用场景：
# 1. 适合线程中IO较多
# 2. 适合做并发处理

# Python 中有对其进行封装 
# greenlet: 属于手动切换，程序受到阻塞之后会阻塞，而不能自动切换
import time
def sing():
    print("sing start")
    print("sing end")

def dance():
    print("dance start")
    print("dance end")

from greenlet import greenlet
def test2():
    """
    greenlet: 需要手动切换
    """
    # 1. 创建协程对象
    green1 = greenlet(sing)
    green2 = greenlet(dance)

    green1.switch() # 手动切换到协程中使用
    green2.switch()

    # sing start
    # sing end
    # dance start
    # dance end

import gevent
# gevent.sleep(2) 本质上是让当前的协程暂停执行 2 秒，
# 但它和 Python 标准库的 time.sleep(2) 有本质区别：
# time.sleep(2)：会让整个线程阻塞 2 秒，
# 期间 CPU 完全不处理这个线程的任何任务，线程内的所有代码都无法执行。
# gevent.sleep(2)：只是让当前协程 “让出” CPU 执行权，线程本身不会阻塞。在这 2 秒内，gevent 会调度该线程内的其他就绪协程执行，直到 2 秒超时后，
# 当前协程才会重新进入就绪状态，等待被调度执行。
def singing():
    print("sing start")
    gevent.sleep(2)
    print("sing end")

def danceing():
    print("dance start")
    gevent.sleep(3)
    print("dance end")

def test3():
    """
    gevent: 遇到IO操作时自动切换
    """
    # 1. 创建协程对象
    g1 = gevent.spawn(singing)
    g2 = gevent.spawn(danceing)
    # 2. 阻塞等待协程执行结束
    g1.join()
    g2.join()

    # sing start
    # dance start
    # sing end
    # dance end

def eat(name:str):
    for i in range(3):
        gevent.sleep(1)
        print(f"{name} is eating {i}th time")

def test4():
    """
    joinall: 等待所有协程都执行结束，再退出
    """
    gevent.joinall([
        gevent.spawn(eat, "webster"),
        gevent.spawn(eat, "yuanwei")
    ])
    # webster is eating 0th time
    # yuanwei is eating 0th time
    # webster is eating 1th time
    # yuanwei is eating 1th time
    # webster is eating 2th time
    # yuanwei is eating 2th time

from gevent import monkey
monkey.patch_all()
# 将用到的time.sleep()代码，替换为gevent里面自己实现的耗时操作的gevent.sleep()代码
# monkey 一定放在被打补丁的前面

def eating(name:str):
    for i in range(3):
        time.sleep(1)
        print(f"{name} is eating {i}th time")

def test5():
    """
    monkey: 拥有在模块运行时替换的功能
    """
    gevent.joinall([
        gevent.spawn(eating, "webster"),
        gevent.spawn(eating, "yuanwei")
    ])


if __name__ == "__main__":
    test5()

