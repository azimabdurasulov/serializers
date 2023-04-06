from django.urls import path
from .views import TodoView

urlpatterns = [
    path('todos', TodoView.as_view()),
    path('todos/<str:tr>', TodoView.as_view())
]