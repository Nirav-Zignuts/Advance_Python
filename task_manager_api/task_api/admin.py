from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class taskAdmin(admin.ModelAdmin):
    list_display = ['title','description','user','created']