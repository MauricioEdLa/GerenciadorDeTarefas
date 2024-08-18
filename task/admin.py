from django.contrib import admin
from .models import Task

# Registro do modelo Task no admin do Django
admin.site.register(Task)