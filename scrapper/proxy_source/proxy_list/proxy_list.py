import requests
from bs4 import BeautifulSoup

URLS = ["https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxy-list.download/api/v1/get?type=https"
        "https://www.proxy-list.download/api/v1/get?type=sock4",
        "https://www.proxy-list.download/api/v1/get?type=sock5"
        ]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/47.0.2526.80 Safari/537.36"}


def get_soup(url):
    try:
        html = requests.get(url, headers=HEADERS).content
    except Exception as e:
        print("An error occurred while fetching the proxy data from calgary")
        return
    return BeautifulSoup(html, "lxml")


def get_proxies():
    proxies = []
    for URL in URLS:
        soup = get_soup(URL)
        if soup:
            proxy_data = soup.text.split("\n")
            for ip in proxy_data:
                proxies.append(ip.strip())
        else:
            print("proxy error")
    proxies = set(proxies)
    proxies = list(proxies)
    return proxies


if __name__ == "__main__":
    get_proxies()
