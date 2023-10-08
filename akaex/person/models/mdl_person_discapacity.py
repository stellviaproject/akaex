from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from .mdl_person import Person
from person.utils import APP_LABEL

class PersonDiscapacity(BaseAkModel):
    """ It relates the person with a discapacity"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    discapacity = models.ForeignKey(DiscapacityType, on_delete=models.CASCADE, verbose_name=_('discapacity'), db_column='discapacidad')

    def __str__(self):
        return f'{self.person} -- Discapacity: {self.discapacity_id}'

    class Meta:
        verbose_name = _('Person Discapacity')
        verbose_name_plural = _('Person Discapacities')
        indexes = [
            models.Index(fields=['discapacity']),
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_persona_discapacidad'