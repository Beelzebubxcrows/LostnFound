from django.contrib import admin
from lost.models import Lost
from lost.models import Found
admin.site.register(Lost)
admin.site.register(Found)