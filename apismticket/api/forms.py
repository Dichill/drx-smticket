from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label="searchtxt", max_length=50)