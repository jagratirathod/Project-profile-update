from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic.edit import CreateView

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import Loginform
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def hello(request):
    return HttpResponse("hiii")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class LoginView(CreateView):
    form_class = Loginform
    template_name = "login.html"
    context_object_name = 'loginhere'
    success_url = reverse_lazy('app:login')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email)
        if user:
            return redirect("/app/profile/")
        else:
            return HttpResponse("Invalid User")





@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and  p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    context =  {
        'u_form' :  u_form,
        'p_form': p_form
    }

    return render(request,"profile.html",context)