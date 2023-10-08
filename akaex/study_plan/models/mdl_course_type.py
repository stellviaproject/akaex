from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from auditlog.registry import auditlog
from study_plan.nom_types import APP_LABEL


class CourseType(BaseAkModel):
    """Represents the course types in which a study plan version can be taught"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Course type')
        verbose_name_plural = _('Course types')
        db_table = f'{APP_LABEL.lower()}_tbd_tipo_curso'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(CourseType)