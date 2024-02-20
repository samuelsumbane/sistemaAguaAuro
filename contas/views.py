from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout

from contas.forms import ContasCadastrarForm
from random import randint



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
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            auth_login(request, user)
            return redirect('/') 
        else:
            return HttpResponse('Invalid credentials.')

      
                    
def signout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':

        letras = ('0', '1', '2', '3', '4', '5', '6', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)
        senha = ''
        for a in range(5):
            senha += str(letras[randint(2, 8)])

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        # password = request.POST['password']
        newuser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=senha
        )
        try:
            newuser.save()
            data = '200'
            return JsonResponse({'data':data, 'password':senha})    
            
        except:
            return HttpResponse('Something went wrong')
        
        
def deluser(request):
    if request.method == 'GET':
        id = request.GET['id']
        try:
            User.objects.filter(id=id).delete()
            data = '200'
        except:
            data = '201'            
        return JsonResponse({'data':data})
        
        

def modifyUser(request):
    if request.method == 'GET':
        id = request.GET['id']
        action = request.GET['action']                          
            
        try:
            user = User.objects.get(id=id)

            if action == 'activeUser':
                user.is_active = True          
                
            elif action == 'disableUser':
                user.is_active = False          
                              
            elif action == 'promoveUser':
                user.is_superuser = True                
                
            elif action == 'despromoveUser':
                user.is_superuser = False                
        
            user.save()
            data = '200'
        except:
            data = '201'            
        return JsonResponse({'data':data})
        
        


def usuario(request):
    usuarios = User.objects.all()
    return render(request, "usuario.html", {"usuarios": usuarios})


def login(request):
    return render(request, "registration/login.html")
    
    
def userpage(request):
    return render(request, "userpage.html")
        
    
    