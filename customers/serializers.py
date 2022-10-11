from rest_framework import serializers
from .models import Customers

class CustmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'image', 'name', 'text', 'socialMedia', 'date_created']
