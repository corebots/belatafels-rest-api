from rest_framework import serializers

from .models import Table
from .models import Photo
from .models import Content

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ('name', 'type_wood', 'type_epox', 'color_epox', 'note', 'ts_created', 'table_id')

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id_table', 'path', 'filename', 'description', 'title', 'ts_created', 'photo_id')

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ('content_id', 'id_table', 'page', 'title', 'subtitle', 'body', 'ts_created')