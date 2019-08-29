from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'core'
urlpatterns = [
    path('weapon', views.WeaponList.as_view(), name='WeaponList'),
    path('ammo/', views.AmmoList.as_view(), name='AmmoList'),
    #path('weapon/<int:pk>', views.WeaponDetail.as_view(), name='WeaponDetail'),
    path('special_gas_facilities/', views.sp_g_f.as_view(), name='sp_g_f'),
    path('main/', views.VestList.as_view(), name='main'),
    path('weapon/(?P<slug>[0-9]+)', views.WeaponDetail.as_view(), name='WeaponDetail'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)