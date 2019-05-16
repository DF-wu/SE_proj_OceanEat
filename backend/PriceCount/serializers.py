from rest_framework import serializers
from PriceCount.models import PriceCount

class PriceCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = PriceCount
        fields = '__all__'