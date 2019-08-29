from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView
    )
from core.models import weapon, ammo, Vest, helmet, service_animals, special_sticks, special_gas_facilities, mobility_limiting_means, stun_devices

class WeaponList(ListView):
    model= weapon

class WeaponDetail(DetailView):
    models = weapon

class AmmoList(ListView):
    model = ammo

class AmmoDetail(DetailView):
    models = ammo

class VestList(ListView):
    model = Vest
class HelmetList(ListView):
    model = helmet

class S_AList(ListView):
    model = service_animals

class sp_st(ListView):
    model = special_sticks

class sp_g_f(ListView):
    model = special_gas_facilities

class m_l_m(ListView):
    model = mobility_limiting_means

class s_d(ListView):
    model = stun_devices


