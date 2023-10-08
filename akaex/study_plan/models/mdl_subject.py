from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL


class Subject(BaseAkModel):
    """Represents the subjects"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    acronym = models.CharField(max_length=20, unique=True, null=False, verbose_name=_('acronym'), db_column='siglas')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
        db_table = f'{APP_LABEL.lower()}_tbd_asignatura'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(Subject)