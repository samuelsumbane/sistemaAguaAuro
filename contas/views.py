from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from contas.forms import ContasCadastrarForm

class ContaCreatView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    form_class = ContasCadastrarForm
    success_url = reverse_lazy('login')

    def form_valid(self, form) -> HttpResponse: 
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return HttpResponse('Invalid credentials.')
        else:
            login(request, user)
            return redirect('/')
            
                    
def signout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
        except:
            return HttpResponse('Something went wrong')