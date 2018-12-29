__author__ = "mpn"

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_ip(html):
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='info__value info__value_type_ipv4').text.strip()
    return ip


def main():
    url = 'https://yandex.ru/internet/'
    rez = get_ip((get_html(url)))
    print('IP = ', rez)


if __name__ == '__main__':
    main()
