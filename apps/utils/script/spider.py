# -*- coding: utf-8 -*-

"""
数据采集软件
download目录下存储采集下来的数据: 按照系统-日期|分类存储
"""

import os
import time
import random
import json
import xlwt
import execjs
import requests

from fake_useragent import UserAgent


class Spider:

    def __init__(self, ):
        self.username = '17343037825'
        self.password = '17343037825'
        self.market_list = []
        self._error_market_rank = []
        self.js_file = ''
        self.headers = ''
        self.BASEDIR = os.path.dirname(__file__)
        self.DOWNLOAD_PATH = os.path.join(self.BASEDIR, 'download', 'Android', time.strftime('%Y-%m-%d', time.localtime()))

    @staticmethod
    def get_random_user_agent():
        """获取随机请求头"""
        return UserAgent().random

    def get_cookie_sync_time(self):
        """获取cookie时间"""
        headers = self.get_headers()
        cookie_res = requests.get('https://www.qimai.cn/rank/', headers=headers)
        cookie_dict = cookie_res.cookies.get_dict()
        return cookie_dict.get('synct')  # 时间

    def get_analysis(self, params, syn_time, req_url):
        """加密参数"""
        js_file = self.get_js_file_path()
        if self.js_file:
            ctx = execjs.compile(self.js_file)
            return ctx.call("get_analysis", syn_time, params, req_url)
        with open(js_file, 'r', encoding='utf8') as f:
            self.js_file = f.read()
            ctx = execjs.compile(self.js_file)
            return ctx.call("get_analysis", syn_time, params, req_url)

    def get_headers(self):
        """请求头封装"""
        headers = {
            "User-Agent": self.get_random_user_agent(),
            "Origin": "https://www.qimai.cn",
            "Referer": "https://www.qimai.cn/",
            "Accept": "application/json,text/plain,*/*",
        }
        return headers

    @staticmethod
    def get_params(market=None, category=None, page=None, date=None):
        """params参数封装"""
        params = {}
        if market:
            params['market'] = market
        if category:
            params['category'] = category
        if page:
            params['page'] = page
        if date:
            params['date'] = date
        else:
            params['date'] = time.strftime('%Y-%m-%d', time.localtime())
        return params

    def get_js_file_path(self):
        """加载js代码"""
        return os.path.join(self.BASEDIR, 'js/qm.js')

    def login(self):
        """登录七麦"""
        headers = self.get_headers()
        data = {
            "username": self.username,
            "password": self.password,
        }
        analysis = self.get_analysis(self.get_params(), self.get_cookie_sync_time(), '/accountV1/login')
        login_url = 'https://api.qimai.cn/accountV1/login?analysis=%s' % analysis
        login_res = requests.post(url=login_url, data=data, headers=headers)
        headers.update(cookie='='.join([login_res.cookies.items()[0][0], login_res.cookies.items()[0][1]]))
        self.headers = headers

    def get_market(self):
        """获取商店列表|分类"""
        market_list_json = os.path.join(os.path.dirname(__file__), 'market_list.json')
        if os.path.isfile(market_list_json):
            with open(market_list_json, 'r') as f:
                # 应用列表缓存在文件中，减少网络请求
                return json.loads(f.read())
        parmas = self.get_params()
        mark_list_url = 'https://api.qimai.cn/rank/marketList'
        analysis = self.get_analysis(parmas, self.get_cookie_sync_time(), '/rank/marketList')
        parmas['analysis'] = analysis
        mark_list_res = requests.get(url=mark_list_url, params=parmas, headers=self.headers)
        if mark_list_res.json().get('code') == 10000:
            with open(market_list_json, 'w') as f:
                f.write(json.dumps(mark_list_res.json().get('marketList'), ensure_ascii=False, indent=4))
                return mark_list_res.json().get('marketList')

    def repair_market(self, market_list):
        """对商店数据做二次处理"""
        for market in market_list:
            market_id = market.get('market_id')
            market_name = market.get('market_name')
            if market.get('categoryList'):
                for category in market['categoryList']:
                    category_id = category.get('category_id')
                    category_name = category.get('category_name')
                    self.market_list.append(
                        {
                            'market_id': market_id,
                            'market_name': market_name,
                            'category_id': category_id,
                            'category_name': category_name
                        }
                    )
                    if category.get('subClass'):
                        for sub in category['subClass']:
                            sub_category_id = sub.get('category_id')
                            sub_category_name = sub.get('category_name')
                            self.market_list.append(
                                {
                                    'market_id': market_id,
                                    'market_name': market_name,
                                    'category_id': sub_category_id,
                                    'category_name': sub_category_name
                                }
                            )

    def dict_init(self):
        """目录初始化"""
        for market in self.market_list:

            DATE_PATH = self.DOWNLOAD_PATH
            if not os.path.exists(DATE_PATH):
                os.mkdir(DATE_PATH)

            MARKET_PATH = os.path.join(DATE_PATH, market['market_name'])
            if not os.path.exists(MARKET_PATH):
                os.mkdir(MARKET_PATH)

            CATEGORY_PATH = os.path.join(MARKET_PATH, market['category_name'])
            if not os.path.exists(CATEGORY_PATH):
                os.mkdir(CATEGORY_PATH)

    def get_market_rank(self):
        """获取市场排名列表"""
        market_rank_url = 'https://api.qimai.cn/rank/marketRank'
        print('*' * 20, 'Count:', len(self.market_list))
        for market in self.market_list:
            print('start: ', market)
            start_time = time.time()
            parmas = self.get_params(market=market.get('market_id'), category=market.get('category_id'))
            analysis = self.get_analysis(parmas, self.get_cookie_sync_time(), '/rank/marketRank')
            parmas['analysis'] = analysis
            _market_rank_res = requests.get(url=market_rank_url, params=parmas, headers=self.headers, timeout=5)

            try:
                print(_market_rank_res.json())
                if _market_rank_res.json().get('code') == 10000:
                    self.save_excel(
                        _market_rank_res=_market_rank_res,
                        parmas=parmas,
                        market_rank_url=market_rank_url,
                        market=market
                    )
            except Exception as e:
                print(e)
                self._error_market_rank.append(market)
            finally:
                print('end: ', market, 'consume: ', time.time() - start_time)
                time.sleep(random.randint(2, 4))

        print('爬取失败商店: ', self._error_market_rank)

    def save_excel(self, _market_rank_res, parmas, market_rank_url, market):
        """数据写入Excel"""
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('sheet1')
        head_field = ['AppName', 'Publisher', 'Company', 'AppScore', 'AppComment']
        for i in range(len(head_field)):
            worksheet.col(i).width = 256 * 20
            worksheet.write(0, i, label=head_field[i])
        try:
            cow_num = 1
            for i in range(1, _market_rank_res.json().get('maxPage') + 1):
                if parmas.get('analysis'):
                    del parmas['analysis']
                parmas['page'] = i
                analysis = self.get_analysis(parmas, self.get_cookie_sync_time(), '/rank/marketRank')
                parmas['analysis'] = analysis
                market_rank_res = requests.get(url=market_rank_url, params=parmas, headers=self.headers)

                if market_rank_res.json().get('code') == 10000 and market_rank_res.json().get('rankInfo'):
                    for rank in market_rank_res.json()['rankInfo']:
                        worksheet.write(cow_num, 0, label=rank.get('appInfo').get('appName'))
                        worksheet.write(cow_num, 1, label=rank.get('appInfo').get('publisher'))
                        worksheet.write(cow_num, 2, label=rank.get('company').get('name'))
                        worksheet.write(cow_num, 3, label=rank.get('appInfo').get('app_comment_score'))
                        worksheet.write(cow_num, 4, label=rank.get('appInfo').get('app_comment_count'))
                        cow_num += 1

        except Exception as e:
            print(e)
        finally:
            workbook.save(self.get_save_file_name(market.get('market_name'), market.get('category_name')))
            print('商店: {market_name}  分类: {category_name} 已写入Excel！'.format(
                market_name=market.get('market_name'),
                category_name=market.get('category_name')
            ))

    def get_save_file_name(self, market_name, category_name):
        """Excel存储文件名"""
        return os.path.join(self.DOWNLOAD_PATH, market_name, category_name, 'data.xls')

    def run(self):
        """
        爬虫主程序
        用户登录 - > 获取已认证cookie
        """
        self.login()
        self.repair_market(self.get_market())  # 商店名称统一格式
        self.dict_init()  # 目录初始化
        self.get_market_rank()  # 爬取商店->应用分类

    def repair_data(self, market_list):
        """对异常数据单独爬取"""
        market_rank_url = 'https://api.qimai.cn/rank/marketRank'
        self.login()
        for market in market_list:
            parmas = self.get_params(market=market.get('market_id'), category=market.get('category_id'))
            analysis = self.get_analysis(parmas, self.get_cookie_sync_time(), '/rank/marketRank')
            parmas['analysis'] = analysis
            _market_rank_res = requests.get(url=market_rank_url, params=parmas, headers=self.headers, timeout=5)

            try:
                if _market_rank_res.json().get('code') == 10000:
                    self.save_excel(
                        _market_rank_res=_market_rank_res,
                        parmas=parmas,
                        market_rank_url=market_rank_url,
                        market=market
                    )
            except Exception as e:
                self._error_market_rank.append(market)
            finally:
                time.sleep(random.randint(2, 4))
        print('爬取失败商店: ', self._error_market_rank)


if __name__ == '__main__':
    start = time.time()
    spider = Spider()
    spider.run()
    print(time.time() - start)
    # print(spider.get_random_user_agent())
    # print(spider.get_js_file_path())
    # print(spider.get_cookie())
    # print(spider.get_cookie_sync_time())
    # print(spider.get_session())
    # print(spider.get_market_list())
    # print(spider.get_market_rank())
    # print(spider.dict_init())
    # print(spider.login())
    # spider.get_headers(spider.login())
    # print(spider.get_save_file_name('百度', 'MOBA'))
