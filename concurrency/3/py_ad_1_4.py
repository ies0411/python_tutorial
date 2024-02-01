"""
    IO Bound - synchronous
    IO BOund, requests
"""

# pip install requests
import requests
import time


def request_site(url, session):
    print(session)
    print(session.headers)
    with session.get(url) as response:
        print(len(response.content), response.status_code, url)


def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)


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
