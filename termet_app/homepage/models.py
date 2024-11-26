from django.db import models

class BaseModel(models.Model):
    """
    Абстрактная модель.
    Добавляет к модели дату создания и последнего изменения.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        abstract = True

from django.db import models


class Container(BaseModel):
    volume = models.IntegerField('Объем контейнера', help_text='Количество сообщений в контейнере')

    def __str__(self):
        return f"Контейнер {self.id}"


class Message(BaseModel):
    text = models.CharField(
        'Сообщение',
        max_length=10,
        unique=True,
        help_text='Сообщение до 10 символов'
    )
    container = models.ForeignKey(
        Container,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    def __str__(self):
        return self.text