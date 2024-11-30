from django.db import models
from django.core.validators import MaxValueValidator

class Container(models.Model):
    capacity = models.PositiveIntegerField(validators=[MaxValueValidator(1000000)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Container {self.id} (Capacity: {self.capacity})"

class Message(models.Model):
    text = models.CharField(max_length=10, unique=True)
    container = models.ForeignKey(Container,
                                  on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.text}"