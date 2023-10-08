from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL


class BaseType(BaseAkModel):
    type = models.CharField(max_length=100, unique=True, verbose_name=_('type'), db_column='tipo')
    description = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Base')
        verbose_name_plural = _('Bases')
        abstract = True
        indexes = [
            models.Index(fields=['name', 'type']),
        ]

    def save(self, *args, **kwargs):
        try:
            if not self.type:
                type = (self.__class__.__name__ + '_' + self.name).strip().upper()
                self.type = type.replace(" ", "_")
                try:
                    if self.municipality:
                        short_name = self.municipality.short_name + '_' + self.province.short_name
                        type = (self.__class__.__name__ + '_' + self.name + '_' + short_name).strip().upper()
                        self.type = type.replace(" ", "_")

                except AttributeError as e:
                    pass

            super(BaseType, self).save(*args, **kwargs)

        except IntegrityError as e:
            raise ('El elemento que trata de registrar ya existe')

