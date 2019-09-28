#файл с url-запросыми приложения
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from core.views import weapon_list, weapon_detail, gas_weapon_list, gas_weapon_detail, air_weapon_list, air_weapon_detail, main_page, ammo_list, ammo_detail, sm_list

app_name = 'core'
urlpatterns = [
    path('оружие', weapon_list, name='WeaponList'),
    path('оружие/<int:pk>', weapon_detail, name='WeaponDetail'),
    path('', main_page, name='Главная'),
    path('патроны', ammo_list, name='AmmoList'),
    path('патроны/<int:pk>', ammo_detail, name='AmmoDetail'),
    path('газовое_оружие', gas_weapon_list, name='GasWeaponList'),
    path('газовое_оружие/<int:pk>', gas_weapon_detail, name='GasWeaponDetail'),
    path('пневматическое_оружие', air_weapon_list, name='AirWeaponList'),
    path('пневматическое_оружие/<int:pk>', air_weapon_detail, name='AirWeaponDetail'),
    path('специальные_средства', sm_list, name='SMList'),
    path('специальные_средства/<int:pk>', ammo_detail, name='SMDetail'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)