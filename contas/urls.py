from django.urls import path

from contas.views import *

urlpatterns = [
    path('contas/signup', ContaCreatView.as_view(), name="signup"),
    path('signin/', signin, name="signin")
]