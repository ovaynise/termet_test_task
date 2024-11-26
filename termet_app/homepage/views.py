from django.shortcuts import render
from django.http import JsonResponse

from .models import Container, Message

def add_message(text):
    # Проверяем длину сообщения
    if len(text) > 10:
        return "Ошибка ввода: сообщение слишком длинное"

    # Проверяем уникальность
    if Message.objects.filter(text=text).exists():
        return "Ошибка ввода: сообщение не уникальное"

    # Найти последний контейнер
    last_container = Container.objects.order_by('id').last()

    # Если контейнеров нет или последний полон, создаём новый
    if not last_container or last_container.messages.count() >= last_container.volume:
        last_container = Container.objects.create(volume=10)  # Здесь "10" заменяется на значение из ввода

    # Добавляем сообщение в контейнер
    Message.objects.create(text=text, container=last_container)
    return "Сообщение успешно добавлено"

def find_message(text):
    try:
        message = Message.objects.get(text=text)
        return f"Сообщение в {message.container}"
    except Message.DoesNotExist:
        return "Сообщения нету"

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'set_volume':
            volume = int(request.POST.get('volume'))
            Container.objects.all().delete()  # Очистить контейнеры
            Container.objects.create(volume=volume)
            return JsonResponse({"message": "Объем контейнера установлен"})

        if action == 'add_message':
            text = request.POST.get('text')
            response = add_message(text)
            return JsonResponse({"message": response})

        if action == 'search_message':
            text = request.POST.get('text')
            response = find_message(text)
            return JsonResponse({"message": response})

    containers = Container.objects.all()
    messages = Message.objects.all()
    return render(request, 'homepage/index.html', {
        'containers': containers,
        'messages': messages,
        'total_messages': messages.count(),
        'total_containers': containers.count(),
    })