from rest_framework import serializers
from OrderController.models import OrderController

class OrderControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderController
        fields = '__all__'