from rest_framework import serializers

from ..models import Company, Contact, Communication


class PartnerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отладки модели Partner
    """
    class Meta:
        model = Company
        fields = ('id', 'inn', 'test_field',)


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отладки модели Contact
    """
    class Meta:
        model = Contact
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отладки модели Communication
    """
    class Meta:
        model = Communication
        fields = '__all__'
