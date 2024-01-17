from django.urls import path

from contas.views import *

urlpatterns = [
    # path('contas/signup', ContaCreatView.as_view(), name="signup"),
    path('login/', login, name="login"),
    path('signin/', signin, name="signin"),
    path('usuario/', usuario, name="usuario"),
    path('signup/', signup, name="signup"),
    path('signout/', signout, name="signout"),
    path('userpage/', userpage, name="userpage"),
    path('deluser/', deluser, name="deluser"),
    path('modifyUser/', modifyUser, name="modifyUser"),
]