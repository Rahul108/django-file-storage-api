from rest_framework import serializers
from store_media.models import MediaStoreInfo

class MediaStorageSerailizer(serializers.Serializer):
    def validate(self, data):
        return data