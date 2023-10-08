from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from person.utils import APP_LABEL


class Evaluation(BaseAkModel):
    
    name = models.CharField(_('name'),unique=True, max_length=10, db_column='nombre')
    acronym = models.CharField(max_length=2, unique=True, verbose_name=_('acronym'), db_column='sigla')

    class Meta:
        verbose_name = _('Evaluation')
        verbose_name_plural = _('Evaluations')
        db_table = f'{APP_LABEL.lower()}_tbd_evaluacion'