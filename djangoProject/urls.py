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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from polls import views
from polls.views import TaskUpdate, TaskList, TaskCreate, WelcomeView, CategoryCreate, CategoryList, CategoryUpdate, \
    CategoryDelete, TaskViewSet, TaskViewByUser
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'taskByUser', TaskViewByUser)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('index.html', views.index),
    path('create_task/', TaskCreate.as_view(), name='create_task'),
    path('list_task/', TaskList.as_view()),
    path('updateTask/<int:pk>', TaskUpdate.as_view()),
    path('welcome/', WelcomeView.as_view()),


    path('create_category/', CategoryCreate.as_view(), name='create_category'),
    path('list_category/', CategoryList.as_view(),name='CategoryList'),
    path('update_category/<int:pk>', CategoryUpdate.as_view(),name='update_category'),
    path('delete_category/<int:pk>', CategoryDelete.as_view(),name='delete_category'),

    path('register', views.register, name= 'register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


    # la primera parte que es como se va a llamar la url,
                        #y despues , el metodo o la clase que vos queres que haga referencia
]

urlpatterns += staticfiles_urlpatterns()