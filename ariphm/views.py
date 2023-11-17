from django.http import HttpRequest
from django.shortcuts import render

from .models import Task
from .forms import QuizForm
def task_list(request:HttpRequest):
    context ={
        "tasks":Task.objects.all(),
    }
    return render(request,"ariphm/task-list.html", context=context)

def quiz(request:HttpRequest):

    if request.method == "POST":
        form=QuizForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            a1=form.cleaned_data["a1"]
            a2 = form.cleaned_data["a2"]
            a3 = form.cleaned_data["a3"]
            Task.objects.create(name=name,description=a1,answer=int(a2))
    else:
        tasks=taskList.objects.all()

        form=QuizForm
    context ={
        "form":form
    }
    return render(request,"ariphm/quiz.html", context=context)

# Create your views here.
