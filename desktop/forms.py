from django import forms

from . import forms_logic as logic


class AddLesson(forms.Form):
    name = forms.CharField(max_length=64)
    classroom = forms.CharField(max_length=8)
    number = forms.IntegerField(max_value=8)
    day = forms.ChoiceField(choices=logic.get_weekdays_touple())

class AddHomework(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows" : 4, "cols" : 40}), label='Homework', required=False)
