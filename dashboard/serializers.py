from dashboard.models import DataSource
from rest_framework import serializers


__author__ = 'Greg'

class DataSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSource
        fields = ('name', 'external_location')
