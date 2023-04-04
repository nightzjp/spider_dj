import os
import sys
import time
import xlwt
import execjs
import requests
from fake_useragent import UserAgent


BASEDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))
JS_FILE = os.path.join(BASEDIR, 'js/qm.js')

sys.path.insert(0, BASEDIR)

ua = UserAgent()

headers = {
    "User-Agent": ua.chrome,
    "Origin": "https://www.qimai.cn",
    "Referer": "https://www.qimai.cn/",
    "Accept": "application/json,text/plain,*/*",
    "cookie": "PHPSESSID=mke1jvenuc685v2jstdceemft7"  # PHPSESSID=ba6gs6do7uj9i108mbikgkcv35
}

params = {
    'market': '6',
    'category': '6',
    'date': '2020-12-11',
    'page': ''
}
resp = requests.get('https://www.qimai.cn/rank/', headers=headers)
t = resp.cookies.get_dict()
synct = t.get('synct')  # 时间


def get_analysis(synct, params, url):
    js_path = JS_FILE
    with open(js_path, 'r', encoding='utf8') as f:
        js_content = f.read()
        ctx = execjs.compile(js_content)
        new_pwd = ctx.call("get_analysis", synct, params, url)
        return new_pwd


analysis = get_analysis(synct, params, '/rank/marketList')
#
params['analysis'] = analysis

# https://api.qimai.cn/rank/marketRank?analysis=dQ51TyxzAEh9WQBIdTBuCiQXGRNRXlsfXVFCUwFDagVaXSETCQIFAwABDVwCAFF0FVA%3D&market=6&category=6&date=2020-12-11
url = 'https://api.qimai.cn/rank/marketList'
res = requests.get(url=url, headers=headers, params=params)
print(res.json())


# start_time = time.time()
# workbook = xlwt.Workbook(encoding='ascii')
# worksheet = workbook.add_sheet('sheet1')
# head_field = ['AppName', 'Publisher', 'Company', 'AppScore', 'AppComment']
# for i in range(len(head_field)):
#     worksheet.col(i).width = 256 * 20
#     worksheet.write(0, i, label=head_field[i])
#
# cow_num = 1
# for i in range(1, 11):
#     if params.get('analysis'):
#         del params['analysis']
#     params['page'] = str(i)
#     analysis = get_analysis(synct, params)
#     params['analysis'] = analysis
#     res = requests.get(url=url, headers=headers, params=params)
#
#     for rank in res.json().get('rankInfo'):
#         worksheet.write(cow_num, 0, label=rank.get('appInfo').get('appName'))
#         worksheet.write(cow_num, 1, label=rank.get('appInfo').get('publisher'))
#         worksheet.write(cow_num, 2, label=rank.get('company').get('name'))
#         worksheet.write(cow_num, 3, label=rank.get('appInfo').get('app_comment_score'))
#         worksheet.write(cow_num, 4, label=rank.get('appInfo').get('app_comment_count'))
#         cow_num += 1
#
#     workbook.save('demo.xls')
