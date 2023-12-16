from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .models import Task, AnswerQuiz, Work
from .forms import QuizForm


def quiz(request:HttpRequest):
    obj = Task.objects.filter(varNumber=request.user.id, isSubmitted=False)
    if obj:
        tObj=obj[0]
        if request.user.is_authenticated:
            if request.method == "POST":
                form=QuizForm(request.POST)
                if form.is_valid():
                    ans=form.cleaned_data["uAnswer"]
                    AnswerQuiz.objects.create(
                        uAnswer=ans,
                        correct= ans==tObj.answer,
                        userN=request.user.id,
                        isSubmitted=True,
                        taskN=tObj.id,
                        numbInV=tObj.number,
                    )
                    if ans==tObj.answer: tObj.rightAnswCount+=1
                    tObj.isSubmitted=True
                    tObj.save()
                    return redirect('quiz:quiz')
            else:

                form=QuizForm
            context ={
                "t":tObj,
                "form":form,
                "fname":request.user.first_name,
                "lname": request.user.last_name,
            }
        else:
            return redirect('myauth:register')
        return render(request, "quiz/quiz.html", context=context)
    else:
        return redirect('myauth:about-me')

def results(request: HttpRequest):
    if request.user.is_authenticated:
        ws = request.user.student.workToDo.all()
        wksL=[]
        for w in ws:
            tskL=[]
            tasks = Task.objects.filter(toUser=request.user, isSubmitted=True,work=w)
            for task in tasks:
                tskL.append({"n":task.number,"ans":task.uAnswer,"rAns":task.answer,"zachet":task.rightAnsw,"text":task.text})
            wksL.append({"n":w.name,"t":tskL})

            context = {
                "wksL":wksL,
                "user": request.user,
                'ia': request.user.is_authenticated
            }
        return render(request, "quiz/results.html", context=context)
    else:
        return redirect('myauth:register')


def journal(request: HttpRequest):
    if request.user.is_authenticated:
        answs = AnswerQuiz.objects.all()
        j=[]
        while answs.exists():
            exUserID=answs.first().userID
            ans=answs.filter(userID=exUserID)
            plusList=[]
            for an in ans:
                if an.correct:
                    plusList.append('+')
                else:
                    plusList.append('-')
            u={"name":ans.first().userID.first_name+" "+ans.first().userID.last_name, "plus":plusList,"corAns":plusList.count("+")}
            j.append(u)
            answs=answs.exclude(userID=exUserID)

        context = {
                "tL":j[0]["plus"],
                "uList":j,
                "user": request.user,
        }
        return render(request, "quiz/journal.html", context=context)
    else:
        return redirect('myauth:register')
def work(request:HttpRequest):
    if request.user.is_authenticated:
        ws = request.user.student.workToDo.all()
        tasks = Task.objects.filter(toUser=request.user, isSubmitted=False)
        if request.method == "POST":
            for task in tasks:
                ans=request.POST[str(task.pk)]
                if ans:ans=int(ans)
                else:ans=None
                AnswerQuiz.objects.create(
                    uAnswer=ans,
                    correct = ans==task.answer,
                    taskID=task,
                    userID=request.user
                )
                task.rightAnsw=ans==task.answer
                task.isSubmitted=True
                task.uAnswer=ans
                task.save()
            #w.student.remove(request.user.student)
            return redirect('quiz:main_journal')
        else:
            if tasks.exists():
                dic=[]
                for w in ws:
                    dic.append({"name":w.name,"ts":Task.objects.filter(toUser=request.user, isSubmitted=False,work=w)})
                context ={
                    "dic":dic,
                    "tasks":tasks,
                    "request":request,
                    'ia': request.user.is_authenticated,
                }
                return render(request, "quiz/work.html", context=context)
            else:
                return redirect('quiz:main_journal') #work done

    else:
        return redirect('myauth:register')

def mainJournal(request: HttpRequest):
    if request.user.is_authenticated:
        usrs=User.objects.all().order_by("last_name")
        tsks=Task.objects.all()
        jL=[]
        maxLen=0
        wsAll=Work.objects.all()
        for usr in usrs:
            bal=0
            ws=usr.student.workToDo.all()
            workL=[]
            for w in wsAll:
                tsksf = tsks.filter(toUser=usr, isSubmitted=True,work=w)
                plusList = ""
                if w in ws:
                    for t in tsksf:
                        if t.rightAnsw:
                            plusList+='+'
                        else:
                            plusList+='-'
                    plusList+=str(plusList.count("+"))
                    bal+=plusList.count("+")
                else:
                    plusList+='X'*w.numbOfTasks+'0'
                workL.append(plusList)
            jL.append({"name":usr.first_name+' '+usr.last_name, "pl":workL, "bal":bal})

        context = {
            'ia':request.user.is_authenticated,
            'usrs':usrs,
            "wsAll":wsAll,
            "jL":jL,
            "user": request.user,
        }
        return render(request, "quiz/work_journal.html", context=context)
    else:
        return redirect('myauth:register')

