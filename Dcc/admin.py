from django.contrib import admin

# Register your models here.

from . import models

# admin.site.register(models.apicase)
# admin.site.site_title = '抖查查'
# admin.site.site_header = '抖查查后台'

admin.site.register(models.apilist)
admin.site.register(models.reportlist)
admin.site.register(models.apiliston)
admin.site.site_title = '抖查查'
admin.site.site_header = '抖查查后台'