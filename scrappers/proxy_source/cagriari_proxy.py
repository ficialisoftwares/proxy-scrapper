import requests
from bs4 import BeautifulSoup

URL = "https://cagriari.com/fresh_proxy.txt"


def get_soup(url):
    try:
        html = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/47.0.2526.80 Safari/537.36"}).content
    except Exception as e:
        print("An error occurred while fetching the proxy data from calgary")
        return None
    return BeautifulSoup(html, "lxml")


def get_proxies():
    proxies = []

    soup = get_soup(URL)
    if soup:
        proxy_data = soup.text.split("\n")
        for data in proxy_data:
            if data.startswith('#') == False and data != '':
                proxy_ip = data.split('|')
                ip = proxy_ip[0]
                proxies.append(ip)
        return proxies
    else:
        print("proxy error")

    return proxies

if __name__ == "__main__":
    get_proxies()