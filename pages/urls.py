from django.urls import path, include
from .views import *

urlpatterns = [
    path('pages/home/', HomePageView.as_view(), name='home'),
]