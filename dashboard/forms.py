from django.forms import ModelForm, ModelChoiceField
from dashboard.models import Team, TeamStatsDf, Player, PlayerStatsDf, PlayerStats

__author__ = 'glivschitz'

from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Layout, Submit, Field, Fieldset, ButtonHolder


class DashboardForm(forms.Form):
    team_name = forms.CharField(required=True)
    won = forms.BooleanField(required=False)
    color = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(DashboardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('team_name', data_label_text="team_name"),
            Field('won', data_label_text="won"),
            Field('color', data_label_text="color")
        )
        self.helper.add_input(Submit('submit', 'Submit'))


class NameModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class DashboardTeamForm(forms.Form):
    choices_list = TeamStatsDf._meta.get_all_field_names()
    choices = [(choice, choice) for choice in choices_list]
    blue_team = NameModelChoiceField(label="", empty_label="Select Blue Team", queryset=Team.objects.all())
    red_team = NameModelChoiceField(label="", empty_label="Select Red Team", queryset=Team.objects.all())
    team_predictor_values = forms.MultipleChoiceField(label="Select Predictors(Advance Option)", choices=choices,
                                                 required=False)

    def __init__(self, *args, **kwargs):
        super(DashboardTeamForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'predict-team-outcome'
        self.helper.form_class = 'predictTeamOutCome'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_team', 'Submit', css_class='btn btn-theme'))


class DashboardPlayerForm(forms.Form):
    predictor_choices_list = PlayerStatsDf._meta.get_all_field_names()
    predictor_choices = [(choice, choice) for choice in predictor_choices_list]
    player_stats_choices_list = PlayerStats._meta.get_all_field_names()
    player_choices = [(choice, choice) for choice in player_stats_choices_list]
    player_name = NameModelChoiceField(label="", empty_label="Select Player", queryset=Player.objects.all())
    player_stats_to_predict = forms.MultipleChoiceField(label="Select stats to predict", choices=player_choices)
    player_predictor_values = forms.MultipleChoiceField(label="Select Predictors(Advance Option)",
                                                        choices=predictor_choices, required=False)

    def __init__(self, *args, **kwargs):
        super(DashboardPlayerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'predict-player-outcome'
        self.helper.form_class = 'predictPlayerOutCome'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_player', 'SUBMIT', css_class='btn btn-theme'))

