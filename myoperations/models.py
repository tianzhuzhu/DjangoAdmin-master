import datetime

import django.contrib.admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelChoiceField


class opetaion_type(models.Model):
    types=models.CharField(max_length=32,null=True)
    def __str__(self):
        return self.types
    def __unicode__(self):
        return self.types
class reason_type(models.Model):
    reason=models.CharField(max_length=32,null=True)
    def __str__(self):
        return self.reason
    def __unicode__(self):
        return self.reason
class Operation(models.Model):
    # 选择操作原因 可行
    # operation_type_choice = (('1', u'增ip'), ('2', u'减ip'))
    # operation_type = models.CharField(u"操作原因", choices=operation_type_choice, max_length=32)

    reason=models.ForeignKey(reason_type,on_delete=models.CASCADE)
    operation_type =models.ForeignKey(opetaion_type,on_delete=models.CASCADE)

    deal_code=models.CharField(max_length=32,default='',verbose_name='业务号码')
    vpn_deal_code=models.CharField(max_length=32,null=True,verbose_name='vpn业务号码')

    operator=models.CharField(max_length=50, blank=True, verbose_name=u"添加者",default='')

    add_ip=models.CharField(max_length=100,default='',verbose_name='新增ip')
    del_ip=models.CharField(max_length=100,default='',verbose_name='回收ip')
    descrption=models.CharField(max_length=50,verbose_name='备注',default='')
    operation_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='操作时间')


    class Meta:
        verbose_name = u'操作日志管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# class Test(models.Model):
#     name = models.CharField(max_length=20)
#
#
# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField(default=0)
#     email = models.EmailField()
#
#     def __unicode__(self):
#         return self.name
#
#
# class Tag(models.Model):
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
#     name = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.name
class person(models.Model):
    sex_type = (('male', u'男'), ('female', u'女'))
    sex = models.CharField(u"性别", choices=sex_type, max_length=32)
