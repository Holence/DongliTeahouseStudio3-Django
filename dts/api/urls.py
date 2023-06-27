from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from texts.views import TextViewSet
from concepts.views import ConceptViewSet
from attachments.views import AttachmentViewSet

router = routers.DefaultRouter()
router.register('texts', TextViewSet, basename="text")
router.register('concepts', ConceptViewSet, basename="concept")
router.register('attachments', AttachmentViewSet, basename="attachment")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls'))
]
