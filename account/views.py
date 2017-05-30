from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.template import RequestContext
# from .models import UcUser
# from django.contrib.auth.decorators import login_required

#
#
# def login(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # TODO: is_active 필드 구현, false시 로그인 x
#             # if user.is_active:
#                 login(request, user)
#                 # 로그인 시 가장 먼저보일 url
#                 return HttpResponseRedirect('/')
#
#
#     return render_to_response(
#             '/registration/login.html',
#             context_instance=RequestContext(request)
#     )

# login이 필요한 view의 경우 데코레이터 추가
# @login_required(login_url='/accounts/login/')



def signup(request):
    """
    signup to register users
    """
    template = 'registration/signup.html'
    userForm = UserCreationForm()
    # 가입 양식 작성하하여 제출 시 POST
    if request.method == "POST":
        userForm = UserCreationForm(request.POST)
        # valid할 경우만 저장 TODO:is_valid() 양식에 맞게 생성필요.
        if userForm.is_valid():
            userForm.save()
            return HttpResponseRedirect(
                reverse("account:signup_ok_url")    # signup_ok라는 url으로
            )

    # 가입 양식 미작성 시 GET. 아무처리하지 X
    elif request.method == "GET":
        pass

    context = {"userForm" : userForm}
    return render(request, template, context)




