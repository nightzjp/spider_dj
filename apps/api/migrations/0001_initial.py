# Generated by Django 3.1.4 on 2021-08-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='删除时间')),
                ('create_by', models.CharField(default='', max_length=32, verbose_name='创建人')),
                ('detail', models.CharField(default='', max_length=200, verbose_name='备注信息')),
                ('organizer', models.CharField(blank=True, max_length=512, null=True, verbose_name='主办单位')),
                ('operating_status', models.CharField(blank=True, max_length=512, null=True, verbose_name='经营状态')),
                ('date_of_establishment', models.CharField(blank=True, max_length=512, null=True, verbose_name='成立日期')),
                ('registered_capital', models.CharField(blank=True, max_length=512, null=True, verbose_name='注册资金')),
                ('website_url', models.CharField(blank=True, max_length=512, null=True, verbose_name='网站地址')),
                ('website_detection', models.CharField(blank=True, max_length=512, null=True, verbose_name='网站监测')),
                ('person_in_charge_of_filing', models.CharField(blank=True, max_length=512, null=True, verbose_name='备案负责人')),
                ('ceo', models.CharField(blank=True, max_length=512, null=True, verbose_name='企业负责人')),
                ('phone', models.CharField(blank=True, max_length=512, null=True, verbose_name='联系电话')),
                ('email', models.CharField(blank=True, max_length=512, null=True, verbose_name='Email邮箱')),
                ('station_phone', models.CharField(blank=True, max_length=512, null=True, verbose_name='站内电话')),
                ('in_site_mailbox', models.CharField(blank=True, max_length=512, null=True, verbose_name='站内邮箱')),
                ('search_promotion', models.CharField(blank=True, max_length=512, null=True, verbose_name='搜索推广')),
                ('review_time', models.CharField(blank=True, max_length=512, null=True, verbose_name='审核时间')),
                ('state_code', models.SmallIntegerField(default=0, verbose_name='状态码')),
                ('reason', models.CharField(blank=True, max_length=512, null=True, verbose_name='状态说明')),
                ('ip', models.CharField(blank=True, max_length=512, null=True, verbose_name='IP')),
                ('city', models.CharField(blank=True, max_length=512, null=True, verbose_name='所在城市')),
                ('country', models.CharField(blank=True, max_length=512, null=True, verbose_name='所在国家')),
                ('district', models.CharField(blank=True, max_length=512, null=True, verbose_name='所在地区')),
                ('isp', models.CharField(blank=True, max_length=512, null=True, verbose_name='运营商')),
                ('province', models.CharField(blank=True, max_length=512, null=True, verbose_name='所在省份, 州')),
                ('post_code', models.CharField(blank=True, max_length=512, null=True, verbose_name='邮政编码')),
                ('area_code', models.CharField(blank=True, max_length=512, null=True, verbose_name='区号')),
                ('next_contact_time', models.DateTimeField(blank=True, null=True, verbose_name='下次联系时间')),
                ('industry', models.CharField(blank=True, max_length=512, null=True, verbose_name='行业')),
                ('relevance', models.SmallIntegerField(choices=[(0, '-'), (1, '未关联'), (2, '已关联'), (3, '未报备'), (4, '已报备')], default=0, verbose_name='关联情况')),
                ('whether_to_add_we_chat', models.SmallIntegerField(choices=[(0, '-'), (1, '未添加'), (2, '已添加-未通过'), (3, '已添加-已通过')], default=0, verbose_name='是否添加微信')),
                ('communication_content', models.CharField(blank=True, max_length=512, null=True, verbose_name='沟通内容')),
                ('intention_degree', models.SmallIntegerField(choices=[(0, '-'), (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, '未接通'), (6, '失效电话'), (7, '手机拨打')], default=0, verbose_name='意向度')),
            ],
            options={
                'verbose_name': '转换报表',
                'verbose_name_plural': '转换报表',
                'index_together': {('organizer', 'website_url')},
            },
        ),
    ]
