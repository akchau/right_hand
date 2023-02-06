from rest_framework import serializers

from ..models import Company


class PartnerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отладки модели Partner
    """
    class Meta:
        model = Company
        fields = ('id', 'inn', 'test_field',)
