from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL


class ScaleRange(BaseAkModel):
    min = models.DecimalField(decimal_places=2, max_digits=6)
    max = models.DecimalField(decimal_places=2, max_digits=6)
    value = models.IntegerField(verbose_name=_('value'), db_column='valor')
    acronym = models.CharField(max_length=20, unique=True, null=False, verbose_name=_('acronym'), db_column='siglas')
    qualification_type = models.ForeignKey(Nomenclator, on_delete=models.CASCADE,
                                           limit_choices_to={'type': NOM_TYPE['QUALIFICATION_TYPE']},
                                           verbose_name=_('qualification type'), db_column='tipo_calificacion')
    class Meta:
        verbose_name = _('Scale Range')
        verbose_name_plural = _('Scale Ranges')
        ordering = ['min']
        db_table = f'{APP_LABEL.lower()}_tbd_rango_valor'
        # unique_together = [('min', 'max')]

auditlog.register(ScaleRange)
