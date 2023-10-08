from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL


class EvaluationConcept(BaseAkModel):
    
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_('description'),
        db_column='descripcion')
    
    acronym = models.CharField(
        max_length=3,
        default=None,
        verbose_name=_('acronym'),
        db_column='siglas')

    class Meta:
        verbose_name = _('Evaluation Concept')
        verbose_name_plural = _('Evaluation Concepts')
        db_table = f'{APP_LABEL.lower()}_tbd_concepto_evaluacion'