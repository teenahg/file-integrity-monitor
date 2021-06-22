from django.contrib import admin
from .models import File
# from .models import User

# admin.site.register(User)
# admin.site.register(Profile)
# admin.site.register(Department)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'hash_value')
    search_fields = ('name', 'hash_value')
    ordering = ('name',)