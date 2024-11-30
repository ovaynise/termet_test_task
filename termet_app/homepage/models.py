from django.db import models

class Container(models.Model):
    capacity = models.PositiveIntegerField()
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