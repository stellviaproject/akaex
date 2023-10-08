from core.models import (EmploymentRelationshipType, LaboralSectorType,
                         RelationshipType, SocialOriginType)
from django.db import models
from django.utils.translation import gettext as _
from person.models import Person
from procedure.nom_types import APP_LABEL
from core.generics.generic import BaseAkModel


class LegalTutor(BaseAkModel):
    
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('name'))
    legal_tutor = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('legal tutor'), db_column='tutor_legal')
    relationship = models.ForeignKey(RelationshipType, on_delete=models.CASCADE, verbose_name=_('relationship'), db_column='relacion')
    employment_relationship = models.ForeignKey(EmploymentRelationshipType, on_delete=models.CASCADE, verbose_name=_('employment relationship'), db_column='relacion_empleo')
    social_origin = models.ForeignKey(SocialOriginType, on_delete=models.CASCADE, verbose_name=_('social origin'), db_column='origen_social')
    workplace = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('workplace'), db_column='lugar_trabajo')
    laboral_sector = models.ForeignKey(LaboralSectorType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('laboral sector'), db_column='sector_laboral')
    formalized = models.BooleanField(default=True, verbose_name=_('formalized'), db_column='formalizado')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Legal Tutor')
        verbose_name_plural = _('Legal Tutors')
        db_table = f'{APP_LABEL.lower()}_tbd_tutor_legal'

    def __str__(self):
        return f'Tutor legal: {self.legal_tutor}'
