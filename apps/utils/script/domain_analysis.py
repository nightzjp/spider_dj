# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: domain_analysis.py
@time: 2021/8/23 上午10:00
通过域名查看服务器所在地|可通过第三方接口付费查询
"""

import os
import socket
import time
import json
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


class DomainAnalysis:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.file_name = os.path.join(self.BASE_DIR, "data", "ICP-domain8-23.xlsx")
        self.base_url = 'https://ip.tool.chinaz.com/{url}'
        self.session = requests.session()
    
    @staticmethod
    def parse_html(html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            address = soup.find_all("em")[-1].text
        except Exception as e:
            address = "--"
        finally:
            return address
    
    def get_html(self, url):
        return self.session.get(url, timeout=1)
    
    def read_excel(self):
        return pd.read_excel(self.file_name, sheet_name=0)
    
    def save_excel(self, excel):
        """必须xls，xlsx等结尾，否则会出现异常"""
        file_name = self.file_name + '.res.xls'
        excel.to_excel(file_name, index=False)
    
    def excel_to_json(self, lis_res):
        # with open('ab.json', 'w') as f:
        # f.write(json.dumps({"data": lis_res}, ensure_ascii=False, indent=4))
        file_name = self.file_name + '.json'
        with open(file_name, 'w') as f:
            f.write(json.dumps({"data": lis_res}, ensure_ascii=False, indent=4))
    
    def run(self):
        lis_res = []
        excel = self.read_excel()
        for idx, item in excel.iterrows():
            print(item[0], item[1], item[2])
            com_url = self.base_url.format(url=item[1])
            try:
                time.sleep(1)
                response = self.get_html(com_url)
                if response.status_code == 200:
                    address = self.parse_html(response.text)
            except Exception as e:
                address = "--"
            finally:
                print(address)
                excel.iloc[idx, 2] = address
                lis_res.append({
                    "name": item[0],
                    "domain": item[1],
                    "address": address
                })
        self.excel_to_json(lis_res)
        self.save_excel(excel)
    

#
# res = requests.get(url='https://ip.tool.chinaz.com/yiwanghuizhan.com')
# soup = BeautifulSoup(res.text, 'html.parser')
#
# print(soup.find_all("em")[-1].text)

# who_ip_wrap = soup.find_all("div", class_="WhoIpWrap jspu")[0]
#
# address = who_ip_wrap.find_all("span", class_="Whwtdhalf w30-0 lh24 tl ml80")[0]
#
# print(address.find_all("em")[0].text)

# excel = pd.read_excel(file_name, sheet_name="Sheet1")


# with open(file_json, 'r') as f:
#     lis = json.loads(f.read())
#
# session = requests.session()
# lis_res = []
# for item in lis.get('data'):
#     com_url = base_url.format(url=item.get('domain'))
#     try:
#         res = session.get(com_url, timeout=1)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         print(soup.find_all("em")[-1].text)
#         address = soup.find_all("em")[-1].text
#     except Exception as e:
#         address = '-'
#     finally:
#         print(item['name'])
#         time.sleep(0.5)
#         lis_res.append({
#             "name": item['name'],
#             "domain": item['domain'],
#             "address": address
#         })
#
# with open('ab.json', 'w') as f:
#     f.write(json.dumps({"data": lis_res}, ensure_ascii=False, indent=4))

# with open("ab.json", 'r') as f:
#     res_list = json.loads(f.read())

# for item in res_list.get('data'):
#     print(item)

# r = pd.DataFrame(res_list.get('data'))
#
# print(r.to_csv('ab.csv'))


# excel = pd.read_excel(file_name, sheet_name=0)
#
#
# for idx, item in excel.iterrows():
#     # print(idx)
#     # print(excel.iloc[idx][excel.columns[2]])
#     # print(excel.loc[idx][excel.columns[2]])
#     excel.iloc[idx, 2] = "-----"
#     # print(item[0], item[1], item[2])
#
# excel.to_excel('xxx.xls', index=False)

if __name__ == '__main__':
    domain = DomainAnalysis()
    domain.run()
