from django.contrib import admin

from work.models import Employee, Role

# Register your models here.

admin.site.register(Role)
admin.site.register(Employee)
