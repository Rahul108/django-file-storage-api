import os
import mimetypes, magic
from django.core.files.storage import default_storage
from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from store_media.models import MediaStoreInfo
from store_media.serializers import MediaStorageSerailizer

class MediaStoreViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = MediaStoreInfo.objects.all()
    serializer_class = MediaStorageSerailizer

    def create(self, request):
        data = request.data
        folder = request.path.replace("/", "_")
        try:
            os.mkdir(settings.MEDIA_ROOT, folder)
        except:
            pass
    
        file_to_save = data['file']
        
        file_name = default_storage.save(file_to_save.name, file_to_save)
        print(file_name)
        file_url = default_storage.url(file_name)
        file_abs_path = settings.MEDIA_ROOT + file_name

        validate_file = magic.from_file(file_abs_path, mime=True)
        print(validate_file)

        default_storage.delete(file_name)
        # result = settings.BASE_URL+file_url
        # new_storage = MediaStoreInfo

        return Response(data='ok',status=status.HTTP_201_CREATED)
