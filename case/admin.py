from django.contrib import admin
from case.models import case,Task,Document,Report
# Register your models here.

admin.site.register(case)
admin.site.register(Report)
admin.site.register(Task)
admin.site.register(Document)
