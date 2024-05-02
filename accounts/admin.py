from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Corrected 'form' to 'from'
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()  # Corrected 'last_filter' to 'list_filter' if you meant to use the list_filter attribute
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
