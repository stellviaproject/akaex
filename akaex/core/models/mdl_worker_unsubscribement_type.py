from core.utils import APP_LABEL
from django.db import models
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType
from core import nom_types as core_nom_types


class WorkerUnsubscribementType(BaseType):

    """
        Used it on Procedure app
        List the types of a worker unsubscribement
    """
    type = models.CharField(max_length=100, unique=False,
                            choices=((core_nom_types.CONST_WORKER_STATE_UNSUBSCRIBED,
                                      _(core_nom_types.CONST_WORKER_STATE_UNSUBSCRIBED)),
                                     (core_nom_types.CONST_WORKER_UNSUBSCRIBEMENT_TRANSFER,
                                      _(core_nom_types.CONST_WORKER_UNSUBSCRIBEMENT_TRANSFER))
                                     ),
                            default=core_nom_types.CONST_WORKER_STATE_UNSUBSCRIBED,
                            verbose_name=_('type'), db_column='tipo')

    class Meta:
        verbose_name = _('Worker unsubscribement type')
        verbose_name_plural = _('Worker unsubscribement types')
        db_table = f'{APP_LABEL.lower()}_tbn_tipo_baja'
