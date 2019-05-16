from rest_framework import serializers
from SearchIndex.models import SearchIndex

class SearchIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchIndex
        fields = '__all__'