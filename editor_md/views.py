from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from .utils import editor_settings


@csrf_exempt
def upload_image(request):
    """
    upload images, handle and save image.
    """
    if request.method == "POST":
        guid = request.GET.get('guid')
        path = request.GET.get("path")
        files = request.FILES['editormd-image-file']
        # todo: get image_formats form conf.setting if it have.else from editor_settings["imageFormats"]
        image_formats = editor_settings["imageFormats"]
        file_name = files.name  # image name
        # file_size = files.size  # image size
        upload_original_name, upload_original_ext = os.path.splitext(file_name)
        last_image_name = "_".join([upload_original_name, guid]) + upload_original_ext
        if upload_original_ext[1:] in image_formats:
            # judge image path is exist;
            media_root = getattr(settings, "MEDIA_ROOT")
            image_save_file = os.path.join(media_root, path)
            image_save_path = os.path.join(image_save_file, last_image_name)
            media_url = getattr(settings, "MEDIA_URL")
            image_url = os.path.join(media_url, path, last_image_name)
            if not os.path.exists(image_save_file):
                os.makedirs(image_save_file)
            with open(image_save_path, 'wb+') as f:
                for chunk in files.chunks():
                    f.write(chunk)
            return JsonResponse(dict(message="File upload success!",
                                     success=1,
                                     url=image_url))
        else:
            return JsonResponse(dict(message="File type not allowed",
                                     success=0,
                                     url=""), status=200)

    else:
        return JsonResponse({"message": "The method is not allowed for the requested URL."}, status=405)
