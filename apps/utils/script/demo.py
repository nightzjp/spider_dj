"""
@author: Mr_zhang
@software: PyCharm
测试代码，测试IP归属地
"""


import requests
from bs4 import BeautifulSoup
import re


url = 'https://www.ipip.net/ip.html'
while True:
    # ip = input('输入你要查询的IP：')
    data = {'ip': '116.62.84.58'}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    r = requests.post(url, data=data, headers=header)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.find_all(name=['span', 'a'])
    ip = re.findall('<a href=".*?style="background: none;color: #0A246A;width: auto;">(.*?)</a>', str(span))
    localtion = re.findall(
        '<span style="display: inline-block;text-align: center;width: 720px;float: left;line-height: 46px;height: 46px;">(.*?)</span>, <span style="float: right">',
        str(span))
    print('------ipip地址查询工具------')
    print('当前查询的ip为：' + str(ip))
    print('当前查询的ip地址为：' + str(localtion))