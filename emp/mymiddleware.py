from django.shortcuts import redirect,HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from user.models import User

class Mymiddleware(MiddlewareMixin):
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("init1")

    # view处理请求前执行
    def process_request(self, request):  # 某一个view
        print(request.path)
        # if "emp/emplist" not in request.path:
        #     return redirect("/static/emp/emplist.html")
        # print("REFER:"
        #
        #
        #
        # ,request.META.get("HTTP_REFERER"))
        # refer = request.META.get("HTTP_REFERER")
        # if "user/login" in refer:
        #     name = request.COOKIES.get("name")
        #     if name:
        #         name = name.encode("latin-1").decode("utf-8")
        #     pwd = request.COOKIES.get("password")
        #     result = User.objects.filter(name=name,password=pwd)
        #     if result:
        #         print(result)
        #         res = redirect("/static/emp/emplist.html")
        #         return res

    # 在process_request之后View之前执行
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("view:", request, view_func, view_args, view_kwargs)

    # view执行之后，响应之前执行
    def process_response(self, request, response):
        print("response:", request, response)
        return response  # 必须返回response

    # 如果View中抛出了异常
    def process_exception(self, request, ex):  # View中出现异常时执行
        print("exception:", request, ex)