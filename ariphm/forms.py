from django import forms
from .models import quiz, AnswerQuiz
class QuizForm(forms.Form):
    name = forms.CharField()
    a1= forms.IntegerField()
    a2 = forms.IntegerField()
    a3 = forms.IntegerField()

class QuizItForm(forms.ModelForm):
    class Meta:
        model=AnswerQuiz
        fields = "__all__"
