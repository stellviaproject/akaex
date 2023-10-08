from core.generics.generic import BaseAkModel
from datetime import date, datetime, timezone
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from person.models import Person
from fuc.nom_types import APP_LABEL


class FUCPerson(BaseAkModel):

    person = models.ForeignKey(Person, on_delete=models.SET_NULL,
                                           default=None,
                                           null=True, blank=True,
                                           verbose_name=_('person'),
                                           db_column='person')



    class Meta:
        verbose_name = _('FUC Person')
        verbose_name_plural = _('FUC Persons')
        db_table = f'{APP_LABEL.lower()}_tbd_fuc_person'



    def __str__(self):
         return f'{str(self.name)}'


