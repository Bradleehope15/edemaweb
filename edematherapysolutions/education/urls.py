from django.urls import path
from education.views import *

from . import views

urlpatterns = [
    path('', EducationView.as_view(), name='education'),
]