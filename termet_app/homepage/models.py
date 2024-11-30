from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.core.exceptions import ValidationError
from homepage.config import (MIN_CONTAINER_CAPACITY, MAX_CONTAINER_CAPACITY,
                    MAX_MESSAGE_LEN, MIN_MESSAGE_LEN)

class Container(models.Model):
    capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                MIN_CONTAINER_CAPACITY,
                message=f'Значение должно быть больше '
                        f'или равно {MIN_CONTAINER_CAPACITY}'),
            MaxValueValidator(
                MAX_CONTAINER_CAPACITY,
                message=f'Значение не должно'
                        f' превышать {MAX_CONTAINER_CAPACITY}')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not isinstance(self.capacity, int):
            raise ValidationError('Значение должно быть целым числом.')

    def __str__(self):
        return f"Container {self.id} (Capacity: {self.capacity})"

class Message(models.Model):
    text = models.CharField(
        max_length=MAX_MESSAGE_LEN,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9!@#$%^&*()\-_+=\[\]{};:,.<>?/|\\~`]+$',
                message='Text может содержать только буквы, цифры или'
                        ' разрешённые символы.'
            ),
        ]
    )
    container = models.ForeignKey(
        Container,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (MIN_MESSAGE_LEN <= len(self.text) <= MAX_MESSAGE_LEN):
            raise ValidationError(
                f'Text должно быть от {MIN_MESSAGE_LEN} до {MAX_MESSAGE_LEN} '
                f'символов.')
        if not self.text:
            raise ValidationError('Text не может быть пустым.')

    def __str__(self):
        return f"Message: {self.text}"
