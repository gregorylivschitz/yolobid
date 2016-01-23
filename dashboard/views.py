import logging
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, ListView, View
from django_filters.views import FilterView
from django_tables2 import SingleTableView, RequestConfig
from dashboard.filters import TeamStatsFilter
from dashboard.forms import DashboardForm
from dashboard.models import DataSource, TeamStats, ProcessedTeamStatsDf, TeamStatsDf
from rest_framework import viewsets
from dashboard.serializers import DataSourceSerializer
from dashboard.tables import TeamStatsTable


class DataSourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DataSources to be viewed or edited.
    """
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


# This is a bit confusing, we are using 3 class based views to accomplish a form and a list on the same page
# This form view will handle the post
class DashboardView(FormView):
    template_name = "dashboard.html"
    form_class = DashboardForm
    success_url = "/dashboard/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        data = form.cleaned_data
        return super(DashboardView, self).form_valid(form)


# This view will handle the get, but we need to tell it to get the form and display it as well.
class DashboardListView(ListView):
    model = TeamStats
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['form'] = DashboardForm()
        return context


# This view says to use the get for the DashboardListView and the post for the DashboardView
class DashboardListFormView(View):

    def get(self, request, *args, **kwargs):
        view = DashBoardTableView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = DashboardView.as_view()
        return view(request, *args, **kwargs)


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(PagedFilteredTableView, self).get_table()
        RequestConfig(self.request, paginate={'page': self.kwargs['page'],
                            "per_page": self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class FilterTableView(FilterView, SingleTableView):
    # Django tables 2 needs data this returns all the data filtered.
    def get_table_data(self):
        return self.object_list


class DashBoardTableView(FilterTableView):
    model = TeamStatsDf
    table_class = TeamStatsTable
    filter_class = TeamStatsFilter
    template_name = "dashboard_table.html"

    def get_table(self):
        table = super(DashBoardTableView, self).get_table()
        columns = self.request.GET.getlist('column')
        if columns:
            tuple_to_exclude = tuple(set(table.columns.names()) - set(columns))
            table.exclude = tuple_to_exclude
        return table

class DashBoardView(TemplateView):
    template_name = "dashboard.html"