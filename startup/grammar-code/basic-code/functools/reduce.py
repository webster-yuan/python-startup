# 把「二元函数」累积成「一元结果」
import operator
from functools import reduce

if __name__ == '__main__':
    # 反复调用二元函数operator.add，对range(1,5)的元素进行累积处理，最终收敛为一个单一结果
    # 注意范围是左闭右开的
    print(reduce(operator.add, range(1, 5)))  # 10

    print(reduce(lambda a, b: a if a > b else b, [3, 1, 4, 2]))  # 4
