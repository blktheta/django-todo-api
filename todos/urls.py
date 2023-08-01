from django.urls import path

from .views import ListTodo, DetailTodo


app_name = "todos"
urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
    path("", ListTodo.as_view(), name="todo_list"),
]
