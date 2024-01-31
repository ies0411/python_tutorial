"""
    multiprocessing vs threading vs aync IO
    CPU Bound,I/O Bound, Async IO

    CPU Bound vs I/O Bound

    CPU Bound
    - 프로세스 진행 -> CPU속도에 의해 제한(결정) -> 행렬 곱, 고속 연산, 압축 파일, 집합 연산 등
    - CPU연산 위주 작업
    - CPU성능에 의해 달라짐

    I/O Bound
    - 파일 쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 병목이 결정
    - CPU성능 지표가 크게 영향을 끼치지 않음

    메모리 바인딩, 캐시바운딩
    작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요

    -multiprocessing : multiple processes, 고가용성(CPU) utilization -> CPU-Bound
    -Threading : single(multi) processing, multiple threads, OS decides task switching-> Fast I/O bound
    -AsyncIO : single process,single thread,cooperative multitasking,tasks cooperatively decide switching

"""
