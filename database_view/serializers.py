from rest_framework import serializers

from .models import Company


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'date_created']