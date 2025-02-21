from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_submission_view, name='create_submission'),
    path('update-status/<int:submission_id>/', views.update_status, name='update_status'),
]

