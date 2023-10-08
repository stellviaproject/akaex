from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_evaluation_category import EvaluationCategory

Letra = "Letra"
Entero = "Entero"
Real = "Real"

CHOICES = ((Letra, "Letra"), (Entero, "Entero"), (Real, "Real"))


class QualificationRange(BaseAkModel):
    """Represents the ranges or scales that will be used in the qualification for the evaluations"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    value_type = models.CharField(max_length=10, verbose_name=_('value_type'), db_column='tipo_valor', choices=CHOICES)
    category = models.ForeignKey(EvaluationCategory, on_delete=models.CASCADE, verbose_name=_('category'), db_column='categoria')
    min_value = models.CharField(max_length=100, verbose_name=_('min_value'), db_column='valor_minimo')
    min_ref = models.IntegerField(verbose_name=_('min_ref'), db_column='referencia_minimo')
    max_value = models.CharField(max_length=100, verbose_name=_('max_value'), db_column='valor_maximo')
    max_ref = models.IntegerField(verbose_name=_('max_ref'), db_column='referencia_maximo')
    approv_value = models.CharField(max_length=100, verbose_name=_('approv_value'), db_column='valor_aprobado')
    approv_ref = models.IntegerField(verbose_name=_('approv_ref'), db_column='referencia_aprobado')
    decimals = models.IntegerField(verbose_name=_('decimals'), null=True, blank=True, db_column='decimales')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Qualification range')
        verbose_name_plural = _('Qualification ranges')
        db_table = f'{APP_LABEL.lower()}_tbd_rango_calificacion'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(QualificationRange)


