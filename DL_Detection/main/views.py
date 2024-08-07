from django.shortcuts import render, redirect
from main.models import Duc, FilesPredicts
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import cv2
import numpy as np
from django.db.models import Q
from django.http import StreamingHttpResponse

# Create your views here.
def index(request):
    ducs=Duc.objects.all()
    context={
        'ducs':ducs,
    }
    return render(request, 'main/index.html',context=context)


def video_page(request):
    return render(request, 'main/video.html')


def image_page(request):
    return render(request, 'main/image.html')


def webcam_page(request):
    return render(request, 'main/camera.html')
