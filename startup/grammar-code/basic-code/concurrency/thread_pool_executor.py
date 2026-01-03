# 多线程IO并发 [threading / ThreadPoolExecutor]

import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List
from dataclasses import dataclass

import requests

logger = logging.getLogger(__name__)

MAX_RETRY_COUNT = 10
TIMEOUT_SECONDS = 10
MAX_WORKERS = 5


@dataclass(slots=True)
class FetchResult:
    url: str
    size: int | None = None
    cost: float | None = None
    error: str | None = None


def _fetch_single(req_url: str) -> FetchResult:
    """单任务：可重试 + 异常兜底"""
    start_time = time.time()
    tries = 0
    while tries < MAX_RETRY_COUNT:
        try:
            response = requests.get(req_url, timeout=TIMEOUT_SECONDS)
            response.raise_for_status()
            return FetchResult(
                url=req_url,
                size=len(response.content),
                cost=time.time() - start_time,
            )
        except Exception as e:
            tries += 1
            logger.warning("Fetch failed (try %d/%d) %s: %s", tries, MAX_RETRY_COUNT, req_url, e)
            if tries >= MAX_RETRY_COUNT:
                return FetchResult(
                    url=req_url,
                    error=str(e),
                    cost=time.time() - start_time,
                )
            time.sleep(0.2)

    return FetchResult(url=req_url, error="Max retry reached", cost=time.time() - start_time)


def batch_fetch(req_urls: List[str], *, max_workers: int = MAX_WORKERS) -> List[FetchResult]:
    """线程池批量抓取，返回有序结果（与 urls 顺序一致）"""
    start_time = time.perf_counter()
    req_urls = [u.strip() for u in req_urls]
    # 预留空位：预生成空壳对象占位，后面只替换内容，不改动顺序
    responses = [FetchResult(url=u) for u in req_urls]
    # 构建映射反查表
    url_to_idx = {u: i for i, u in enumerate(req_urls)}

    # ThreadPoolExecutor 自动管理 thread 的start和join
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 把任务丢进池子之后，立即返回一个Future对象，构建{Future():url}
        future_map = {executor.submit(_fetch_single, u): u for u in req_urls}
        for future in as_completed(future_map):  # as_completed 谁先完成就yield哪一个
            req_url = future_map[future]
            responses[url_to_idx[req_url]] = future.result()  # 真正拿到future的返回值

    logger.info("Batch fetch done %d req_urls cost %.2fs", len(req_urls), time.perf_counter() - start_time)
    return responses


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    urls = ["https://httpbin.org/delay/1"] * 5
    results = batch_fetch(urls)
    for res in results:
        if res.error:
            logger.error(f"❌ {res}")
        else:
            logger.info(f"✅ {res}")
