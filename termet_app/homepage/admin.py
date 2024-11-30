
from django.contrib import admin


from .models import Container, Message



@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Container._meta.fields]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]
    search_fields = ('text', 'container__id')
    list_filter = ('container',)



