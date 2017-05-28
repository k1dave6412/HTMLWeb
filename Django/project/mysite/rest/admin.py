from django.contrib import admin
from .models import Restaurant, Menu


# class MenuInline(admin.TabularInline):
#     model = Menu
#     extra = 2

# class RestaurantAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['name']}),
#         ('Price', {'fields': ['price'], 'classes': ['collapse']}),
#     ]
#     inlines = [MenuInline]
#     list_display = ('name', 'price')
#     list_filter = ['price']
#     search_fields = ['name']


admin.site.register(Restaurant)
admin.site.register(Menu)
