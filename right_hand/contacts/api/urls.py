from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PartnerViewSet, ContactViewSet, CommunicationViewSet

app_name = 'api'

router = SimpleRouter()
router.register('partners', PartnerViewSet, basename='partners')
router.register('contacts', ContactViewSet, basename='contacts')
router.register(
    'communications',
    CommunicationViewSet,
    basename='communications'
)

urlpatterns = [
    path('', include(router.urls)),
]
