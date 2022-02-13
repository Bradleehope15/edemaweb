from django.urls import path
from services.views import *

from . import views

urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
]