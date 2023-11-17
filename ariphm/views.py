from django.http import HttpRequest
from django.shortcuts import render

from .models import Task,taskList
from .forms import QuizForm,QuizItForm
def task_list(request:HttpRequest):
    context ={
        "tasks":Task.objects.all(),
    }
    return render(request,"ariphm/task-list.html", context=context)

def quiz(request:HttpRequest):

    if request.method == "POST":
        form=QuizItForm(request.POST)
        if form.is_valid():
            ans=form.cleaned_data["uAns"]
    else:
        var=taskList.objects.filter(varNumber=1).values('number','text')
     #   d=dict()
      #  for n in var:
       #     d[n['number']]=n['text']

        form=QuizItForm
    context ={
       # "d":d
        "form":form
    }
    return render(request,"ariphm/quiz.html", context=context)

# Create your views here.
