"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# Toda URL precisa tambem no mínimo de uma view.py
# Toda função view.py recebe um um argumento "request" pois todo url recebe requisições ou faz, por exemplo um url no navegador faz um 'get'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]
