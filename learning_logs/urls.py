from django.urls import path
from . import views 

app_name = 'learning_logs'

urlpatterns = [
    #Главная страница
    path('', views.index, name='index'),

    #Страница со списком всех тем
    path('topics/', views.topics, name='topics'),

    #Cтраница по отдельной теме(topic)
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Стараница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),

    #Стараница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    #Стараница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]