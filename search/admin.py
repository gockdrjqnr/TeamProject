from django.contrib import admin
from search.models import Keywords, Theme, Chart

# Register your models here.

admin.site.register(Keywords)
admin.site.register(Theme)
admin.site.register(Chart)