from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_message/<int:container_id>/',
         views.add_message, name='add_message'),
    path('search_message/', views.global_search_message,
         name='global_search_message'),
    path('output_data/', views.output_all_data,
         name='output_all_data'),

]