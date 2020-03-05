from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<user_id>', views.show),
    path('process', views.process)
]