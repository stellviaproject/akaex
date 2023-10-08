from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from core.generics.generic import BaseAkModel


class Course(BaseAkModel):

    name = models.CharField(max_length=100, verbose_name=_('name'))
    start_date = models.DateField(verbose_name=_('start_date'))
    end_date = models.DateField(verbose_name=_('end_date'))
    extension = models.DateField(blank=True, null=True, verbose_name=_('extension'))
    is_open = models.BooleanField(default=False, verbose_name=_('is_open'))
    description = models.TextField('Descripción', blank=True, default='')



    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f'{self.name}'