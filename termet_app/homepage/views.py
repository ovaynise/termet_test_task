from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.db.models import Count, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Container, Message

MAX_CAPACITY = 1000000

def reset_container_id():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence "
                       "WHERE name='homepage_container'")


def index(request):
    if request.method == 'POST':
        if 'delete_all' in request.POST:
            Container.objects.all().delete()
            reset_container_id()
            return redirect('homepage:index')

        capacity = request.POST.get('capacity', '').strip()
        if not capacity.isdigit() or int(capacity) > MAX_CAPACITY:
            return render(request, 'homepage/index.html', {
                'containers_exist': False,
                'error': f'Введите корректное целое число от 1 до {MAX_CAPACITY}.',
            })

        capacity = int(capacity)
        if capacity > 0:
            container = Container.objects.create(capacity=capacity)
            return redirect('homepage:add_message', container_id=container.id)

    all_containers = Container.objects.all()
    containers_exist = all_containers.exists()

    return render(request, 'homepage/index.html', {
        'containers_exist': containers_exist,
        'containers': all_containers,
        'total_containers': all_containers.count(),
        'total_messages': Message.objects.count(),
        'container_capacity': all_containers.first().capacity if containers_exist else None,
        'next_container': Container.objects.annotate(
            filled_count=Count('messages')
        ).filter(filled_count__lt=F('capacity')).first(),
    })

def add_message(request, container_id):
    container = get_object_or_404(Container, id=container_id)
    total_containers = Container.objects.count()
    total_messages = Message.objects.count()
    container_capacity = container.capacity

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if not text or len(text) > 10 or not all(
                char.isalnum() or char in "!@#$%^&*()-_=+[]{};:,.<>?/|\\~`" for char in text):
            return render(request, 'homepage/add_message.html', {
                'container': container,
                'total_containers': total_containers,
                'total_messages': total_messages,
                'container_capacity': container_capacity,
                'error': 'Ошибка ввода: Сообщение должно быть не более '
                         '10 символов, содержать только буквы, цифры или'
                         ' разрешённые символы.',
            })

        if Message.objects.filter(text=text).exists():
            return render(request, 'homepage/add_message.html', {
                'container': container,
                'total_containers': total_containers,
                'total_messages': total_messages,
                'container_capacity': container_capacity,
                'error': 'Ошибка ввода: Сообщение должно быть уникальным'
                         ' во всей базе данных.',
            })

        container.messages.create(text=text)
        if container.messages.count() >= container.capacity:
            next_container = Container.objects.annotate(
                filled_count=Count('messages')
            ).filter(filled_count__lt=F('capacity')).first()

            if not next_container:
                next_container = Container.objects.create(
                    capacity=container.capacity)

            return redirect('homepage:add_message',
                            container_id=next_container.id)

        return redirect('homepage:add_message',
                        container_id=container.id)

    return render(request, 'homepage/add_message.html', {
        'container': container,
        'total_containers': total_containers,
        'total_messages': total_messages,
        'container_capacity': container_capacity,
    })

def global_search_message(request):
    query = request.GET.get('text', '').strip()
    results = []

    if query:
        results = Message.objects.filter(text__icontains=query).select_related('container')

    return render(request, 'homepage/global_search_message.html', {
        'results': results,
        'query': query,
    })

def output_all_data(request):
    messages = Message.objects.select_related('container').all()
    paginator = Paginator(messages, 10)
    page = request.GET.get('page')
    try:
        paginated_messages = paginator.page(page)
    except PageNotAnInteger:
        paginated_messages = paginator.page(1)
    except EmptyPage:
        paginated_messages = paginator.page(paginator.num_pages)

    return render(request, 'homepage/output_all_data.html', {
        'paginated_messages': paginated_messages,
    })
