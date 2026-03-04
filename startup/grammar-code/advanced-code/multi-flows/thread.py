import time
import threading

def sing():
    print("sing start")
    time.sleep(2)
    print("sing end")

def dance():
    print("dance start")
    time.sleep(2)
    print("dance end")


def test_code1():
    print("hello world")
    # 1. 创建线程对象，指定每个对象做的任务
    thread1 = threading.Thread(target=sing)
    thread2 = threading.Thread(target=dance)

    # 3. 设置守护线程，
    # 设置为守护线程后，主线程退出时会直接终止所有守护线程，不需要等待它们执行完成；
    # 如果不设置，主线程会等待所有非守护线程执行完毕后才退出。

    thread1.daemon = True
    thread2.daemon = True

    # 2. 开启线程
    thread1.start()
    thread2.start()

    # 4. 阻塞主线程join(),暂停主线程，等到子线程都完成之后，主线程继续执行，必须放在start后面
    thread1.join()
    thread2.join()

    # 5. 获取线程名字
    print(thread1.name) # Thread-1 (sing)
    print(thread2.name) # Thread-2 (dance)
    print("完美谢幕")
    # hello world
    # sing start
    # dance start
    # dance end
    # sing end
    # Thread-1 (sing)
    # Thread-2 (dance)
    # 完美谢幕

def shouting(name:str):
    print(f"{name} is shouting start")
    time.sleep(2)
    print(f"{name} is shouting end")

def test_code2():
    """
    执行任务的函数携带参数
    """
    thread3 = threading.Thread(target=shouting, args=("webster", )) # 以元组的形式传参，不要忘记,
    thread3.daemon = True
    thread3.start()
    thread3.join()
    # webster is shouting start
    # webster is shouting end

def task_with_thread_name():
    time.sleep(1)
    print(f"当前线程是 {threading.current_thread().name} 在跑！")

def test_code3():
    """
    验证线程执行是无序的，资源存在竞争
    """
    for i in range(5):
        # 每循环一次，启动一个线程
        t= threading.Thread(target=task_with_thread_name)
        t.start()

    # 当前线程是 Thread-5 (task_with_thread_name) 在跑！
    # 当前线程是 Thread-1 (task_with_thread_name) 在跑！
    # 当前线程是 Thread-4 (task_with_thread_name) 在跑！
    # 当前线程是 Thread-3 (task_with_thread_name) 在跑！
    # 当前线程是 Thread-2 (task_with_thread_name) 在跑！

custom_sum =0
add_count = 10000000

def add1():
    for i in range(add_count):
        global custom_sum
        custom_sum +=1
    print(f"第一次累加：{custom_sum}")


def add2():
    for i in range(add_count):
        global custom_sum
        custom_sum +=1

    print(f"第二次累加：{custom_sum}")

def test_code4():
    """
    验证线程之间共享资源
    """
    thread4 = threading.Thread(target=add1)
    thread5 = threading.Thread(target=add2)

    thread4.start()
    thread5.start()

    thread4.join()
    thread5.join()

    # 第一次累加：19708641
    # 第二次累加：20000000

from threading import Lock
# 创建全局互斥锁
lock =Lock()

custom_sum1 =0
add_count1 = 1000000000

def add3():
    try:
        lock.acquire()
        global custom_sum1

        for i in range(add_count1):
            custom_sum1 +=1

        print(f"第一次累加：{custom_sum1}")
    finally:
        lock.release()


def add4():
    try:
        lock.acquire()
        global custom_sum1

        for i in range(add_count1):
            custom_sum1 +=1

        print(f"第二次累加：{custom_sum1}")
    finally:
        lock.release()


def test_code5():
    """
    线程同步：解决竞争-> 互斥锁：保证同一时刻，只有一个线程执行
    """
    thread4 = threading.Thread(target=add3)
    thread5 = threading.Thread(target=add4)

    thread4.start()
    thread5.start()

    thread4.join()
    thread5.join()

    # 第一次累加：10000000
    # 第二次累加：20000000

if __name__=="__main__":
    test_code5()
