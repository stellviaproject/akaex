from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class ValidatedType(BaseType):

    STATUS = (
        ('YES', _('Yes')),
        ('NOT', _('No')),
    )
    name = models.CharField(_('validated'),
                                 max_length=50,
                                 choices=STATUS,
                                 default='NOT',
                                 db_column='nombre')

    class Meta:
        verbose_name = _('Validated')
        verbose_name_plural = _('Validated')

