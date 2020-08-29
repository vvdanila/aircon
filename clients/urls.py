from django.urls import path

from . import views


urlpatterns = [
    path('', views.ClientList.as_view(), name='client_list')
]
