
from django.contrib import admin


from .models import Container, Message



class ContainerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'volume',
        'created_at',
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'container',
    )
    search_fields = ('container',)
    list_filter = ('container',)



admin.site.register(Container, ContainerAdmin)
admin.site.register(Message, MessageAdmin)
