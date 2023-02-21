from django.urls import path
from apps.healthcheck import views

urlpatterns = [
    path('', views.healthcheck, name='healthcheck'),
]
