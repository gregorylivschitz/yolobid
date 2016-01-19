from django.views.generic import TemplateView, FormView, ListView, View
from dashboard.forms import DashboardForm
from dashboard.models import DataSource, TeamStats
from rest_framework import viewsets
from dashboard.serializers import DataSourceSerializer


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
        view = DashboardListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = DashboardView.as_view()
        return view(request, *args, **kwargs)