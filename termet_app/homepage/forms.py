from django import forms
from .models import Container
from django.core.exceptions import ValidationError
from .models import Message

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['capacity']

class MessageAdminForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        container = cleaned_data.get('container')
        if container and container.messages.count() >= container.capacity:
            raise ValidationError(f'Контейнер {container.id} уже заполнен.')
        return cleaned_data