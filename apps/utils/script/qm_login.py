# -*- coding: utf-8 -*-

import requests

from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    "User-Agent": ua.chrome,
    "Origin": "https://www.qimai.cn",
    "Referer": "https://www.qimai.cn/",
    "Accept": "application/json,text/plain,*/*",
}

cookie = requests.get(url='https://api.qimai.cn/rank', headers=headers)

headers['cookie'] = "=".join([cookie.cookies.items()[0][0], cookie.cookies.items()[0][1]])

print(headers)
data = {
    "username": 17343037825,
    "password": 17343037825,
}

login = requests.post(url='https://api.qimai.cn/accountV1/login?analysis=eEcbVwJTX0VeRGYBFwhYXw1adkIJAgYBAwEADVcAACQXBw%3D%3D', data=data, headers=headers)
print(login.json())
print(login.cookies)