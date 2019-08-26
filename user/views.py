import random
import string

from django.db import transaction
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from user.captcha.image import ImageCaptcha
from user.models import User
# Create your views here.


def loginlogic(request):
    '''
    处理登录逻辑
    :param request:
    :return:
    '''
    username = request.POST.get("username")
    userpwd = request.POST.get("userpwd")
    rem = request.POST.get("remember")
    result = User.objects.filter(name=username,password=userpwd)
    if result:
        request.session["login"]="ok"
        response = HttpResponse("ok")
        if rem:
            response.set_cookie("name",username.encode("utf-8").decode("latin-1"),max_age=7*24*3600)
            response.set_cookie("password",userpwd,max_age=7*24*3600)
        return response
    return HttpResponse("error")


def registlogic(request):
    '''
    处理注册逻辑
    :param request:
    :return:
    '''
    try:
        with transaction.atomic():
            username = request.POST.get("username")
            if not username:
                raise
            userpwd = request.POST.get("userpwd")
            realname = request.POST.get("realname")
            gender = request.POST.get("gender")
            print(username, userpwd, realname, gender)
            u = User.objects.create(name=username, password=userpwd, realname=realname, gender=gender)
            if u:
                return HttpResponse("ok")
    except:
        return HttpResponse("error")

def checkname(request):
    name = request.POST.get("username")
    result = User.objects.filter(name=name)
    if result:
        return HttpResponse("error")
    return HttpResponse("ok")


def getcaptcha(request):

    image = ImageCaptcha() # 声明一个图片验证码的对象
    # 生成一个随机码
    codes = random.sample(string.ascii_letters+string.digits,5)
    codes = "".join(codes)
    print(codes)
    request.session['codes'] = codes
    data = image.generate(codes)
    print(data)
    return HttpResponse(data,"image/png")

def checkcode(request):
    input_codes = request.POST.get("code")
    codes = request.session.get("codes")
    if input_codes.lower() == codes.lower():
        return HttpResponse("ok")
    return HttpResponse("error")