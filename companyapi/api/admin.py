from django.contrib import admin
from  api.models import Company,Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company','position')
# Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)