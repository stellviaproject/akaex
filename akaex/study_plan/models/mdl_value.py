from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_qualification_range import QualificationRange


class Value(BaseAkModel):
    """Reference the values that are typified as "letters". """
    reference_value = models.IntegerField(verbose_name=_('reference_value'), db_column='valor_referencia')
    range = models.ForeignKey(QualificationRange, on_delete=models.CASCADE, verbose_name=_('range'), db_column='rango')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Value')
        verbose_name_plural = _('Values')
        db_table = f'{APP_LABEL.lower()}_tbd_valor'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(Value)