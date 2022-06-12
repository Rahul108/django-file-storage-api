from rest_framework import serializers
from store_media.models import MediaStoreInfo
import mimetypes, magic

class MediaStorageSerailizer(serializers.Serializer):
    file = serializers.ListField()
    
    def validate_file(self, file):
        res = []
        for elm in file:
            if elm:
                temp_path = elm.temporary_file_path()
                validate_file = magic.from_file(temp_path, mime=True)
                get_file_mimetype = mimetypes.guess_type(elm.name)
                if validate_file == get_file_mimetype[0]:
                    res.append(elm)
                else:
                    serializers.ValidationError(f'Invalid/Corrupted-File for {elm.name}')
        
        return res