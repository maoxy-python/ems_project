from django.urls import path
from emp import views

urlpatterns = [
    path("getemp/",views.getemp,name="getemp"),
    path("emplist/",views.emplist,name="emplist"),
    path("addlogic/",views.addlogic,name="addlogic"),
    path("delete/",views.delete,name="delete"),
    path("updatelogic/",views.updatelogic,name="updatelogic"),

]