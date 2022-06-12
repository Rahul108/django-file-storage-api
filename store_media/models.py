from django.db import models
import pghistory

@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class MediaStoreInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=300)

    class Meta:
        db_table = "media_store_info"