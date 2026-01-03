# 每个进程有独立 Python 解释器 → 绕过 GIL，真正多核并行

import time
from concurrent.futures import ProcessPoolExecutor
import math


def is_prime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False

    return True


if __name__ == '__main__':
    nums = range(2_000_000, 2_000_300)
    with ProcessPoolExecutor() as executor:
        start = time.time()
        ok = sum(executor.map(is_prime, nums))

    print("prime count=", ok, "cost", time.time() - start)
    # prime count= 21 cost 0.6815598011016846
