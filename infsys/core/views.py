#файл отвечает за предоставление данных из БД по соответствующим запросам во фронт, а также открывает соответстующие 
# html-файлы по указанному в браузере пути
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView
    )
from .models import weapon, gas_weapon, air_weapon, ammo, Vest, helmet, service_animals, special_sticks, special_gas_facilities, mobility_limiting_means, stun_devices
from django.shortcuts import redirect

def weapon_list(request):
    weapons = weapon.objects.all()
    return render(request, 'core/weapon_list.html', context={'weapons': weapons})

def weapon_detail(request, pk):
    Weapon = get_object_or_404(weapon, pk=pk)
    context = { 'weapon': weapon }
    return render(request, 'core/weapon_detail.html', context)

def gas_weapon_list(request):
    gas_weapons = gas_weapon.objects.all()
    return render(request, 'core/gas_weapon_list.html', context={'gas_weapons': gas_weapons})

def gas_weapon_detail(request, pk):
    Gas_weapon = get_object_or_404(gas_weapon, pk=pk)
    context = {'gas_weapon': gas_weapon }
    return render(request, 'core/gas_weapon_detail.html', context)

def air_weapon_list(request):
    air_weapons = air_weapon.objects.all()
    return render(request, 'core/air_weapon_list.html', context={'air_wepons': air_weapon})

def air_weapon_detail(request, pk):
    Air_weapon = get_object_or_404(air_weapon, pk=pk)
    context = {'air_weapn': air_weapon}
    return render(request, 'core/air_weapon_detail.html', context)

def main_page(request):
    weapons = weapon.objects.all()
    return render(request, 'core/Главная.html', context={'weapons': weapons})
    
def ammo_list(request):
    ammos = ammo.objects.all()
    return render(request, 'core/ammo_list.html', context={'ammos': ammos})

def ammo_detail(request, pk):
    Ammo = get_object_or_404(ammo, pk=pk)
    return render(request, 'core/ammo_detail.html', context={'ammo': ammo})

def sm_list(request):
    special_gas_facilitiess = special_gas_facilities.objects.all()
    return render(request, 'core/sm_list.html', context={'special_gas_facilitiess': special_gas_facilitiess})

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
