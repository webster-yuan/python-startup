from multiprocessing import Process
import time
import os

def sing():
    print(f"cur process is {{os.getpid()}}, parent process is {os.getppid()}")

    print(f"sing start ")
    time.sleep(2)
    print("sing end")

def dance():
    print(f"cur process is {{os.getpid()}}, parent process is {os.getppid()}")

    print("dance start")
    time.sleep(2)
    print("dance end")

def eat(name:str):
    print(f"{name} is eating")


def test1():
    process1 = Process(target=sing, name="process 1")
    process2 = Process(target=dance, name="process 2")

    print(f"main process is {os.getpid()}")

    process1.start()
    process2.start()

    print(f"{process1.name}")
    print(f"{process2.name}")

    print(f"{process1.pid}")
    print(f"{process2.pid}")


def test2():
    """
    主进程等待子进程退出
    """
    process1 = Process(target=eat, args=("webster", ))
    process1.start()
    process1.join() # 主进程等待

    print(f"{process1.is_alive()}")

global_list = []

def write():
    global global_list
    for i in range(5):
        global_list.append(i)
        time.sleep(1)

    print(f"写入的列表为：{global_list}")


def read():
    global global_list
    print(f"读取得到的列表为：{global_list}")
    

def test3():
    """
    进程之间不共享全局变量
    """
    p1 = Process(target=write, name="write process")
    p2 = Process(target=read, name="read process")
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # 读取得到的列表为：[]
    # 写入的列表为：[0, 1, 2, 3, 4]

from multiprocessing import Queue
def test_queue():
    """
    1. 队列
    """
    queue1 = Queue(maxsize=3) # 最多接收3条消息，为负值代表没有上限
    queue1.put("a")
    queue1.put("b")
    queue1.put("c")
    print(f"队列满了吗？{queue1.full() == True}")
    # 队列满了吗？True

    queue1.get("a")
    queue1.get("b")
    queue1.get("c")
    
    if queue1.empty():
        print(f"已空")
    else:
        print(queue1.qsize())

    # 已空

def write_data(q: Queue):
    """向队列中写入数据"""
    # 循环写入5个数字
    for i in range(5):
        q.put(i)
        print(f"成功写入元素：{i}")
    
    # 移除未定义的global_list打印，改为提示写入完成
    print("数据写入完成！")

def read_data(q: Queue):
    """从队列中读取数据"""
    # 循环读取队列中的数据，直到队列为空
    while True:
        try:
            # 使用get_nowait()非阻塞读取，避免队列空时阻塞
            elem = q.get_nowait()
            print(f"读取到的元素：{elem}")
        except:
            # 队列为空时捕获异常并退出循环
            print("数据读取完成！")
            break
    
def test4():
    """
    进程间通信
    """
    queue2 = Queue()
    
    # 创建写入和读取进程
    process1 = Process(target=write_data,args=(queue2, ))
    process2 = Process(target=read_data,args=(queue2, ))
    
    # 启动进程（无需先join写入进程，让两个进程并发执行）
    process1.start()
    process2.start()
    
    # 等待所有进程执行完毕
    process1.join()
    process2.join()


# 1. 防止被import时执行main里面的方法
# 2. 防止win系统递归创建子进程
if __name__ == "__main__":
    test4()
