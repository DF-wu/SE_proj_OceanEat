from django.shortcuts import render
from OrderController.models import OrderController
from OrderController.serializers import OrderControllerSerializer

from rest_framework import viewsets

class OrderControllerViewSet(viewsets.ModelViewSet):
    queryset = OrderController.objects.all()
    serializer_class = OrderControllerSerializer