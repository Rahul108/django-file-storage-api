import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from store_media.models import MediaStoreInfo
from store_media.serializers import MediaStorageSerailizer
from store_media.services import MediaFileSaveService

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
    
        serializer = MediaStorageSerailizer(data=data)
        if serializer.is_valid():
            saved_files_url = MediaFileSaveService(serializer.validated_data).save_media_files()
            return Response(data=saved_files_url, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

