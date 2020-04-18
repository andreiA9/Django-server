from rest_framework import serializers

from .models import Company
from .models import Programmer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'date_created']

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ['id', 'name', 'age', 'company']