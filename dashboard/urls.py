from django.conf.urls import url, include
from rest_framework import routers
from dashboard import views
from dashboard.views import DashboardListFormView

__author__ = 'Greg'

router = routers.DefaultRouter()
router.register(r'datasource', views.DataSourceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^dashboard/$', DashboardListFormView.as_view(), name='dashboard'),
]