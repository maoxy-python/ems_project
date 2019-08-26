from django.urls import path
from user import views


urlpatterns = [
    path("loginlogic/",views.loginlogic,name="loginlogic"),
    path("registlogic/", views.registlogic, name="registlogic"),
    path("checkname/", views.checkname, name="checkname"),
    path("checkcode/", views.checkcode, name="checkcode"),
    path("getcaptcha/", views.getcaptcha, name="getcaptcha"),
]