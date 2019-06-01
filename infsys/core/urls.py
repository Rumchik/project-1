from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('weapon',
    views.WeaponList.as_view(),
    name='WeaponList'),
]