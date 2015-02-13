from django import forms


class RangeForm(forms.Form):
    num = forms.IntegerField(max_value=101)
