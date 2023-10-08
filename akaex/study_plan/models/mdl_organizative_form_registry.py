from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_subject_version import SubjectVersion
from .mdl_typology import Typology
from .mdl_organizative_form import OrganizativeForm


class OrganizativeFormRegistry(BaseAkModel):
    """Relates the evaluation registries that are associated with a subject version"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    subject_version = models.ForeignKey(SubjectVersion, on_delete=models.CASCADE, verbose_name=_('subject version'), db_column='version_asignatura')
    typology = models.ForeignKey(Typology, on_delete=models.CASCADE, verbose_name=_('typology'), db_column='tipologia')
    organizative_form = models.ForeignKey(OrganizativeForm, on_delete=models.CASCADE, verbose_name=_('organizative form'), db_column='forma_organizativa')
    hours = models.IntegerField(verbose_name=_('hours'), db_column='hora_clase')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Organizative form registry')
        verbose_name_plural = _('Organizative form registries')
        db_table = f'{APP_LABEL.lower()}_tbd_registro_forma_organizativa'

    def __str__(self):
        return f'{str(self.subject_version)} - {str(self.organizative_form)}'

auditlog.register(OrganizativeFormRegistry)