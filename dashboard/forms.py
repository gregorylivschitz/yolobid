from django.forms import ModelForm, ModelChoiceField
from dashboard.models import Team, TeamStatsDf, Player, PlayerStatsDf, PlayerStats, ProcessedTeamStatsDf, \
    ProcessedPlayerStatsDf

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


def get_choices_for_predictors(ModelDF):
    choices_list = ModelDF._meta.get_all_field_names()
    choices = []
    for choice in choices_list:
        if ('csum_min_' in choice or 'eff' in choice) and 'allowed' not in choice \
                and 'game_number' not in choice and 'game_length' not in choice:
            cleaned_choice = choice.replace('csum_min_', 'per minute ').replace('eff', 'efficiency').replace('_', ' ').upper()
            choices.append((choice, cleaned_choice))
    return choices


# def get_choices_for_player_stats(ModelDF):
#     choices_list = ModelDF._meta.get_all_field_names()
#     choices = []
#     for choice in choices_list:
#         if ('csum_prev_min' in choice or 'eff' in choice) \
#                 and 'game_number' not in choice and 'game_length' not in choice \
#                 and 'csum_prev_minions_killed' != choice:
#             choices.append((choice, choice))
#     return choices

class DashboardTeamForm(forms.Form):
    choices = get_choices_for_predictors(ProcessedTeamStatsDf)
    blue_team = NameModelChoiceField(label="", empty_label="Select Blue Team", queryset=Team.objects.all(),
                                     to_field_name='name')
    red_team = NameModelChoiceField(label="", empty_label="Select Red Team", queryset=Team.objects.all(),
                                    to_field_name='name')
    team_predictor_values = forms.MultipleChoiceField(label="Select Predictors(Advance Option)", choices=choices,
                                                 required=False)
    team_game_range = forms.ChoiceField(label="", choices=([('empty_label', 'Select Game Range (Advance Option)'),
                                                         ('5', '5 game back'),
                                                         ('10', '10 games back')]), required=False)

    def __init__(self, *args, **kwargs):
        super(DashboardTeamForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'predict-team-outcome'
        self.helper.form_class = 'predictTeamOutCome'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_team', 'Submit', css_class='btn btn-theme'))


class DashboardPlayerForm(forms.Form):
    predictor_choices = get_choices_for_predictors(ProcessedPlayerStatsDf)
    player_stats_choices_list = ('kills', 'deaths', 'assists', 'minions_killed', 'gold')
    player_choices = [(choice, choice) for choice in player_stats_choices_list]
    player_name = NameModelChoiceField(label="", empty_label="Select Player", queryset=Player.objects.all())
    player_stats_to_predict = forms.MultipleChoiceField(label="Select stats to predict", choices=player_choices)
    player_predictor_values = forms.MultipleChoiceField(label="Select Predictors(Advance Option)",
                                                        choices=predictor_choices, required=False)
    player_game_range = forms.ChoiceField(label="", choices=([('empty_label', 'Select Game Range (Advance Option)'),
                                                         ('5', '5 game back'),
                                                         ('10', '10 games back')]), required=False)
    opposing_team = NameModelChoiceField(label="", empty_label="Select Opposing Team", queryset=Team.objects.all(),
                                     to_field_name='name')

    def __init__(self, *args, **kwargs):
        super(DashboardPlayerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'predict-player-outcome'
        self.helper.form_class = 'predictPlayerOutCome'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_player', 'Submit', css_class='btn btn-theme'))

