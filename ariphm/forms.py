from django import forms

class QuizForm(forms.Form):
    name = forms.CharField()
    a1=forms.IntegerField()
    a2 = forms.IntegerField()
    a3 = forms.IntegerField()