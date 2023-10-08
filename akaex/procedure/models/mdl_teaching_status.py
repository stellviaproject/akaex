from core.models import BaseType
from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL, TEACHING_STATUS_TYPE


class TeachingStatus(BaseType):
    name = models.CharField(max_length=100, default="Teaching Status",
                                       verbose_name=_('name'), db_column='nombre')
    color = ColorField(default='#FFFFFF', verbose_name=_('color'))
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    type = models.CharField(max_length=100, choices=TEACHING_STATUS_TYPE, default="type", verbose_name=_('type'), db_column='tipo')

    class Meta:
        verbose_name = _('Teaching Status')
        verbose_name_plural = _('Teaching Statuses')
        db_table = f'{APP_LABEL.lower()}_tbn_estado_docente'

    def __str__(self):
        return self.name
