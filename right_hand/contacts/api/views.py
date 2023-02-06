from rest_framework import viewsets

from .serializers import PartnerSerializer

from ..models import Company


class PartnerViewSet(viewsets.ModelViewSet):
    """Вьюсет для отладки и тестирования модели Partner"""
    queryset = Company.objects.all()
    serializer_class = PartnerSerializer
