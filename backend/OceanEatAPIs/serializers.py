from rest_framework import serializers
from OceanEatAPIs.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')