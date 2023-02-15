from django.contrib import admin

from portfolio.models import Alternative_Tech, Languages, Portfolio, States

# Register your models here.

admin.site.register(Languages)
admin.site.register(States)
admin.site.register(Portfolio)
admin.site.register(Alternative_Tech)

