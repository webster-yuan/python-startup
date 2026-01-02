# 迭代器协议&生成器

## 迭代器协议：
# 有没有 __iter__() → 返回「迭代器对象自身」
# 有没有 __next__() → 返回下一个值，没货时抛 StopIteration

class CountDownV1:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration

        print("cur value is", self.n)
        self.n -= 1
        return self.n + 1


for i in CountDownV1(10):
    print(i)


## 生成器函数
# 生成器函数在被调用时，并不会执行函数体代码从而立即返回结果，只是返回一个生成器对象
# 不调用不执行，调用一次执行一次
# 第一次调用时，执行到yield为止，返回n值，记录当前状态
# 下一次调用时，从之前暂停的为止继续执行 n-=1
# 这种 “调用next()才执行、遇到yield就暂停、下次调用继续恢复” 的机制，
# 就是生成器只能通过next() 或者 其他方式（本质底层都是调用next()）
def CountDownV2(n):
    while n > 0:
        yield n  # 包含yield的函数是生成器函数，不是普通函数
        n -= 1


g = CountDownV2(3)
print(next(g), next(g), next(g))  # 3 2 1

## yield from 委托子生成器， 把活都传给另一个生成器，顺便把值/异常/返回都传回来
print("yield from 生成器委托功能")


def subGen():
    yield 1
    yield 2
    return 'done'


def main():
    print("start")
    # 1. yield from 透传产出值，委托 subGen()产出值:
    # 将subGen()产出的所有值（yield后面的值）直接透传给外层的迭代器（这里就是list()），无需main()手动干预，将产出值暂存进入list中
    # 2. yield from 捕获返回值，捕获subGen()的返回值并赋值给v：
    # 执行到return 'done' 时， Python 不会直接抛出StopIteration异常终止， 将 'done' 赋值给到StopIteration的value属性中
    # yield from会自动捕获这个StopIteration异常，并提取其中的value（即 'done'），赋值给委托生成器中的变量v；
    v = yield from subGen()
    print('subGen returned:', v)  # subGen returned: done


# list(g)会遍历这个生成器对象（底层不断调用next()）
print(list(main()))  # [1, 2]

print("send() 双向通信")


def running_avg():
    total = cnt = 0
    while True:
        val = yield total / cnt if cnt else None
        total += val
        cnt += 1


# 拿到迭代器对象，并没有执行，函数处于休眠状态，total cnt 都没初始化
avg = running_avg()
# 调用一次next，执行到 val 赋值卡住等待下一次next调用，执行后续逻辑（赋值给到val），生成器将None作为next(avg)的返回值
next(avg)
# 向暂停在yield处的生成器传入一个值，同时触发生成器恢复执行，直到下一个yield暂停并返回产出值
print(avg.send(1))  # send 将1传给running_avg 赋值val = 1 ，后续total=1 cnt=1 yield返回1/1=1.0，在下一次val赋值卡主
print(avg.send(2))  # send 将2传给running_avg 赋值val = 2 ，后续total=1+2=3，cnt=1+1=2 yield返回3/2=1.5，在下一次val赋值卡主
