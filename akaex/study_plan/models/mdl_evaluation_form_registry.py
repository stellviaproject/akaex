from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_subject_version import SubjectVersion
from .mdl_evaluation_way import EvaluationWay
from .mdl_evaluation_type import EvaluationType
from .mdl_evaluation_category import EvaluationCategory
from .mdl_qualification_range import QualificationRange


class EvaluationFormRegistry(BaseAkModel):
    """Relates the registries of the evaluation forms that are associated with a subject version"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    subject_version = models.ForeignKey(SubjectVersion, on_delete=models.CASCADE, verbose_name=_('subject version'), db_column='version_asignatura')
    evaluation_way = models.ForeignKey(EvaluationWay, on_delete=models.CASCADE, verbose_name=_('evaluation way'), db_column='via')
    evaluation_type = models.ForeignKey(EvaluationType, on_delete=models.CASCADE, verbose_name=_('evaluation type'), db_column='tipo_evaluacion')
    range = models.ForeignKey(QualificationRange, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('range'),  db_column='range')
    evaluation_category = models.ForeignKey(EvaluationCategory, on_delete=models.CASCADE, verbose_name=_('evaluation category'), db_column='categoria')
    amount = models.IntegerField(verbose_name=_('amount'), default=None, null=True, blank=True, db_column='cant_convocatorias')
    order = models.IntegerField(default=None, null=True, blank=True, verbose_name=_('order'))

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Evaluation form registry')
        verbose_name_plural = _('Evaluation form registries')
        db_table = f'{APP_LABEL.lower()}_tbd_registro_forma_evaluacion'

    def __str__(self):
        return f'{str(self.subject_version)} - {str(self.evaluation_way)}'

auditlog.register(EvaluationFormRegistry)