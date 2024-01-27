"""
    processpoolexecutor, as_completed,futures,timeout,dict
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# GIL, io bound -> multi-processing, async 사용 추천

URLS = [
    "http://www.daum.net",
    "http://www.cnn.com",
    "http://naver.com",
    "http://ruliweb",
    "http://some-made-up-domain.com",
]


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    with ProcessPoolExecutor(max_workers=5) as executor:
        # future 로드(실행x)
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                print(e)
            else:
                print(url, len(data))


if __name__ == "__main__":
    main()
