"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from blog import views
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('equipments/', views.equipments,name='equipments'),
    path('eq_stat/', views.eq,name='eq'),
    path('equipments1/', views.eq1,name='equipments_op'),
    path('equipments2/', views.eq2,name='equipments_un'),
    path('equipments3/', views.eq3,name='equipments_id'),
    path('parameters/', views.parameters,name='parameters'),
    path('var_list/', views.vars,name='vars')
]