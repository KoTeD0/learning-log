"""Определяет схемы URL для learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Изменение публичности топика
    path('change_public/<int:topic_id>', views.change_public, name='change_public'),
    # Удаление записи из топика
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Удаление темы
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]
