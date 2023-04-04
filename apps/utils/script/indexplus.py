"""
@author: Mr_zhang
@software: PyCharm
七麦数据爬取测试
"""

import time
import base64

import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.qimai.cn/rank",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/59.0"
}

params = {
    "market": "6",
    "category": "6",
    "date": "2020-12-11",
    "page": ""
}


# 自定义加密函数
def encrypt(
    a: str,
    n="a12c0fa6ab9119bc90e4ac7700796a53"
) -> str:
    s, n = list(a), list(n)
    sl, nl = len(s), len(n)
    for i in range(0, sl):
        s[i] = chr(ord(s[i]) ^ ord(n[i % nl]))
    return "".join(s)


def main() -> None:
    # iPhone 免费榜单

    # 步骤一：时间差
    t = str(int((time.time() * 1000 - 1515125653845)))
    # 步骤二：提取查询参数值并排序
    s = "".join(sorted([str(v) for v in params.values()]))
    # 步骤三：Base64 Encode
    s = base64.b64encode(bytes(s, encoding="ascii"))
    # 步骤四：拼接自定义字符串
    s = "@#".join([s.decode(), "/rank/marketRank", t, "1"])
    # 步骤五：自定义加密 & Base64 Encode
    s = base64.b64encode(bytes(encrypt(s), encoding="ascii"))
    # 步骤六：拼接 URL
    params["analysis"] = s.decode()
    url = "https://api.qimai.cn/rank/marketRank"
    # 测试：发起请求
    print(params)
    res = requests.get(url, headers=headers, params=params)
    print(res.json())


if __name__ == '__main__':
    main()
