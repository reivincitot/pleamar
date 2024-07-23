from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.GET('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # redirige a la pagina home luego de haber iniciado sesión
        else:
            messages.error(request,'Credenciales inválidas. Inténtelo de nuevo')
    else:
      return render(request,'account/login.html')