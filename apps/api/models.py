from django.db import models

from public.models import BaseModel


class DomainReport(BaseModel):
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
        
        # Next contact time 下次联系时间
        # Industry 行业
        # Relevance 关联情况  | 报备  已报备  已关联
        # Whether to add WeChat 是否加微信 | 是、已通过  是、未通过  否
        # Communication content 沟通内容
        # Intention degree 意向度 | A B C D 未接通 失效电话  手机拨打
    """
    RELEVANCE = (
        (0, '-'),
        (1, '未关联'),
        (2, '已关联'),
        (3, '未报备'),
        (4, '已报备')
    )
    WE_CHAT = (
        (0, '-'),
        (1, '未添加'),
        (2, '已添加-未通过'),
        (3, '已添加-已通过')
    )
    INTENTION_DEGREE = (
        (0, '-'),
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
        (5, '未接通'),
        (6, '失效电话'),
        (7, '手机拨打'),
    )
    
    organizer = models.CharField(max_length=512, null=True, blank=True, verbose_name='主办单位')
    operating_status = models.CharField(max_length=512, null=True, blank=True, verbose_name='经营状态')
    date_of_establishment = models.CharField(max_length=512, null=True, blank=True, verbose_name='成立日期')
    registered_capital = models.CharField(max_length=512, null=True, blank=True, verbose_name='注册资金')
    website_url = models.CharField(max_length=512, null=True, blank=True, verbose_name='网站地址')
    website_detection = models.CharField(max_length=512, null=True, blank=True, verbose_name='网站监测')
    person_in_charge_of_filing = models.CharField(max_length=512, null=True, blank=True, verbose_name='备案负责人')
    ceo = models.CharField(max_length=512, null=True, blank=True, verbose_name='企业负责人')
    phone = models.CharField(max_length=512, null=True, blank=True, verbose_name='联系电话')
    email = models.CharField(max_length=512, null=True, blank=True, verbose_name='Email邮箱')
    station_phone = models.CharField(max_length=512, null=True, blank=True, verbose_name='站内电话')
    in_site_mailbox = models.CharField(max_length=512, null=True, blank=True, verbose_name='站内邮箱')
    search_promotion = models.CharField(max_length=512, null=True, blank=True, verbose_name='搜索推广')
    review_time = models.CharField(max_length=512, null=True, blank=True, verbose_name='审核时间')
    state_code = models.SmallIntegerField(default=0, verbose_name='状态码')
    reason = models.CharField(max_length=512, null=True, blank=True, verbose_name='状态说明')
    ip = models.CharField(max_length=512, null=True, blank=True, verbose_name='IP')
    city = models.CharField(max_length=512, null=True, blank=True, verbose_name='所在城市')
    country = models.CharField(max_length=512, null=True, blank=True, verbose_name='所在国家')
    district = models.CharField(max_length=512, null=True, blank=True, verbose_name='所在地区')
    isp = models.CharField(max_length=512, null=True, blank=True, verbose_name='运营商')
    province = models.CharField(max_length=512, null=True, blank=True, verbose_name='所在省份, 州')
    post_code = models.CharField(max_length=512, null=True, blank=True, verbose_name='邮政编码')
    area_code = models.CharField(max_length=512, null=True, blank=True, verbose_name='区号')
    
    next_contact_time = models.DateTimeField(null=True, blank=True, verbose_name='下次联系时间')
    industry = models.CharField(max_length=512, null=True, blank=True, verbose_name='行业')
    relevance = models.SmallIntegerField(choices=RELEVANCE, default=0, verbose_name='关联情况')
    whether_to_add_we_chat = models.SmallIntegerField(choices=WE_CHAT, default=0, verbose_name='是否添加微信')
    communication_content = models.CharField(max_length=512, null=True, blank=True, verbose_name='沟通内容')
    intention_degree = models.SmallIntegerField(choices=INTENTION_DEGREE, default=0, verbose_name='意向度')
    
    class Meta:
        verbose_name = '转换报表'
        verbose_name_plural = verbose_name
        index_together = ['organizer', 'website_url']


