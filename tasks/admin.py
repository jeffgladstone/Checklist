from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_created', 'is_done')
    search_fields = ('description',)
    list_filter = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
    fields = ('description', 'date_created', 'is_done')
    #raw_id_fields = ('user',)

admin.site.register(Task, TaskAdmin)
