from django import forms
from .models import quiz
class QuizForm(forms.Form):
    name = forms.CharField()
    a1= forms.IntegerField()
    a2 = forms.IntegerField()
    a3 = forms.IntegerField()

#class QuizItForm(forms.ModelForm):
#    class Meta
 #       model = quiz
  #      fields = ['uAnswer']
