from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_subject import Subject
from .mdl_organizative_form import OrganizativeForm
from .mdl_evaluation_type import EvaluationType


class SubjectVersion(BaseAkModel):
    """Relates the versions of the lective subjects that are taken"""
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('subject'), db_column='asignatura')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    is_average = models.BooleanField(default=False, verbose_name=_('is average'), db_column='promedia')
    thematic_plan = models.TextField(max_length=1000, null=True, blank=True, verbose_name=_('thematic plan'), db_column='plan_tematico')
    school_hours = models.IntegerField(null=True, blank=True, default=None, verbose_name=_('horas_clase'))
    organizative_form = models.ManyToManyField(OrganizativeForm, through='OrganizativeFormRegistry', through_fields=['subject_version', 'organizative_form'], verbose_name=_('organizative forms registries'), db_column='forma_organizativa')
    evaluation_form = models.ManyToManyField(EvaluationType, through='EvaluationFormRegistry', through_fields=['subject_version', 'evaluation_type'], verbose_name=_('evaluation forms registries'), db_column='forma_evaluacion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Subject version')
        verbose_name_plural = _('Subject versions')
        db_table = f'{APP_LABEL.lower()}_tbd_version_asignatura'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(SubjectVersion)