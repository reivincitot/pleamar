from django.shortcuts import render
from .models import Participaciones


def home_view(request):
    return render(request, 'homepage/home.html')