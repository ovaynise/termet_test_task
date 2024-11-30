from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

class Container(models.Model):
    capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message='Capacity должно быть больше или равно 1'),
            MaxValueValidator(1000000, message='Capacity не должно превышать 1000000')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not isinstance(self.capacity, int):
            raise ValidationError('Capacity должно быть целым числом.')

    def __str__(self):
        return f"Container {self.id} (Capacity: {self.capacity})"

class Message(models.Model):
    text = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9!@#$%^&*()\-_+=\[\]{};:,.<>?/|\\~`]+$',
                message='Text может содержать только буквы, цифры или разрешённые символы.'
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
        if not (1 <= len(self.text) <= 10):
            raise ValidationError('Text должно быть от 1 до 10 символов.')
        if not self.text:
            raise ValidationError('Text не может быть пустым.')

    def __str__(self):
        return f"Message: {self.text}"
