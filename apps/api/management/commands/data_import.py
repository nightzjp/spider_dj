import os
import datetime
import requests
import time
import random
import pandas as pd

from django.core.management.base import BaseCommand
from django.conf import settings

from api import models
from utils.constant import CHINAZ_KEY


class Command(BaseCommand):
    help = 'Get the value from the message queue and write to queue'
    
    def __init__(self, *args, **kwargs):
        self.BASE_DIR = settings.BASE_DIR
        # self._file_name = os.path.join(self.BASE_DIR, 'static', 'ICP-domain8-23.xlsx')
        self.file_name = os.path.join(self.BASE_DIR, 'static', 'excel', 'ICP8.23—8.27.xlsx')
        self.chinaz_url = 'https://apidatav2.chinaz.com/single/ip'
        super(Command, self).__init__(*args, **kwargs)
        
    def add_arguments(self, parser):
        parser.add_argument(
            '--ex_type', nargs='?',
            help='导入脚本功能: all表示首先导入excel数据，然后更新相关数据; file_import表示只导入数据; update_report表示只更新表单')

    def handle(self, *args, **options):
        command = options.get('ex_type')
        if not command:
            print("请输入正确指令:")
            print("--ex_type=all 表示第一步执行excel导入，导入成功之后执行表单更新操作")
            print("--ex_type=file_import 表示只导入excel至数据库")
            print("--ex_type=update_report 表示更新已导入表单数据")
            return
        if command == 'all':
            start = time.time()
            print("-------------------------------------------%s------------------------------------------" % 'excel开始导入')
            self.file_import()
            print("-------------------------------------------%s------------------------------------------" % 'excel导入成功')
            print(time.time() - start)
            self.update_report()
        elif command == 'file_import':
            start = time.time()
            print("-------------------------------------------%s------------------------------------------" % 'excel开始导入')
            self.file_import()
            print("-------------------------------------------%s------------------------------------------" % 'excel导入成功')
            print(time.time() - start)
        elif command == 'update_report':
            self.update_report()
        else:
            print("未识别到有效指令")
            return
        
    def file_import(self):
        """excel导入"""
        """
        域名解析表
        # Organizer        主办单位
        # Operating status  经营状态
        # Date of establishment 成立日期
        # Registered capital 注册资金
        # Website URL 网站地址
        # Website detection 网站监测
        # Person in charge of filing  备案负责人
        # CEO 企业负责人
        # phone 联系电话
        # email Email邮箱
        # Station phone 站内电话
        # In-site mailbox 站内邮箱
        # Search promotion 搜索推广
        # Review time 审核时间
        """
        excel = pd.read_excel(self.file_name, sheet_name=0, skiprows=[0])
        for idx, item in excel.iterrows():
            if not models.DomainReport.objects.filter(organizer=item[1], website_url=item[5]).exists():
                models.DomainReport.objects.create(
                    organizer=item[1], operating_status=item[2], date_of_establishment=item[3], registered_capital=item[4],
                    website_url=item[5], website_detection=item[6], person_in_charge_of_filing=item[7], ceo=item[8],
                    phone=item[9], email=item[10], station_phone=item[11], in_site_mailbox=item[12], search_promotion=item[13],
                    review_time=item[14]
                )
                print("Idx: {idx}, ProductName: {organizer}, ProductDomain: {website_url} insert success.".format(idx=idx, organizer=item[0], website_url=item[5]))
            else:
                print("Idx: {idx}, ProductName: {organizer}, ProductDomain: {website_url} already exist.".format(idx=idx, organizer=item[0], website_url=item[5]))
    
    def update_report(self):
        now_date = datetime.datetime.now().date()
        session = self.get_session()
        domain_report_list = models.DomainReport.objects.filter(create_at__gte=now_date, reason__isnull=True)
        for domain_report in domain_report_list:
            params = {
                'key': CHINAZ_KEY,
                'ip': domain_report.website_url
            }
            try:
                res = session.get(self.chinaz_url, params=params, timeout=1).json()
                print(res)
                state_code = res.get('StateCode')
                reason = res.get('Reason')
                if state_code == 1 and reason == '成功':
                    ip = res['Result'].get('IP', None)
                    city = res['Result'].get('City', None)
                    country = res['Result'].get('Country', None)
                    district = res['Result'].get('District', None)
                    isp = res['Result'].get('Isp', None)
                    province = res['Result'].get('Province', None)
                    post_code = res['Result'].get('ZipCode', None)
                    area_code = res['Result'].get('AreaCode', None)
                else:
                    ip = ''
                    city = ''
                    country = ''
                    district = ''
                    isp = ''
                    province = ''
                    post_code = ''
                    area_code = ''

            except Exception as e:
                print(e)
                continue
            else:
                models.DomainReport.objects.filter(
                    id=domain_report.id
                ).update(
                    state_code=state_code, reason=reason, ip=ip, city=city, country=country, district=district, isp=isp,
                    province=province, post_code=post_code, area_code=area_code
                )
            finally:
                time.sleep(random.random())
        
    @staticmethod
    def get_session():
        return requests.session()

