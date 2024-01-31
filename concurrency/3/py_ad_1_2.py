"""
    blocking vs non-blocking IO
    blocking IO, Non-Blocking IO, Sync, Aync
    blocking IO vs Non-blocking IO

    blocking IO
    - sys call 요청시 -> 커널 IO 작업 완료 시 까지 응답 대기
    - 제어권(IO작업) -> 커널 소유 -> 응답(response)전 까지 대기(block) -> 다른 작업 수행 불가(대기)

    non-blocking IO
    - 시스템 콜 요청시 -> 커널 IO 작업 완료 여부 상관없이 즉시 응답
    - 제어권(IO작업) -> 유저프로세스 -> 다른 작업 수행 가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료 여부 확인

    Async vs Sync
    async : IO 작업 완료 여부에 대한 Noty는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수)
    sync : IO 작업 완료 여부에 대한 Noty는 유저프로세스(호출하는 함수) -> 커널(호출되는함수)
"""
