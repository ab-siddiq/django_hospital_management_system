from django.contrib import admin
from .models import UserDetails,UserHospitalManagement
# Register your models here.
class UserHospitalManagementAdmin(admin.ModelAdmin):
    list_display = ('username','account_type','employee_id','date_of_birth','gender')
admin.site.register(UserHospitalManagement,UserHospitalManagementAdmin)
admin.site.register(UserDetails)