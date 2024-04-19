from django.contrib import admin
from .models import Topic, Receipt


admin.site.register(Receipt)
admin.site.register(Topic)