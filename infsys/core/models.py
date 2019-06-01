from django.db import models
from django.utils.text import slugify

# var = models.type(blank=True) - не обязательное заполнеине поля  


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class weapon(models.Model):

#основные характеристики
    weapons_name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    length = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    barrel_length = models.PositiveIntegerField()
    mass = models.PositiveIntegerField()
    caliber = models.PositiveIntegerField()

#характеристики следообразующих деталей
    method_manufacture_barrel = models.TextField()
    number_rifling = models.PositiveIntegerField()
    direction_rifling = models.TextField()
    width_fields_rifling = models.PositiveIntegerField()
    angle_rifling = models.PositiveIntegerField()
    gas_outlet = models.TextField()
    strikers_diameter = models.PositiveIntegerField()
    width_hook_extractor = models.PositiveIntegerField()
    angle_between_hook_reflector = models.PositiveIntegerField()
    chamber_shape = models.PositiveIntegerField()
    chamber_length = models.PositiveIntegerField()
    trace_pattern_sleev = models.TextField()

# технические характеристики
    sleeves_reflection = models.TextField()
    automation_principle = models.TextField()
    locking_mech = models.TextField()
    trigger_mech = models.TextField()
    safety_catch = models.TextField()
    liner_removal_mech = models.TextField()
    used_ammo = models.TextField()
    magazine = models.TextField()
    magazines_capacity = models.PositiveIntegerField()

#маркировочные обозначенния 
    marking_designation_description = models.TextField()
    location_details = models.TextField()
   # marking_image = models.ImageField(upload_to=image_folder)

#иные сведения
    disassembly_procedure = models.TextField()
    #weapons_photo = models.ImageField()
    #trace_pattern_sleev_image = models.ImageField()
    features = models.TextField()

    def __str__(self):
        return '{} ({})'.format(self.weapons_name, self.length)

class ammo(models.Model):
    #общие характеристики
    ammo_name=models.CharField(max_length=80)
    ammo_producer=models.CharField(max_length=100)
    ammo_length=models.IntegerField()
    powder_mass=models.IntegerField()
    ignition_type=models.CharField(max_length=160)
    mounting_method=models.CharField(max_length=160)

    #характеристики гильзы
    shell_length=models.IntegerField()
    diameter_dults=models.IntegerField()
    diameter_case_slope=models.IntegerField()
    case_diameter_bottom=models.IntegerField()
    bottom_diameter=models.IntegerField()
    flange_diameter=models.IntegerField()
    form=models.TextField()
    material_color=models.CharField(max_length=80)

    #характеристики капсуля
    capsule_type=models.CharField(max_length=80)
    capsule_material_color=models.CharField(max_length=80)
    diameter=models.IntegerField()

    #характеристики пули
    head_part_form=models.CharField(max_length=80)
    bullet_length=models.IntegerField()
    diameter_head_part=models.IntegerField()
    bullet_mass=models.IntegerField()
    bullet_type=models.CharField(max_length=80)

    #маркировочные оозначения
    markings=models.TextField()
    #ammo_image=models.ImageField()
    
    #иные сведения
    #common_view_ammo=models.ImageField()
    #common_view_bullet-models.ImageField()
    #pack_common_view=models.ImageField()

    def __str__(self):
        return '{} ({})'.format(self.ammo_name, self.diameter_head_part)

class special_means(models.Model):
    type1=1
    type2=2
    type3=3
    type4=4
    type5=5
    type6=6
    type7=7
    type8=8
    type9=9
    type10=10
    type11=11
    type12=12
    type13=13
    type14=14
    variants_of_type = (
        (type1, 'Палки специальные'),
        (type2, 'Специальные газовые средства'),
        (type3, 'Средства ограничения подвижности'),
        (type4, 'Специальные окрашивающее средства'),
        (type5, 'Электрошоковые устройства'),
        (type6, 'Светошоковые устройства'),
        (type7, 'Служебные животные'),
        (type8, 'Световые и звуковые специальные средства'),
        (type9, 'Средства остановки транспорта'),
        (type10, 'Средства сковывания движения'),
        (type11, 'Водомёты'),
        (type12, 'Бронемашины'),
        (type13, 'Средства защиты охраняемых объектов'),
        (type14, 'Средства разрушения преград'),
    )
    type_of_sm = models.IntegerField(
        choices=variants_of_type,
        default=type1
    )
    sm_title=models.CharField(max_length=100)
    if type_of_sm == type1:
        manufacturing_method = models.CharField(max_langth=80)
        manufacturing_material = models.CharField(max_length=80)
        stick_diameter = models.PositiveIntegerField()
        stick_mass = models.PositiveIntegerField()
        stick_length = models.PositiveIntegerField()
        stick_description = models.TextField()
        #stick_image = models.ImageField()
    elif type_of_sm == type2:
        gase_grenade_description = models.CharField(max_length=80)
        gase_grenade_mass = models.PositiveIntegerField()
        gase_grenade_diameter = models.PositiveIntegerField()
        gase_grenade_length = models.PositiveIntegerField()
        voleme_of_aerosol_cloud = models.CharField(max_length=100)
        temprature_range_of_application = models.CharField(max_length=100)
        #gase_grenade_image = models.ImageField()
    
    elif type_of_sm == type3:
        handcuffs_descrioption = models.TextField()
        handcuffs_material = models.CharField(max_length=200)
        handcuffs_mass = models.PositiveIntegerField()
        number_of_links = models.PositiveIntegerField()
        equipment = models.TextField()
        number_of_openings = models.CharField(max_length=160)
        rings_diameter = models.PositiveIntegerField()
        guarantee_period = models.PositiveIntegerField()

    elif type_of_sm == type5:
        stun_gun_formfactor = models.CharField(max_length=100)
        operating_principle = models.CharField(max_length=100)
        electrodes = models.CharField(max_length=200)
        voltage = models.PositiveIntegerField()
        efficiency = models.CharField(max_length=100)
        stun_gun_mass = models.PositiveIntegerField()
        stun_gun_length = models.PositiveIntegerField()
        stun_gun_height = models.PositiveIntegerField()
        stun_gun_width = models.PositiveIntegerField()
        material = models.CharField(max_length=80)
        power_methods = models.CharField(max_length=160)
        charging = models.CharField(max_length=300)