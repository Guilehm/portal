from django.contrib import admin

from register.models import Category, Message, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('code', 'full_name', 'doc', 'active')
    search_fields = ('code', 'first_name', 'last_name', 'home_phone_number', 'cell_phone_number')
    list_filter = ('active', 'date_added', 'date_changed')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'active')
    search_fields = ('description',)
    list_filter = ('active', 'date_added', 'date_changed')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')
    search_fields = ('title', 'description')
    list_filter = ('date_added', 'date_changed')
