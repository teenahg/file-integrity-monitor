from django.contrib import admin
from .models import File
# from .models import User

# admin.site.register(User)
# admin.site.register(Profile)
# admin.site.register(Department)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'hash_value', 'slug')
    list_filter = ('created', 'publish', 'location')
    search_fields = ('name', 'hash_value')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)