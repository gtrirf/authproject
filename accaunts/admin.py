from django.contrib import admin
from .models import CostumerUsers


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'last_name', 'first_name')


admin.site.register(CostumerUsers, CustomUserAdmin)
