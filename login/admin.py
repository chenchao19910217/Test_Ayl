from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.site_title = '抖查查'
admin.site.site_header = '抖查查后台'