
# 不推荐的多线程
import threading

def io_task():
    with open("t.txt","w") as f:
        f.write("hello")
        
threads = [threading.Thread(target=io_task) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
    
# 推荐
import asyncio

async def io_task():
    async with aiofiles.open("t.txt","w") as f:
        await f.write("hello")
        
asyncio.run(main())

# 推荐多进程(CPU密集型)
from multiprocessing import Pool

def cpu_task(x):
    return x*x

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(cpu_task,[1,2,3,4]))
        

        