import django_filters
from dashboard.models import TeamStats

__author__ = 'Greg'


class TeamStatsFilter(django_filters.FilterSet):
    class Meta:
        model = TeamStats
        fields = ['color', 'kills']