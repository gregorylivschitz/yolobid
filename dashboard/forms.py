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