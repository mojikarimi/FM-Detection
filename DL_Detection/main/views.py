from django.shortcuts import render
from main.models import Duc

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
