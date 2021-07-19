from __future__ import unicode_literals
from django.contrib import admin
from django.forms import forms, ModelForm
from django.http import HttpResponse

from .models import *

# Register your models here.
from openpyxl import Workbook

class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            row = ws.append(data)

        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'

# class userProfileForm(ModelForm):
#     option = ModelChoiceField(label=u'下拉框',queryset=opetaion_type.objects.all())



@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin,ExportExcelMixin):
    #
    # form=userProfileForm
    list_display=('reason', 'operation_type', 'deal_code', 'vpn_deal_code','operator','add_ip','del_ip','operation_time')
    fileds=('reason', 'operation_type', 'deal_code', 'vpn_deal_code','operator','add_ip','del_ip','operation_time')

    ordering = ('-operation_time',)
    search_fields = ('name','operator')
    # list_editable = ['deal_code','from_ips','to_ips',]
    readonly_fields = ['id','operation_time','operator']
    list_per_page=30
    def save_model(self, request, obj, form, change):
        obj.operator = request.user
        obj.save()
    actions = ['export_as_excel']
    verbose_name=u'操作日志'
admin.site.site_title = "操作记录日志"
admin.site.site_header = "操作记录日志"

    # name=models.CharField(max_length=50,verbose_name='操作名称')
    #
    # operator=models.CharField(max_length=100,verbose_name='操作人')
    # deal_code=models.CharField(default='',verbose_name='业务号')
    # from_ips=models.CharField(default='',verbose_name='原始ip')
    # to_ips=models.CharField(default='',verbose_name='结果ip')
    #
    # operation_time=models.DateTimeField(default=datetime.datetime.now,verbose_name='操作时间')
# admin.site.register(Operation,OperationAdmin)
# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import person
'''
class ngo_base_info_admin(admin.ModelAdmin):
    list_display = ('name', 'abstrat', 'tech_person')#显示的信息
    search_fields = ('name',)#查找
    list_filter = ('name',)#过滤器

admin.site.register(ngo_base_info, ngo_base_info_admin)#注册
'''
# Register your models here.
admin.site.register(person)