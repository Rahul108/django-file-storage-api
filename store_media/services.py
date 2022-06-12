import mimetypes
import time
from django.core.files.storage import default_storage
from django.conf import settings
class MediaFileSaveService:
    def __init__(self, validated_data):
        self.validated_data = validated_data

    def save_media_files(self):
        res = []
        
        for file in self.validated_data['file']:
            file_type = mimetypes.guess_type(file.name)
            extension = mimetypes.guess_extension(file_type[0])
            new_file_name = str(format(time.time() * 1000000000, ".0f")) + extension
            file_name = default_storage.save(new_file_name, file)
            file_url = default_storage.url(file_name)
            result = settings.BASE_URL+file_url
            res.append(result)
        return res