from core.utils import APP_LABEL
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType


class LaboralFunctionType(BaseType):
    
    """
        Used it on Procedure app
    """
    
    class Meta:
        verbose_name = _('Laboral function')
        verbose_name_plural = _('Laboral functions')
        db_table = f'{APP_LABEL.lower()}_tbn_funcion_laboral'