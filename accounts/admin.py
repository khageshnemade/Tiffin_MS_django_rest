from django.contrib import admin
from .models import User

class UserDisplay(admin.ModelAdmin):
    # Customize list display
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined')
    # Add filters for easy navigation
    list_filter = ('role', 'is_active', 'is_staff')
    # Enable search functionality
    search_fields = ('email', 'first_name', 'last_name')

# Register your models here
admin.site.register(User, UserDisplay)