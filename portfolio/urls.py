from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/', views.blog),
    # blog single
    # portfolio single
]