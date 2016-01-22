from django_tables2 import tables
from dashboard.models import TeamStats, TeamStatsDf, ProcessedTeamStatsDf

__author__ = 'Greg'


class TeamStatsTable(tables.Table):
    class Meta:
        model = TeamStatsDf
        template = 'django_tables2/bootstrap.html'