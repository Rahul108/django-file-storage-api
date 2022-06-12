from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from store_media.views import MediaStoreViewSet

router = DefaultRouter()
router.register('file', MediaStoreViewSet)

urlpatterns = []
urlpatterns += router.urls
