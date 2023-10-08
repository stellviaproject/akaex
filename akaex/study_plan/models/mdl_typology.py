from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_organizative_form import OrganizativeForm


class Typology(BaseAkModel):
    """Relates the typologies that the organizative forms that are associated with a subject version may have."""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    acronym = models.CharField(max_length=20, unique=True, null=False, verbose_name=_('acronym'), db_column='abreviatura')
    organizative_form = models.ForeignKey(OrganizativeForm, on_delete=models.CASCADE, verbose_name=_('organizative form'), db_column='forma')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Typology')
        verbose_name_plural = _('Typologies')
        db_table = f'{APP_LABEL.lower()}_tbd_tipologia'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(Typology)