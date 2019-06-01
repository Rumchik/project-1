from django.contrib import admin
from core.models import weapon
from core.models import ammo
from core.models import special_means

admin.site.register(weapon)
admin.site.register(ammo)
admin.site.register(special_means)
# Register your models here.
