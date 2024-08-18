from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')), # Inclua as URLs do app task
    path('accounts/', include('django.contrib.auth.urls')), #URLs para login/logout
]
