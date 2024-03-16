from django.urls import path
from . import views

urlpatterns = [
    path('pupil', views.pupil, name='pupil')
]