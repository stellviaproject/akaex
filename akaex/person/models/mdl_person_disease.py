from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from .mdl_person import Person
from person.utils import APP_LABEL

class PersonDisease(BaseAkModel):
    """ It relates the person with a disease"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    disease = models.ForeignKey(DiseaseType, on_delete=models.CASCADE, verbose_name=_('disease'), db_column='enfermedad')

    def __str__(self):
        return f'{self.person} -- Disease: {self.disease_id}'

    class Meta:
        verbose_name = _('Person Disease')
        verbose_name_plural = _('Person Diseases')
        indexes = [
            models.Index(fields=['disease']),
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_persona_enfermedad'