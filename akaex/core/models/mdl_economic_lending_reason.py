from core.utils import APP_LABEL
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType


class EconomicLendingReasonType(BaseType):
    
    """
        Used it on Procedure app
    """
    
    class Meta:
        verbose_name = _('Economic lending reason')
        verbose_name_plural = _('Economic lending reasons')
        db_table = f'{APP_LABEL.lower()}_tbn_motivo_prestacion_economica'