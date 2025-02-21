from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_submissions, name='get_submissions'),

]

