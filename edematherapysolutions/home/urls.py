from django.urls import path
from home.views import *

from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]