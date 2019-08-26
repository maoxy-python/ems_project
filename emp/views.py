import os

from django.core.paginator import Paginator
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.http import JsonResponse

from emp.models import Employee
import uuid
# Create your views here.
def getemp(request):
    def mydefault(e):
        if isinstance(e, Employee):
            return {"id": e.id, "name": e.name, "age": e.age, "salary": str(e.salary),
                    "birthday": e.birthday.strftime("%Y-%m-%d"), "url": str(e.headpic.url)}

    id = request.GET.get("id")
    emp = Employee.objects.get(pk=id)
    return JsonResponse(emp,safe=False,json_dumps_params={"default":mydefault})

def emplist(request):
    def mydefault(e):
        if isinstance(e,Employee):
            return {"id":e.id,"name":e.name,"age":e.age,"salary":str(e.salary),"birthday":e.birthday.strftime("%Y-%m-%d"),"url":str(e.headpic.url)}
    emps = Employee.objects.all()
    print(emps)
    return JsonResponse({"emps":list(emps)},json_dumps_params={"default":mydefault})

def addlogic(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    salary = request.POST.get("salary")
    birthday = request.POST.get("birthday")
    headpic = request.FILES.get("headpic")

    headpic.name = str(uuid.uuid4()) + os.path.splitext(headpic.name)[1]

    emp = Employee.objects.create(name=name,age=age,salary=salary,birthday=birthday,headpic=headpic)
    if emp:
        return HttpResponse("ok")
    return("error")


def delete(request):
    id = request.GET.get("id")
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return HttpResponse("ok")

def updatelogic(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    age = request.POST.get("age")
    salary = request.POST.get("salary")
    birthday = request.POST.get("birthday")
    headpic = request.FILES.get("headpic")

    emp = Employee.objects.get(pk=id)
    emp.name=name
    emp.age=age
    emp.salary = salary
    emp.birthday=birthday

    if headpic:
        headpic.name = str(uuid.uuid4()) + os.path.splitext(headpic.name)[1]
        emp.headpic = headpic

    emp.save()
    return HttpResponse("ok")


def emp(request):

    print('123')
    print('165优秀')
    print('678')
    return HttpResponse('项目完成')