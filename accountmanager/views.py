from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        u = request.POST.get('username')
        e = request.POST.get('email')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        if p1 == p2:
            try:
                u = User(username=u, email=e, first_name=f, last_name=l)
                u.set_password(p1)
                u.save()
                messages.add_message(request, messages.SUCCESS, "Account create successfully")
                return redirect('login')
            except:
                messages.add_message(request, messages.ERROR, "Username already Exist")
                return redirect('signup')
        else:
            messages.add_message(request, messages.ERROR, "Password does not match")
            return redirect('signup')


class SigninView(View):
    template_name = 'signin.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Username or password didn't match")
            return redirect('login')


class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'
    login_url = 'login'

    def get(self, request):
        return render(request, self.template_name)


def signout(request):
    logout(request)
    return redirect('login')
