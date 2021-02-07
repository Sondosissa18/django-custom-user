# from django.shortcuts import render , redirect


# from django.contrib.auth import login, authenticate

from myuser.models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from .forms import  LoginForm , RegisterForm

# MyUser = settings.AUTH_USER_MODEL

from myuser.forms import LoginForm



def index_view(request):
    context_dict = {"MyUser": settings.AUTH_USER_MODEL}
    # MyUser = settings.AUTH_USER_MODEL

    return render(request, 'home.html', context_dict)

    


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # user = authenticate(
            #     request, username=data["username"], password=data["password"]
            # )

            MyUser.objects.create_user(
                username=data["username"], password=data["password"]
            )
            return HttpResponseRedirect(
                    request.GET.get("next", reverse("home"))
                )
    form = RegisterForm()
    return render(request, "signup.html", {"form": form})





def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("home"))
                )
    form = LoginForm()
    return render(request, "login.html", {"form": form})

