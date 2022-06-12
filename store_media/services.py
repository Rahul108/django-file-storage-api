from django.core.files.storage import default_storage
from django.conf import settings

class MediaFileSaveService:
    def __init__(self, validated_data):
        self.validated_data = validated_data

    def save_media_files(self):
        res = []
        
        for file in self.validated_data['file']:
            print(file)
            file_name = default_storage.save(file.name, file)
            file_url = default_storage.url(file_name)
            result = settings.BASE_URL+file_url
            res.append(result)
        return res