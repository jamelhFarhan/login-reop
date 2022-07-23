from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #  path('', views.user_list, name='index'),
]
