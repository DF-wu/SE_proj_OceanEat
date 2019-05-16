from django.shortcuts import render
from SearchIndex.models import SearchIndex
from SearchIndex.serializers import SearchIndexSerializer
from rest_framework.decorators import list_route
from rest_framework import viewsets, status
from rest_framework.response import Response
from SearchIndex import search_index
import os

class SearchIndexViewSet(viewsets.ModelViewSet):
    queryset = SearchIndex.objects.all()
    serializer_class = SearchIndexSerializer
    # /api/SearchIndex/query/?query=query_term
    @list_route(methods=['get'])
    def query(self, request):
        query_term = request.query_params.get('query', None)
        return Response(search_index.SearchIndex().query(query_term), status=status.HTTP_200_OK)
        