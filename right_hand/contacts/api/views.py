from rest_framework import viewsets

from .serializers import (
    PartnerSerializer,
    ContactSerializer,
    CommunicationSerializer
)

from ..models import Company, Contact, Communication


class PartnerViewSet(viewsets.ModelViewSet):
    """Вьюсет для отладки и тестирования модели Partner"""
    queryset = Company.objects.all()
    serializer_class = PartnerSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Вьюсет для отладки и тестирования модели Partner"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CommunicationViewSet(viewsets.ModelViewSet):
    """Вьюсет для отладки и тестирования модели Partner"""
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
