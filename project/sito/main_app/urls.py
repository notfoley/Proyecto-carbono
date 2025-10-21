from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.miap, name='miap'),
    path('miap/', views.miap, name='miap')
]