from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TableSerializer
from .serializers import PhotoSerializer
from .serializers import ContentSerializer

from .models import Table
from .models import Photo
from .models import Content

# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('name')
    serializer_class = TableSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('ts_created')
    serializer_class = PhotoSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('id_table')
    serializer_class = ContentSerializer