from django.urls import re_path
from main.views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^image_detection$', image_page, name='image_page'),
    re_path(r'^video_detection$', video_page, name='video_page'),
    re_path(r'^webcam_detection$', webcam_page, name='webcam_page'),
]
