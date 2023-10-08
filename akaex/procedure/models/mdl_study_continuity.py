from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from person.models import Person
from structure.models import Speciality, ExternalCenter, Structure, SpecialityModality, EducativeCenter
from core.models import EducationalCenterType, OrganismType
from planning.models import Course

from .mdl_procedure_reason import ProcedureReason
from .mdl_student_procedure import StudentProcedure


class StudentStudyContinuityProcedure(BaseAkModel):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('name'))
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name=_('student procedure'), db_column='tramite docente')
    external_speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True, blank=True,
                                            verbose_name=_('external specialty'), db_column='especialidad externa')
    educational_center = models.ForeignKey(EducativeCenter, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                           verbose_name=_('center'), db_column='centro')
    external_center = models.ForeignKey(ExternalCenter, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                        verbose_name=_('external center'), db_column='centro_externo')
    forming_organism = models.ForeignKey(OrganismType, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                         verbose_name=_('forming organism'), db_column='forming_organism')
    speciality = models.ForeignKey(SpecialityModality, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                   verbose_name=_('speciality'), db_column='speciality')
    continuity_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                          verbose_name=_('course'), db_column='course')

    class Meta:
        verbose_name = _('Student Study Continuity')
        verbose_name_plural = _('Student Studies Continuity')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_continuidad_estudio'

    def __str__(self):
        return f'Trámite de continuidad de estudio a estudiante: {self.student_procedure}'