"""
    IO Bound
    threading vs asyncio vs multiprocessing
    I/O bound, requests, threading
    aync는 cpu bound가 아닌 다른 자원을 쓸때사용 (network, IO..) -> 만약 복잡한 cpu계산을 넣으면 sync하게 돌아감, 즉 다른 외부자원이 일을하고 callback해서 cpu한테 다되었다고 알려주는거
    thread는 걍 논리적으로 cpu가 여러개
"""

# pip install requests
import requests
import time
import concurrent.futures
import threading

# 각 스레드에 생성되는 객체, 독립된 네임스페이스
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def request_site(url):
    session = get_session()
    with session.get(url) as response:
        print(len(response.content), response.status_code, url)


def request_all_sites(urls):
    # multi thread
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)


def main():
    # test url
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com",
    ] * 5

    start_time = time.time()
    request_all_sites(urls)
    duration = time.time() - start_time

    print(len(urls), duration)


if __name__ == "__main__":
    main()


########################


# pip install requests
import requests
import time
import concurrent.futures
import multiprocessing

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때 마다 객체 생성은 비추 -> 각 프로세스마다 할당
session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def request_site(url):
    print(session)
    with session.get(url) as response:
        name = multiprocessing.current_process().name

        print(len(response.content), response.status_code, url, name)


def request_all_sites(urls):
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


def main():
    # test url
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com",
    ] * 5

    start_time = time.time()
    request_all_sites(urls)
    duration = time.time() - start_time

    print(len(urls), duration)


if __name__ == "__main__":
    main()


#######################

"""
    asyncio
    패러다임 변화
    싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> cpu연산, DB연동, API호출 대기 시간 늘어남 -> 비동기, await..(sys -> user)
    파이썬 -> 비동기(aync io) 표준라이브러리 등장
"""

import time
import asyncio


def test():
    pass


def test1():
    pass


def test2():
    pass


# async
test()
test1()
test2()


async def test1():  # coroutine object
    await test2()


async def test2():
    pass


def exe_calculate_sync(name, n):
    for i in range(i, n + 1):
        print(name, i, n)
        time.sleep(1)
    print(name)


def process_sync():
    start = time.time()
    exe_calculate_sync("one", 1)
    exe_calculate_sync("two", 2)
    exe_calculate_sync("three", 3)
    end = time.time()
    print(end - start)


async def exe_calculate_async(name, n):
    for i in range(i, n + 1):
        print(name, i, n)
        await asyncio.sleep(1)
        # time.sleep(1)
    print(name)


async def process_async():
    start = time.time()

    await asyncio.wait(
        [
            exe_calculate_async("one", 1),
            exe_calculate_async("two", 2),
            exe_calculate_async("three", 3),
        ]
    )

    end = time.time()
    print(end - start)


if __name__ == "__main__":
    # process_sync()

    asyncio.run(process_async())


#################
# pip install requests
# import requests
import time
import concurrent.futures
import multiprocessing
import asyncio
import aiohttp

# pip install aiohttp


async def request_sites(session, url):
    print(session)
    async with session.get(url) as response:
        print(response.content_length, url)


async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_site(session, url))
            task.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)


def main():
    # test url
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com",
    ] * 5

    start_time = time.time()
    # The line `# request_all_sites(urls)` is commented out, which means it is not being executed.
    # request_all_sites(urls)
    # asyncio.run(request_all_sites(urls))
    asyncio.get_event_loop().run_until_complete(request_all_sites(urls))
    duration = time.time() - start_time

    print(len(urls), duration)


if __name__ == "__main__":
    main()
