from django.contrib import admin

from .models import Task,Variant
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    

    list_display = "pk", "name", "description", "answer"
    list_display_links = "pk", "name"
class TaskInline(admin.TabularInline):
    model = Variant.tasks.through

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline
    ]
    list_display = "pk", "number", "theme", "created_at"
    list_display_links = "pk", "number"



