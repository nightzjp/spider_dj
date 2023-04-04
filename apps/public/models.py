from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    """自定义Model基类"""
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    delete_at = models.DateTimeField(null=True, blank=True, default=None, verbose_name='删除时间')
    create_by = models.CharField(max_length=32, default='', verbose_name='创建人')

    detail = models.CharField(max_length=200, default='', verbose_name='备注信息')

    class Meta:
        abstract = True
        ordering = ['id']

    def set_delete(self):
        """软删除"""
        self.delete_at = datetime.now()
        self.save()
