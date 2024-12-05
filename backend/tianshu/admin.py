from django.contrib import admin
 
# Register your models here.
from . import models
 
admin.site.register(models.Approval)
admin.site.register(models.Account)
admin.site.register(models.Agent)
admin.site.register(models.Employee)
admin.site.register(models.Customer)
admin.site.register(models.Contract)
admin.site.register(models.PlatformAccountRecharge)
