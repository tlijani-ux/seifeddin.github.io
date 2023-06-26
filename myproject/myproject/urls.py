"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from todo.views import  index,complete_task,delete_all,delete_completed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('complete/<int:task_id>',complete_task,name='complete'),
    path('delete_completed/',delete_completed,name='delete_completed'),
    path('delete_all/',delete_all,name='delete_all'),
   # path('about/',about,name='about'),
    #path('delete/<int:task_id>',Delete_task,name='delete')
]
