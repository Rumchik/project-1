from django.shortcuts import render
from django.views.generic import (
    ListView, DeleteView,
    )
from core.models import weapon, ammo, special_means

class WeaponList(ListView):
    model= weapon

class WeaponDetail(DeleteView):
    models = weapon

class AmmoList(ListView):
    model = ammo

class SpecialMeans(ListView):
    model = special_means
# Create your views here.
