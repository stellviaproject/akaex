from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db import models
from colorfield.fields import ColorField
from django.utils.text import slugify
from django.db.models.signals import pre_save

from guardian.models import UserObjectPermissionBase
from guardian.models import GroupObjectPermissionBase

from location_field.models.plain import PlainLocationField
from treenode.models import TreeNodeModel

from core.generics.generic import BaseAkModel
from core.tree_node_patch import AkTreeNodeModel
from structure.managers import StructureManager
from core.models import *
from structure.models.mdl_building import Building
from structure.models.mdl_responsibility import Responsibility
from structure.models.mdl_characteristics import Characteristics
from structure.models.mdl_speciality_modality_avtivity_education import SpecialityModalityAvtivityEducation
from structure.models.mdl_structure_type import StructureType
from structure.models.mdl_speciality import Speciality

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog


from structure.utils import APP_LABEL

class Structure(BaseAkModel, AkTreeNodeModel):
    """Represents the structures"""
    history = AuditlogHistoryField()

    treenode_display_field = 'name'

    type = models.ForeignKey(StructureType, on_delete=models.CASCADE, verbose_name=_("Type"), db_column='tipo')

    # @Todo Revisar campo category
    # category = models.ForeignKey(
    #     StructureCategory, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(CountryType, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('country'), db_column='id_pais')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_("Province"), db_column='id_provincia')
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_("Municipality"), db_column='id_municipio')
    building = models.ManyToManyField(
        Building, through='StructureBuilding', verbose_name=_('building'))
    responsibility = models.ManyToManyField(
        Responsibility, through='StructureResponsibility', verbose_name=_('responsibility'))
    characteristics = models.ManyToManyField(
        Characteristics, through='StructureCharacteristics', verbose_name=_('characteristics'))
    #address = models.CharField('Dirección', max_length=255)
    address = models.TextField('Dirección', blank=True, default='', db_column='direccion')
    #popular_council = models.CharField(max_length=255, null=True, blank=True)

    popular_council = models.ForeignKey(PopularCouncilType, on_delete=models.SET_NULL, null=True, verbose_name=_('popular_council'), db_column='id_consejo_popular')
    location_type = models.ForeignKey(LocationType, on_delete=models.SET_NULL, null=True, verbose_name=_('location_type'), db_column='id_localidad')
    # education_level_type = models.ManyToManyField(EducationLevelType, blank=True, default=None)
    # education_type = models.ManyToManyField(EducationType, blank=True, default=None)
    educational_center_type = models.ForeignKey(
        EducationalCenterType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('educational_center_type'), db_column='id_centro_eduacional')
    # organism_type = models.ForeignKey(
    #     OrganismType, on_delete=models.SET_NULL, null=True, blank=True)
    session_type = models.ForeignKey(
        SessionType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('session_type'), db_column='id_sesion')
    regime = models.ForeignKey(RegimeType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('regime'), db_column='id_regimen')
    location = PlainLocationField(based_fields=['address'], zoom=7, null=True, verbose_name="Coordenadas")
    code = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name=_('code'), db_column='codigo')
    health_council = models.ForeignKey(HealthCouncilType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('health_council'), db_column='id_consejo_salud')
    attention_area = models.ForeignKey(AttentionAreaType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('attention_area'), db_column='id_area_atencion')
    # main_activity = models.ManyToManyField(StructureActivityType, blank=True)
    plan_turquino = models.BooleanField(default=False)
    university_seat = models.BooleanField(default=False, verbose_name=_('university_seat'), db_column='sede_universitaria')
    # library = models.BooleanField(default=True, blank=False)
    # materials_disabled_students = models.BooleanField(default=False)
    # population = models.BigIntegerField(default=0)
    email = models.EmailField('Correo electrónico', null=True, blank=True, db_column='correo')
    is_mixed = models.BooleanField(default=False, verbose_name=_('is_mixed'), db_column='mixta')
    is_rural = models.BooleanField(default=False, verbose_name=_('is_rural'), db_column='rural')
    is_closed = models.BooleanField(default=False, verbose_name=_('is_closed'), db_column='cerrada')
    description = models.TextField('Descripción', blank=True, default='', db_column='descripcion')
    phone = models.CharField(
        'Teléfono móvil',
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message=_("Phone number must be entered in the format '123456789'")
            )],
        db_column='telefono_movil'
    )
    main_phone = models.CharField(
        'Teléfono fijo',
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message=_("Phone number must be entered in the format '123456789'")
            )],
        db_column='telefono_fijo'
    )
    extra_field = models.JSONField(blank=True, null=True, verbose_name=_('extra_field'))
    is_validated = models.BooleanField(default=False, verbose_name=_('is_validated'), db_column='validado')
    specialities = models.ManyToManyField(Speciality, through='evaluation.EducativeCenterSpeciality', blank=True, verbose_name=_('speciality'))
    category = models.ForeignKey(StructureCategoryType, on_delete=models.SET_NULL, null=True, verbose_name=_('category'), db_column='id_categoria_estructura')
    vinculation = models.ForeignKey(VinculationType, on_delete=models.SET_NULL, null=True, verbose_name=_('vinculation'), db_column='id_vinculacion')

    objects = StructureManager()

    class Meta:
        verbose_name = _('Structure')
        verbose_name_plural = _('Structures')
        permissions = [
            ("add_school", _("Can add school")),
            ("view_school", _("Can view school")),
            ("change_school", _("Can change school")),
            ("delete_school", _("Can delete school")),
            ("view_map", _("Can view the map")),
            ("admin", _("Can manager structure permissions")),
            ("view_not_educational_worker_school", _("Can view not_educational_worker")),
            ("add_not_educational_worker_school", _("Can add not_educational_worker")),
            ("change_not_educational_worker_school", _("Can change not_educational_worker")),
            ("delete_not_educational_worker_school", _("Can delete not_educational_worker")),
            ("view_educational_worker_school", _("Can view educational_worker")),
            ("add_educational_worker_school", _("Can add educational_worker")),
            ("change_educational_worker_school", _("Can change educational_worker")),
            ("delete_educational_worker_school", _("Can delete educational_worker")),
            ("view_student_school", _("Can view student")),
            ("add_student_school", _("Can add student")),
            ("change_student_school", _("Can change student")),
            ("delete_student_school", _("Can delete student")),
            ("view_student_group_school", _("Can view student_group")),
            ("add_student_group_school", _("Can add student_group")),
            ("change_student_group_school", _("Can change student_group")),
            ("delete_student_group_school", _("Can delete student_group")),
        ]
        indexes = [
            models.Index(fields=('name', 'code', ))
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_estructura'

    @classmethod
    def async_update_tree(cls):
        """ This function call an async task to update the tree
        """
        from structure.tasks import async_update_tree_node
        async_update_tree_node.delay()

    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    # Also we change this function to async update the tree
    @classmethod
    def update_tree(cls):
        cls.async_update_tree()


def update_code_structure(sender, instance, **kwargs):
    try:
        code = str(instance.code)
        if not code == '':
            cadena = code.split("-")
            head = Province.objects.get(pk=instance.province_id).code + Municipality.objects.get(pk=instance.municipality_id).code
            body = '-' + cadena[-1] if len(cadena) > 0 else ''
            instance.code = head + body

    except Exception as ex:
        raise Exception("Error update code in structure")


pre_save.connect(update_code_structure, sender=Structure)

auditlog.register(Structure)
