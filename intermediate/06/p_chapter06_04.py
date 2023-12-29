# future, threading, multi-processing
# 비동기 작업
# 동기 A -> B: block cpu, resource 낭비 방지,
# ex) nerwork ,I/O 관련 작업을 동시성 활용 권장
# 성능향상

# 기존
import threading
import multiprocessing

# 2가지 패턴
# concurrent.futures -> threading wrapping
# futures : 비동기 실행을 위한 API를 고수준으로 작성
# 1. Multi threading, multi processing API 통일
# 2. 실행중인 작업 취소, 완료여부, 타임아웃, 콜백, 동기화 코드 쉬움 -> promise 개념

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점 방지위해 GIL실행
# 리소스 전체에 lock걸림 -> context switch 비용 -> 여러 thread가 오히려 단일 thread보다 오래걸릴수도
# 그래서 multi-processing, Cpython이용해서 GIL우회
import os
import time
from concurrent import futures

WORK_LIST = [10000, 1000000, 10000000, 10000000]

# 동시성 합계 계산 메인 함수


def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # worker count
    worker = min(10, len(WORK_LIST))
    start_tm = time.time()

    with futures.ThreadPoolExecutor() as excutor:
        # map은 작업순서를 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)  # result : list

    end_tm = time.time() - start_tm
    msg = "\n Result -> {}Time : {:.2f}s"
    print(msg.format(list(result), end_tm))


if __name__ == "__main__":
    main()
