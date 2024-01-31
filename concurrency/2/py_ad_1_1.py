"""
    process,thread,병렬성
    1. parrallelism :
        - 완전히 동일한 타이밍에 태스크 실행
        - 다양한 파트로 나눠서 실행(합 나눠서 구하고 취합)
        - 멀티프로세싱에서 cpu가 1core인 경우 만족하지 않음
        - 딥러닝에서 I/O, network bounding에서는 GIL때문에 multi-threading대신 multi-processing을 사용

    2. process vs thread
        - 독립된 메모리(프로세스), 공유메모리(스레드)
        - 많은 메모리(프로세스), 적은 메모리(스레드)
        - 좀비프로세스 생성 가능성, 좀비스레드 생성 별로 없음
        - 오버헤드 큼(프로스세), 오버헤드 적음(스레드)
        - 생성소멸 다소 느림(프로세스), 생성/소멸 빠름(스레드)
        - 코드 작성 쉬움/디버깅 어려움(프로세스), 코드작성 어려움/디버깅 어려움(스레드)
"""
