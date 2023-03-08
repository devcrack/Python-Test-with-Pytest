from django.contrib import admin
from .models import Company

# WAY #1
# class CompanyAdmin(admin.ModelAdmin):
#     model = Company
#
#
# admin.site.register(Company, CompanyAdmin)


# WAY 2
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
