from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'), # Listar tarefas
    path('new/', TaskCreateView.as_view(), name='task_create'), # Criar nova tarefa
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_update'), # Editar tarefa
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'), # Excluir tarefa
]