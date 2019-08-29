from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from transliterate import translit
 #var = models.type(blank=True) - не обязательное заполнеине поля  


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug

class weapon(models.Model):

#основные характеристики
    weapons_name = models.CharField(max_length=100, verbose_name = "Название")
    producer = models.CharField(max_length=100, verbose_name = "Производитель")
    length = models.PositiveIntegerField(verbose_name = "Длина")
    height = models.PositiveIntegerField(verbose_name = "Высота")
    width = models.PositiveIntegerField(verbose_name = "Ширина")
    barrel_length = models.PositiveIntegerField(verbose_name = "Длина ствола")
    mass = models.PositiveIntegerField(verbose_name = "Масса")
    caliber = models.PositiveIntegerField(verbose_name = "Калибр")

#характеристики следообразующих деталей
    method_manufacture_barrel = models.TextField(verbose_name = "Способ изготовления ствола")
    number_rifling = models.PositiveIntegerField(verbose_name = "Количество нарезов")
    direction_rifling = models.TextField(verbose_name = "Направление нарезов")
    width_fields_rifling = models.PositiveIntegerField(verbose_name = "Ширина полей нарезов")
    angle_rifling = models.PositiveIntegerField(verbose_name = "Угол наклона нарезов")
    gas_outlet = models.TextField(verbose_name = "Наличае газоотводного отверстия в канале ствола")
    strikers_diameter = models.PositiveIntegerField(verbose_name = "Диаметр бойка, мм")
    width_hook_extractor = models.PositiveIntegerField(verbose_name = "Ширина зацепа выбрасывателя")
    angle_between_hook_reflector = models.PositiveIntegerField(verbose_name = "Угол между зацепом выбрасывателя и отражателем")
    chamber_shape = models.PositiveIntegerField(verbose_name = "Форма патронника")
    chamber_length = models.PositiveIntegerField(verbose_name = "Длина патронника")
    trace_pattern_sleev = models.TextField(verbose_name = "Схема следов на гильзе")

# технические характеристики
    sleeves_reflection = models.TextField(verbose_name = "Отражение гильзы")
    automation_principle = models.TextField(verbose_name = "Принцип отражателя")
    locking_mech = models.TextField(verbose_name = "Механизм запирания ствола")
    trigger_mech = models.TextField(verbose_name = "Ударно-спусковой механизм")
    safety_catch = models.TextField(verbose_name = "Предохранитель")
    liner_removal_mech = models.TextField(verbose_name = "Механиз удаления гильзы")
    used_ammo = models.TextField(verbose_name = "Применяемый патрон")
    magazine = models.TextField(verbose_name = "Магазин")
    magazines_capacity = models.PositiveIntegerField(verbose_name = "Ёмкость магазина, патронов")

#маркировочные обозначенния 
    marking_designation_description = models.TextField(verbose_name = "Маркировочные обозначения (описание)")
    location_details = models.TextField(verbose_name = "Расположение на деталях оружия")
    marking_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение маркировочных значений")

#иные сведения
    disassembly_procedure = models.TextField(verbose_name = "Порядок неполной сборки и разборки")
    weapons_photo = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение оружия")
    trace_pattern_sleev_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение следообразующих деталей")
    features = models.TextField(verbose_name = "Технические и иные особенности, характерные для этой модели")

    slug = models.CharField(max_length=255, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("weapon", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружие'


    def __str__(self):
        return '{} ({})'.format(self.weapons_name, self.length)

class ammo(models.Model):
    #общие характеристики
    ammo_name=models.CharField(max_length=80, verbose_name = "Название")
    ammo_producer=models.CharField(max_length=100, verbose_name = "Производитель")
    ammo_length=models.IntegerField(verbose_name = "Длина")
    ammo_mass=models.IntegerField(blank=True, verbose_name = "Масса патрона")
    powder_mass=models.IntegerField(verbose_name = "Масса порохового (иного) заряда")
    ignition_type=models.CharField(max_length=160, verbose_name = "Тип воспламенитиля")
    mounting_method=models.CharField(max_length=160, verbose_name = "Способ крепления пули с гильзой")

    #характеристики гильзы
    shell_length=models.IntegerField(verbose_name = "Длина гильзы")
    diameter_dults=models.IntegerField(verbose_name = "Диаметр дульца")
    diameter_case_slope=models.IntegerField(verbose_name = "Диаметр корпуса у ската")
    case_diameter_bottom=models.IntegerField(verbose_name = "Диаметр корпуса у донного упора")
    bottom_diameter=models.IntegerField(verbose_name = "Диаметр донного упора")
    flange_diameter=models.IntegerField(verbose_name = "Диаметр фланца")
    form=models.TextField(verbose_name = "Форма")
    material_color=models.CharField(max_length=80, verbose_name = "Цвет материала")
    
    #характеристики капсуля
    capsule_type=models.CharField(max_length=80, verbose_name = "Тип капсуля")
    capsule_material_color=models.CharField(max_length=80, verbose_name = "Цвет материала")
    diameter=models.IntegerField(verbose_name = "Диаметр капсуля")

    #характеристики пули
    head_part_form=models.CharField(max_length=80, verbose_name = "Длина головной части")
    bullet_length=models.IntegerField(verbose_name = "Длина пули, мм")
    diameter_head_part=models.IntegerField(verbose_name = "Диаметр ведущей части, мм")
    bullet_mass=models.IntegerField(verbose_name = "Масса пули, г")
    bullet_type=models.CharField(max_length=80, verbose_name = "Тип пули")

    #маркировочные оозначения
    markings=models.TextField(verbose_name = "Маркировочное обозначение (описание)")
    ammo_image=models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение маркировочных обохнаений")
    
    #иные сведения
    common_view_ammo = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение общего вида патрона")
    common_view_bullet = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "общее изображение пули")
    pack_common_view = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение упаковки")

    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Патроны'
        verbose_name_plural = 'Патроны'

    def __str__(self):
        return '{} ({})'.format(self.ammo_name, self.diameter_head_part)

"""
1) палки специальные - realize
2) специальные газовые средства - realize
3) средства ограничения подвижности - realized
4) специальные окрашивающие и маркирующие средства 
5) электрошоковые устройства - realized
6) светошоковые устройства 
7) служебных животных -realized
8) световые и акустические специальные средства 
9) средства принудительной остановки транспорта 
10) средства сковывания движения 
11) водометы 
12) бронемашины
13) средства защиты охраняемых объектов (территорий), блокирования движения групп граждан, совершающих противоправные действия
14) средства разрушения преград 
"""
class special_sticks(models.Model):
    special_sticks_title = models.CharField(max_length=80, blank=True, verbose_name = "Навание")
    manufacturing_method = models.CharField(max_length=80, verbose_name = "Метод производства")
    manufacturing_material = models.CharField(max_length=80, blank=True, verbose_name = "Материал производства")
    stick_diameter = models.PositiveIntegerField(verbose_name = "Диаметр палки")
    stick_mass = models.PositiveIntegerField(verbose_name = "Масса палки")
    stick_length = models.PositiveIntegerField(verbose_name = "Длинна палки")
    stick_description = models.TextField(verbose_name = "Описание")
    stick_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображенрие")
    
    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Палки специальные'
        verbose_name_plural = 'Палки специальные'

    def __str__(self):
        return '{} ({})'.format(self.special_sticks_title, self.manufacturing_material)
    
class special_gas_facilities(models.Model):
    gase_greande_title = models.CharField(max_length=80, blank=True, verbose_name = "Название")
    gase_grenade_description = models.CharField(max_length=80, verbose_name = "Описание")
    gase_grenade_mass = models.PositiveIntegerField(verbose_name = "Масса")
    gase_grenade_diameter = models.PositiveIntegerField(verbose_name = "Диаметр")
    gase_grenade_length = models.PositiveIntegerField(verbose_name = "Длина")
    voleme_of_aerosol_cloud = models.CharField(max_length=100, verbose_name = "Объём аэйрозольного облака")
    temprature_range_of_application = models.CharField(max_length=100, blank=True, verbose_name = "Температурная область примениея")
    gase_grenade_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение")
    
    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Специальные газовые средства'
        verbose_name_plural = 'Специальные газовые средства'

    def __str__(self):
        return '{} ({})'.format(self.gase_greande_title, self.temprature_range_of_application)
    
class mobility_limiting_means(models.Model):
    handcuffs_title = models.CharField(max_length=80, blank=True, verbose_name = "Название")
    handcuffs_description = models.TextField(blank=True, verbose_name = "Описание")
    handcuffs_material = models.CharField(max_length=200, blank=True, verbose_name = "Материал")
    handcuffs_mass = models.PositiveIntegerField(verbose_name = "Масса")
    number_of_links = models.PositiveIntegerField(verbose_name = "Число колец")
    equipment = models.TextField(verbose_name = "Снаряжение")
    number_of_openings = models.CharField(max_length=160, verbose_name = "Число открытий/закрытий")
    rings_diameter = models.PositiveIntegerField(verbose_name = "диаметр колец")
    guarantee_period = models.PositiveIntegerField(verbose_name = "Период гарантии")
    handcuffs_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение")

    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Средства ограничения подвижности'
        verbose_name_plural = 'Средства ограничения подвижности'

    def __str__(self):
        return '{} ({})'.format(self.handcuffs_title, self.handcuffs_material)

class stun_devices(models.Model):
    stun_gun_title = models.CharField(max_length=80, blank=True, verbose_name = "Название")
    stun_gun_formfactor = models.CharField(max_length=100, blank=True, verbose_name = "Формфактор")
    operating_principle = models.CharField(max_length=100, verbose_name = "Принцип применения")
    electrodes = models.CharField(max_length=200, verbose_name = "Электроды")
    voltage = models.PositiveIntegerField(verbose_name = "Напряжение")
    efficiency = models.CharField(max_length=100, verbose_name = "Эффективная дальность")
    stun_gun_mass = models.PositiveIntegerField(verbose_name = "Масса")
    stun_gun_length = models.PositiveIntegerField(verbose_name = "Длина")
    stun_gun_height = models.PositiveIntegerField(verbose_name = "Высота")
    stun_gun_width = models.PositiveIntegerField(verbose_name = "Ширина")
    material = models.CharField(max_length=80, verbose_name = "Материал")
    power_methods = models.CharField(max_length=160, verbose_name = "Метод воздействия")
    charging = models.CharField(max_length=300, verbose_name = "Заряд")
    stun_gun_description = models.TextField(blank=True, verbose_name = "Описание")
    stun_gun_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение")

    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
       verbose_name = 'Электрошоковые устройства'
       verbose_name_plural = 'Электрошоковые устройства'

    def __str__(self):
        return '{} ({})'.format(self.stun_gun_title, self.stun_gun_formfactor)

class Vest(models.Model):
    vest_title=models.CharField(max_length=80, blank=True, verbose_name = "Название")
    body_material=models.CharField(max_length=80, verbose_name = "Материал основы")
    vests_color = models.CharField(max_length=100, verbose_name = "Цвет") #нафиг?
    vests_length = models.PositiveIntegerField(verbose_name = "Длина")
    vests_width = models.PositiveIntegerField(verbose_name = "Ширина")
    vest_mass = models.CharField(max_length=20, verbose_name = "Масса")
    vest_size = models.CharField(max_length=40, verbose_name = "Размер")
    materials = models.CharField(max_length=200, verbose_name = "Материал")
    protection_area = models.PositiveIntegerField(verbose_name = "Площадь защищённой поверхности")   #дм^2
    total_protection_area = models.PositiveIntegerField(verbose_name = "Общая площадь защиты")
    material_of_armor_elements = models.CharField(max_length=200, verbose_name = "Материал бронеэлемента")
    protection_class = models.CharField(max_length=40, blank=True, verbose_name = "Класс защиты")
    cloth = models.CharField(max_length=200, verbose_name = "Вид ткани")
    wearing_type = models.CharField(max_length=100, verbose_name = "Тип ношения")
    vest_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение")
    vest_description = models.TextField(verbose_name = "Описание")
    
    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
       verbose_name = 'Бронежилеты'
       verbose_name_plural = 'Бронежилеты'
                
    def __str__(self):
        return '{} ({})'.format(self.vest_title, self.protection_class)


class helmet(models.Model):
    helmet_title = models.CharField(max_length=100, blank=True, verbose_name = "Название")
    helmet_material = models.CharField(max_length=200, verbose_name = "МАтериал")
    helmet_hight = models.PositiveIntegerField(verbose_name = "Высота")
    helmet_width = models.PositiveIntegerField(verbose_name = "Ширина")
    helmet_total_protection_area = models.PositiveIntegerField(verbose_name = "Площадь защиты")
    helmet_size = models.CharField(max_length=100, verbose_name = "Размер")
    helmet_mass = models.PositiveIntegerField(verbose_name = "Массса")
    helmet_protection_class = models.CharField(max_length=80, blank=True, verbose_name = "Класс защиты")
    helmet_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение")
    helmet_description = models.TextField(blank=True, verbose_name = "Описание")

    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Шлемы'
        verbose_name_plural = 'Шлемы'
        
    def __str__(self):
        return '{} ({})'.format(self.helmet_title, self.helmet_protection_class)

class service_animals(models.Model):
    at1 = 0
    at2 = 1
    animals = (
        (at1, 'Собака'),
        (at2, 'Лощадь'),
    )
    animals_type = models.IntegerField(
        choices=animals,
        default = at1,
        verbose_name = "Вид"
    )
    kind = models.CharField(max_length=100, verbose_name = "Порода")
    purpose = models.CharField(max_length=200, blank=True, verbose_name = "Предназначение")
    average_hight = models.PositiveIntegerField(verbose_name = "Высота")
    average_lenght = models.PositiveIntegerField(blank=True, verbose_name = "Длина")
    jaws_strength = models.PositiveIntegerField(blank=True, verbose_name = "Сила челюсти")
    animals_description = models.TextField(blank=True, verbose_name = "Описание")
    animals_image = models.ImageField(upload_to=image_folder, blank=True, verbose_name = "Изображение")

    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Служебные животные'
        verbose_name_plural = 'Служебные животные'


    def __str__(self):
        return '{} ({})'.format(self.animals, self.purpose)