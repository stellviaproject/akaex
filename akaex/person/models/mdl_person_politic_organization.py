from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from .mdl_person import Person
from person.utils import APP_LABEL

class PersonPoliticOrganization(BaseAkModel):
    """ It relates the person with a politic organization"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    organization = models.ForeignKey(PoliticOrganizationType, on_delete=models.CASCADE, verbose_name=_('organization'), db_column='organizacion')

    def __str__(self):
        return f'{self.person} -- Organization: {self.organization_id}'

    class Meta:
        verbose_name = _('Person Politic Organization')
        verbose_name_plural = _('Person Politic Organizations')
        indexes = [
            models.Index(fields=['organization']),
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_persona_organizacion_politica'