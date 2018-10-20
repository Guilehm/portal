from django.contrib import admin

from transactions.models import Event, Request, ServiceOrder


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('code', 'machine', 'category', 'subject')
    list_filter = ('machine', 'category', 'date_added', 'date_changed')
    readonly_fields = ('company',)


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'event', 'category', 'machine', 'priority')
    list_filter = ('category', 'priority')
    search_fields = ('event', 'category', 'subject', 'description')
    readonly_fields = ('company',)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('code', 'category', 'machine', 'date')
    list_filter = ('category', 'date')
    search_fields = ('subject', 'machine', 'category')
