from django.contrib import admin
from .models import ab



# Shop by Category Admin (ab model)
@admin.register(ab)
class abAdmin(admin.ModelAdmin):
    list_display = ('image',)