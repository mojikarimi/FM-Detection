from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def video_page(request):
    return render(request, 'main/video.html')


def image_page(request):
    return render(request, 'main/image.html')


def webcam_page(request):
    return render(request, 'main/camera.html')
