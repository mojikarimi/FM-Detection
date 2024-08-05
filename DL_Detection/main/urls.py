from django.urls import re_path
from main.views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
]
