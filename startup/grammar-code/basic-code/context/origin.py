import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()  # 返回系统的高精度计时器当前值（以秒为单位）
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cost = time.perf_counter() - self.start
        print(f'[timer] cost:{self.cost:.3f}s')
        # 异常为None，说明正常结束
        if exc_type is not None:
            print(f"[timer] exception captured, do rollback/clean there")

        return False


if __name__ == '__main__':
    with Timer() as t:
        time.sleep(3)

    print('t.cost:', t.cost)

# [timer] cost:3.011s
# t.cost: 3.0114789999788627
