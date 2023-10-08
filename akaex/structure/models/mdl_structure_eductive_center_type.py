from django.utils.translation import gettext_lazy as _
from django.db import models
from structure.managers import EcducativeCenterManager
from structure.models.mdl_structure import Structure


class EducativeCenter(Structure):
    objects = EcducativeCenterManager()
    class Meta:
        proxy=True
        verbose_name = _('Educative Center')
        verbose_name_plural = _('Educative Centers')