"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from polls.views import TaskUpdate, TaskList, TaskCreate
from user.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_task/', TaskCreate.as_view()),
    path('login/', my_view),
    path('list_task/', TaskList.as_view()),
    path('updateTask/<int:pk>', TaskUpdate.as_view()),






    # la primera parte que es como se va a llamar la url,
                        #y despues , el metodo o la clase que vos queres que haga referencia
]
