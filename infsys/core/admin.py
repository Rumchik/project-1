from django.contrib import admin
from core.models import weapon
from core.models import ammo
from core.models import Vest
from core.models import helmet
from core.models import service_animals
from core.models import special_sticks
from core.models import special_gas_facilities
from core.models import mobility_limiting_means
from core.models import stun_devices

admin.site.register(weapon)
admin.site.register(ammo)
admin.site.register(Vest)
admin.site.register(helmet)
admin.site.register(service_animals)
admin.site.register(special_sticks)
admin.site.register(special_gas_facilities)
admin.site.register(mobility_limiting_means)
admin.site.register(stun_devices)
# Register your models here.
