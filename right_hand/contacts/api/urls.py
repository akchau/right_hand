from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PartnerViewSet

app_name = 'api'

router = SimpleRouter()
router.register('partners', PartnerViewSet, basename='partners')

urlpatterns = [
    path('', include(router.urls)),
]
