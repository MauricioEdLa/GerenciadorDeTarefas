from django.db import models
from django.contrib.auth.models import User

# Modelo para representar uma tarefa
class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Alta'),
        (2, 'Média'),
        (3, 'Baixa'),
    ]

    # Título da tarefa
    title = models.CharField(max_length=255)

    # Descrição da tarefa
    description = models.TextField(blank=True)

    # Data de conclusão da tarefa
    due_date = models.DateField()

    # Prioridade da tarefa
    priority = models.IntegerField(choices=PRIORITY_CHOICES)

    # Status de conclusão da tarefa (padrão: não concluída)
    completed = models.BooleanField(default=False)

    # Usuário associado à tarefa
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Ordenação padrão por data de conclusão
    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title