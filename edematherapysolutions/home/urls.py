from django.urls import path
from home.views import Home

from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
]