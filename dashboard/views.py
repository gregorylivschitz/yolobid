import logging
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, FormView, ListView, View
from django_filters.views import FilterView
from django_tables2 import SingleTableView, RequestConfig
from sqlalchemy import create_engine
from dashboard.filters import TeamStatsFilter
from dashboard.forms import DashboardForm, DashboardTeamForm, DashboardPlayerForm
from dashboard.models import DataSource, TeamStats, ProcessedTeamStatsDf, TeamStatsDf
from rest_framework import viewsets
from dashboard.multiforms import MultiFormsView
from dashboard.serializers import DataSourceSerializer
from dashboard.service.predict_player_stats import PredictPlayerStats
from dashboard.service.predict_team_outcome import PredictTeamWin
from dashboard.tables import TeamStatsTable
from django.conf import settings

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


class TeamPredictions(TemplateView):
    template_name = "team_predictions.html"

    def get_context_data(self, **kwargs):
        context = super(TeamPredictions, self).get_context_data()
        databases = getattr(settings, "DATABASES", None)
        database = databases['default']
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(database['USER'], database['PASSWORD'],
                                                                    database['HOST'], database['PORT'],
                                                                    database['NAME']), echo=False)
        predict = PredictTeamWin(engine,  'SK TELECOM T1', 'COUNTER LOGIC GAMING')
        predict_single_game = predict.predict_on_single_game()
        winning_percent = predict_single_game['SK TELECOM T1']
        context['team_name'] = 'SK TELECOM T1'
        context['winning_percent'] = winning_percent
        return context


class DashboardViewTest(MultiFormsView):
    template_name = 'dashboard_test.html'
    form_classes = {'submit_team': DashboardTeamForm,
                    'submit_player': DashboardPlayerForm}

    def submit_team_form_valid(self, form):
        if self.request.is_ajax():
            engine = self.get_engine()
            blue_team = form.cleaned_data['blue_team'].name
            red_team = form.cleaned_data['red_team'].name
            team_predictor_values = form.cleaned_data['team_predictor_values']
            print('predictor value {}'.format(team_predictor_values))
            predict = PredictTeamWin(engine, blue_team, red_team, predictor_stats=team_predictor_values)
            predict_single_game = predict.predict_on_single_game()
            morris_chart_data = []
            print('making morris chart')
            for k, v in predict_single_game.items():
                single_chart_point = {'label': k, 'value': v}
                morris_chart_data.append(single_chart_point)
            response_object = {'data': morris_chart_data}
            return JsonResponse(response_object)
        else:
            return HttpResponseRedirect(self.get_success_url())

    def submit_player_form_valid(self, form):
        engine = self.get_engine()
        player_name = form.cleaned_data['player_name'].name
        player_stats_to_predict = form.cleaned_data['player_stats_to_predict']
        player_predictor_values = form.cleaned_data['player_predictor_values']
        predicted_stats = self.predict_multiple_stats(engine, player_name, player_stats_to_predict, player_predictor_values)
        morris_chart_data = []
        for k, v in predicted_stats.items():
            single_chart_point = {'label': k, 'value': v[player_name][0]}
            morris_chart_data.append(single_chart_point)
        response_object = {'data': morris_chart_data}
        return JsonResponse(response_object)

    def predict_multiple_stats(self, engine, player, stats, player_predictor_values):
        stats_dict = {}
        stats = tuple(stats)
        for stat in stats:
            predict_player = PredictPlayerStats(engine, player, stat, player_predictor_values)
            predicted_player = predict_player.predict_player_stat()
            stats_dict[stat] = predicted_player
        return stats_dict

    @staticmethod
    def get_engine():
        databases = getattr(settings, "DATABASES", None)
        database = databases['default']
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(database['USER'], database['PASSWORD'],
                                                                    database['HOST'], database['PORT'],
                                                                    database['NAME']), echo=False)
        return engine
