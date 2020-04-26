from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_album>', views.read, name='read_album'),
    path('', views.home, name="home"),
    path('research/', views.research, name='research')
]
