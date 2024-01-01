# asyncIO
# 비동기 I/O coroutine 작업
# None blocking

# Blocking I/O : 호출된 함수가 자식ㄴ의 작업이 완료 될 때까지 제어권을 가지고 있음
# Non Blocking I/O : 호출된 함수가 (서브루틴) return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# thread : 디버깅, 자원 접근 시 race condition, dead lock -> 단점
# coroutine : 하나의 루틴만 실행 -> dead lock없음 -> 제어권으로 실행 -> 단점 : 사용 함수가 비동기로 구현이 되어 있어야함, 혹은 직접 비동기로 구현해야 함


import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading


start = timeit.default_timer()

urls = ["http://daum.net", "https://naver.com", "https://tistory.com"]


async def fetch(url, executor):
    print("thread name : ", threading.current_thread().getName(), "start", url)
    res = await loop.run_in_executor(executor, urlopen, url)
    print("thread name : ", threading.current_thread().getName(), "Done", url)

    return res.read()[0:5]


async def main():
    executor = ThreadPoolExecutor(max_workers=10)
    futures = [asyncio.ensure_future(fetch(url, executor) for url in urls)]

    result = await asyncio.gather(*futures)
    print("result : ", result)


if __name__ == "__main__":
    # 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start
    print("time : ", duration)
