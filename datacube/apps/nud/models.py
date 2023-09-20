from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Nud_list(models.Model):
    """
    define table based on the dfa review
    """
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Date")
    year = models.CharField(blank=True, null=True, max_length=10,verbose_name='Year')
    nud_id = models.CharField(blank=True, null=True,max_length=10, verbose_name='Nud Id')
    funnel = models.CharField(blank=True, null=True, max_length=50, verbose_name='Funnel')
    source = models.CharField(blank=True, null=True, max_length=10, verbose_name='Source')
    key_focus_area = models.CharField(blank=True, null=True, max_length=100, verbose_name='Key Focus Area')
    risk = models.CharField(blank=True, null=True, max_length=20, verbose_name='Risk')
    nud_level = models.CharField(blank=True, null=True, max_length=20, verbose_name='NUD Level')
    title = models.CharField(blank=True, null=True, max_length=200, default='no info', verbose_name='Title')
    objective = models.TextField(blank=True, null=True, verbose_name='Objective')
    weekly_status = models.TextField(blank=True, null=True, verbose_name='Weekly Status')
    assessment_status = models.CharField(blank=True, null=True, max_length=200, verbose_name='Assessment Status')
    risk_level = models.CharField(blank=True, null=True, max_length=100, verbose_name='Risk Level')
    nud_owner = models.CharField(blank=True, null=True, max_length=50, verbose_name='Owner')
    funnel_owner = models.CharField(blank=True, null=True, max_length=50, verbose_name='Funnel Owner')
    state = models.CharField(blank=True, null=True, max_length=50, verbose_name='State')
    product_category = models.CharField(blank=True, null=True, max_length=30, default='Notebook Only', verbose_name='Product Category')
    leading_product = models.CharField(blank=True, null=True, max_length=50, verbose_name='Leading Product')
    rtp_date = models.DateField(blank=True, null=True, verbose_name='RTP Date')
    target_products = models.TextField(blank=True, null=True, verbose_name='Target Products')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Nud list"
        verbose_name_plural = verbose_name
        db_table = "datacube_nud_list"  # 指定数据表名称