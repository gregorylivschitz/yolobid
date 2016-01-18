from dashboard.models import DataSource
from rest_framework import viewsets
from dashboard.serializers import DataSourceSerializer

# Create your views here.

class DataSourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DataSources to be viewed or edited.
    """
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer
