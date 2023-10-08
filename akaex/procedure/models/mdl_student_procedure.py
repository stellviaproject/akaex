from core.generics.generic import BaseAkModel
from core.models import SchoolSituationType
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from person.models import Person
from procedure.nom_types import APP_LABEL, PROCEDURE_STATES
from structure.models import Structure

from .mdl_student_procedure_type import StudentProcedureType
from .mdl_student_registration import (StudentRegistration,
                                       person_photo_storage_path)


class StudentProcedure(BaseAkModel):
    
    student_registration = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, verbose_name=_('student registration'), db_column='registro_estudiante')
    second_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('second name'), db_column='segundo_nombre')
    first_last_name = models.CharField(max_length=100, verbose_name=_('first last name'), db_column='primer_apellido')
    second_last_name = models.CharField(max_length=100, verbose_name=_('second last name'), db_column='segundo_apellido')
    ci = models.CharField(max_length=11,
                          validators=[RegexValidator(r"^\d{11}$", message="The CI must have 11 characters")], verbose_name=_('id'), db_column='ci')
    student_procedure_type = models.ForeignKey(StudentProcedureType, on_delete=models.CASCADE, verbose_name=_('student procedure type'), db_column='tipo_tramite_estudiante')
    # school_course = models.ForeignKey(SchoolCourse, on_delete=models.CASCADE, null=True, blank=True)
    school_center = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('school center'), db_column='centro_escolar')
    # specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True, blank=True)
    # school_term = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, null=True, blank=True)
    # organization_current_plan = models.ForeignKey(OrganizationCurrentPlan, on_delete=models.CASCADE, null=True, blank=True)
    # school_course_type = models.ForeignKey(SchoolCourseType, on_delete=models.CASCADE, null=True, blank=True)
    # study_mode = models.ForeignKey(StudyModeType, on_delete=models.CASCADE, null=True, blank=True)
    school_situation = models.ForeignKey(SchoolSituationType, on_delete=models.CASCADE, verbose_name=_('school situation'), db_column='situacion_escolar')
    photo = models.ImageField(upload_to=person_photo_storage_path, default=None, null=True, blank=True, verbose_name=_('photo'), db_column='foto')
    processor_person_id = models.UUIDField(null=True, default=None, blank=True, verbose_name=_('processor person id'), db_column='persona_procesa')
    start_date = models.DateField(auto_now=True, verbose_name=_('start date'), db_column='fecha_inicio')
    end_date = models.DateField(null=True, blank=True, verbose_name=_('end date'), db_column='fecha_fin')
    state = models.CharField(max_length=50, choices= PROCEDURE_STATES, null=True, blank=True, verbose_name=_('status'), db_column='estado')
    previous_procedure = models.ForeignKey('StudentProcedure', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('previous procedure'), db_column='tramite_anterior')

    class Meta:
        verbose_name = _('Student Procedure')
        verbose_name_plural = _('Student Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_estudiante'

    def __str__(self):
        return f'Trámite a estudiante: {self.name}'