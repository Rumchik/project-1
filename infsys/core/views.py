from django.shortcuts import render
from django.views.generic import ListView
from core.models import weapon

class WeaponList(ListView):
    model= weapon

# Create your views here.
