# 单线程协程（async / await）
# 特点：事件循环驱动，>10k 连接也只吃几十 MB 内存；
# 适用：高并发 I/O 密集（Web API、爬虫、网关、消息转发）；
# 前提：必须全程用异步库（aiohttp、aiomysql、aioredis …），混一个同步库就会阻塞整个循环。
# 骨架 = 5 个函数 / 对象即可跑通任意异步 I/O 任务：
# 1. `asyncio.run(coro)` # 启动事件循环
# 2. `asyncio.create_task(coro)`# 把协程包成 Task，可并发调度
# 3. `asyncio.gather(*tasks)`# 批量并发并收集结果
# 4. `asyncio.Semaphore(n)`# 控制并发量级
# 5. `async with session:`# 异步连接池（aiohttp / aiomysql / redis）

import asyncio
import logging
import time
from dataclasses import dataclass
from typing import List

import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry

logger = logging.getLogger(__name__)

MAX_RETRY_COUNT = 10
TIMEOUT_SECONDS = 10
CONCURRENT_LIMIT = 5  # 最大并发数（等同 MAX_WORKERS）


@dataclass(slots=True)
class FetchResult:
    url: str
    size: int | None = None
    cost: float | None = None
    error: str | None = None


async def _fetch_single(session: RetryClient, url: str) -> FetchResult:
    """单任务：异步重试 + 异常兜底"""
    start_time = time.time()
    try:
        async with session.get(url) as resp:
            resp.raise_for_status()
            data = await resp.read()
            return FetchResult(
                url=url,
                size=len(data),
                cost=time.time() - start_time,
            )
    except Exception as e:  # 网络/超时/HTTPError 都会被 aiohttp-retry 重试
        return FetchResult(
            url=url,
            error=str(e),
            cost=time.time() - start_time,
        )


async def batch_fetch(req_urls: List[str]) -> List[FetchResult]:
    """异步并发抓取，顺序返回（与 urls 一致）"""
    req_urls = [u.strip() for u in req_urls]
    start = time.perf_counter()

    # 1. 创建带重试策略的异步 session
    retry_options = ExponentialRetry(attempts=MAX_RETRY_COUNT, start_timeout=0.2)
    async with RetryClient(
            raise_for_status=True,
            timeout=aiohttp.ClientTimeout(total=TIMEOUT_SECONDS),
            retry_options=retry_options,
    ) as session:
        # 2. 用信号量限并发（等同 ThreadPoolExecutor 的 max_workers）
        sem = asyncio.Semaphore(CONCURRENT_LIMIT)

        async def limited_fetch(url: str) -> FetchResult:
            async with sem:
                return await _fetch_single(session, url)

        # 3. 顺序创建任务 → gather 保证顺序返回
        tasks = [limited_fetch(u) for u in req_urls]
        responses = await asyncio.gather(*tasks)

    logger.info("Async batch fetch done %d urls cost %.2fs", len(urls), time.perf_counter() - start)
    return responses


# 4. 入口
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    urls = ["https://httpbin.org/delay/1"] * 5
    results = asyncio.run(batch_fetch(urls))
    for res in results:
        if res.error:
            logger.error(f"❌ {res}")
        else:
            logger.info(f"✅ {res}")
