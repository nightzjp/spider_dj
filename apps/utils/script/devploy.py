"""
@author: Mr_zhang
@software: PyCharm
http请求测试
"""

import time
import requests
import httpx
import aiohttp
import asyncio


url = 'http://118.89.19.78:8028/service/update'


# ##################################### 时间装饰器 ###################################################


def wrapper(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return inner

# ##################################### 同步请求 ###################################################


@wrapper
def requests_sync_test(count=100):
    session = requests.Session()
    for _ in range(count):
        res = session.get(url=url)
        print(res.json())


@wrapper
def http_x_sync_test(count=100):
    for _ in range(count):
        res = httpx.get(url=url)
        print(res.json())


# ##################################### 异步请求 ###################################################


async def request(client):
    resp = await client.get(url=url)
    result = resp.json()
    print(result)


@wrapper
async def http_x_async_test(count=100):
    async with httpx.AsyncClient() as client:
        task_list = []
        for _ in range(count):
            task = asyncio.create_task(
                request(client=client)
            )
            task_list.append(task)
        await asyncio.gather(*task_list)


@wrapper
async def aio_http_async_text(count=100):
    """废弃|太慢"""
    async with aiohttp.ClientSession() as client:
        for _ in range(count):
            res = await client.get(url=url)
            res_json = await res.json()
            print(res_json)


if __name__ == '__main__':
    requests_sync_test(count=10)
    # asyncio.run(http_x_async_test(10))
    # asyncio.run(aio_http_async_text(10))
