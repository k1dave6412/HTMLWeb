from django.contrib import admin

# Register your models here.
from .models import Restaurant,Food

admin.site.register(Food)
admin.site.register(Restaurant)
