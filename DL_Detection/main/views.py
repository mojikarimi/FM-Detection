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
    files = FilesPredicts.objects.filter(original_file__endswith='.mp4')
    context = {'files': files}
    if request.method == 'POST':
        video = request.FILES.get('video')
        if video:
            model = settings.MODEL
            fs = FileSystemStorage(location=f'{settings.MEDIA_URL[1:]}video_originals/')
            filename = fs.save(video.name, video)
            # create object
            file = FilesPredicts()
            file.original_file = video.name
            file.original_file_url = fs.url(f'video_originals/{filename}')
            path_video = f'{settings.MEDIA_ROOT}\\video_originals\\{filename}'
            vid = cv2.VideoCapture(path_video)
            frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(vid.get(cv2.CAP_PROP_FPS))
            # initialize the FourCC and a video writer object
            fourcc = cv2.VideoWriter_fourcc(*'mp4t')
            output = cv2.VideoWriter(f'media/video_predicts/pred_{filename}', fourcc, fps,
                                     (frame_width, frame_height))
            while True:
                success, img = vid.read()
                if not success:
                    break
                face_cascade = settings.FACE_MODEL
                faces = face_cascade.detectMultiScale(img, 1.2, 5)
                if np.any(faces):
                    for (x, y, w, h) in faces:
                        my_img = cv2.resize(img[y:y + h, x:x + w], (125, 125))
                        y_pred = model.predict(my_img.reshape(1, 125, 125, 3))
                        if y_pred[0, 0] == 1:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
                        else:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
                else:
                    pass

                output.write(img)
                if vid.get(cv2.CAP_PROP_POS_FRAMES) == vid.get(cv2.CAP_PROP_FRAME_COUNT):
                    file.Prediction_file = f'pred_{filename}'
                    file.Prediction_file_url = f'/media/video_predicts/pred_{filename}'
                    break
            vid.release()
            cv2.destroyAllWindows()
        file.save()
        return redirect('video_page')
    return render(request, 'main/video.html', context=context)


def image_page(request):
    return render(request, 'main/image.html')


def webcam_page(request):
    return render(request, 'main/camera.html')
