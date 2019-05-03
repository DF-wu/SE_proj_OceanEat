from django.shortcuts import render

# Create your views here.

from OceanEatAPIs.models import Member
from OceanEatAPIs.serializers import MemberSerializer

from rest_framework import viewsets

# auth api
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
#     permission setting
    permission_classes = (IsAuthenticated,)
