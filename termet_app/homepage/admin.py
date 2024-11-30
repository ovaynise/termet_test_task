from django.contrib import admin
from .models import Container, Message
from .forms import MessageAdminForm

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'capacity', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    list_display = ('id', 'text', 'container', 'created_at')
    readonly_fields = ('created_at',)


