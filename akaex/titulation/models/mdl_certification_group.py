from core.generics.generic import BaseAkModel
from datetime import date, datetime, timezone
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from structure.models import Structure, OrganizatinalUnit, SpecialityModalityAvtivityEducation, EducativeCenter
from planning.models import Course
from study_plan.models import CourseType


def certified_nominal_relationships_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<titulation-docs>/<certified_nominal_relationship>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'titulation-docs/certified-nominal-relationships/{current_date}/{filename}'

    return path


class CertificationGroup(BaseAkModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, verbose_name=_('course'), db_column='id_curso')
    educatinal_center = models.ForeignKey(EducativeCenter, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='certification_groups', verbose_name=_('educatinal_center'), db_column='id_centro_educativo')
    organizatinal_unit = models.ForeignKey(OrganizatinalUnit, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='certification_groups', verbose_name=_('organizatinal_unit'), db_column='id_unidad_organizacional')
    date = models.DateField(null=True, blank=True, verbose_name=_('date'), db_column='fecha')
    speciality_configuration = models.ForeignKey(SpecialityModalityAvtivityEducation, on_delete=models.SET_NULL, null=True, blank=True, default=None,  verbose_name=_('speciality_configuration'), db_column='configuracion_especialidad')
    course_type = models.ForeignKey(CourseType, null=True, blank=True, default=None, on_delete=models.SET_NULL, verbose_name=_('course_type'), db_column='tipo_curso')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    doc = models.FileField(upload_to=certified_nominal_relationships_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('document'), db_column='documento')


    class Meta:
        verbose_name = _('Certification Group')
        verbose_name_plural = _('Certification Groups')
        db_table = f'{APP_LABEL.lower()}_tbd_grupo_certificacion'
        unique_together = ('name', 'speciality_configuration', 'educatinal_center', 'course')


    def __str__(self):
         return f'{str(self.name)}'


