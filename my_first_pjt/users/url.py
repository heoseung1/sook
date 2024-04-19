from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('<username>/', views.profile),
]
