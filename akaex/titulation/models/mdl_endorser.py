from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import TitleConfiguration, EndorserResponsibilityTitleConfiguration, CertificationGroup
from person.models import Person


class Endorser(BaseAkModel):
    worker = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('worker'), db_column='trabajador')
    certification_group = models.ForeignKey(CertificationGroup, default=None, null=True, on_delete=models.CASCADE, verbose_name=_('certification_group'), db_column='grupo_certificacion')
    variable = models.CharField(max_length=50, verbose_name=_('variable'), db_column='variable')
    resp_endorser = models.ForeignKey(EndorserResponsibilityTitleConfiguration, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('responsibility'), db_column='responsabilidad_avaladora')

    class Meta:
        verbose_name = _('Endorser')
        verbose_name_plural = _('Endorsers')
        db_table = f'{APP_LABEL.lower()}_tbd_avalador'

    def __str__(self):
        return f'{str(self.worker)}'