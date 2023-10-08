from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan import managers
from study_plan.nom_types import APP_LABEL

from .mdl_rating_scale import RatingScale
from .mdl_scale_range import ScaleRange


class RatingScaleRange(BaseAkModel):
    rating_scale = models.ForeignKey(RatingScale, on_delete=models.CASCADE, verbose_name=_('rating scale'), db_column='rango_evaluacion')
    scale_range = models.ForeignKey(ScaleRange, on_delete=models.CASCADE, verbose_name=_('scale range'), db_column='rango_valor')
    is_approved = models.BooleanField(default=False, verbose_name=_('is approved'), db_column='aprobado')

    class Meta:
        verbose_name = _('Rating Scale Range')
        verbose_name_plural = _('Rating Scale Ranges')
        db_table = f'{APP_LABEL.lower()}_tbr_valor_evaluacion'


    def __str__(self):
        return self.rating_scale.name + ' -- ' + self.scale_range.name

auditlog.register(RatingScaleRange)