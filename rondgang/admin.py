from django.contrib import admin

# Register your models here.
from .models import Status, Segment

@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ('gemeente', 'straat',)
    search_fields = ['straat',]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    autocomplete_fields = ['segment']
