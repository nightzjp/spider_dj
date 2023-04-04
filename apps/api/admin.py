from django.contrib import admin
from api import models
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.formats import base_formats


class ReportResources(resources.ModelResource):
    class Meta:
        model = models.DomainReport


@admin.register(models.DomainReport)
class ReportAdmin(ImportExportModelAdmin):
    list_per_page = 10
    list_display = [
        'id', 'organizer', 'website_url', 'review_time', 'registered_capital', 'phone', 'isp', 'ip', 'next_contact_time',
        'relevance', 'whether_to_add_we_chat', 'intention_degree', 'industry', 'communication_content'
    ]
    list_filter = ['isp', 'relevance', 'whether_to_add_we_chat', 'intention_degree', 'reason', 'review_time']
    list_editable = [
        'next_contact_time', 'relevance', 'whether_to_add_we_chat', 'intention_degree', 'industry', 'communication_content'
    ]
    date_hierarchy = 'create_at'
    # search_fields = ['reason']
    resource_class = ReportResources
    formats = [base_formats.XLS, base_formats.XLSX]


admin.site.site_header = '域名转换厂商'
