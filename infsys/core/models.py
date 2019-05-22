from django.db import models

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
    #ammo_image-models.ImageField()
    
    #иные сведения
    #common_view_ammo=models.ImageField()
    #common_view_bullet-models.ImageField()
    #pack_common_view=models.ImageField()

    def __str__(self):
        return '{} ({})'.format(self.ammo_name, self.diameter_head_part)