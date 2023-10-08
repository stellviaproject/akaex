from core.utils import APP_LABEL
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType


class ContractType(BaseType):
    """
        Used it on Procedure app
    """

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')
        db_table = f'{APP_LABEL.lower()}_tbn_tipo_contrato'
