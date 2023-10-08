from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from core.models import SchoolSituationType
from procedure.models import StudentRegistration
from study_plan.models import AcademicYear, SchoolPeriod
from .mdl_study_group import StudyGroup
from .mdl_enrollment_cut_educative_center import EnrollmentCutEducativeCenter
from evaluation.nom_types import APP_LABEL


class EnrollmentCutStudents(BaseAkModel):
    """
        It relates students and initial enrollment registers
    """
    enrollment_cut_educative_center = models.ForeignKey(EnrollmentCutEducativeCenter,
        on_delete=models.CASCADE, db_column="id_corte_matricula_centro_educacional",
        verbose_name=_("Enrollment cut educative center"))

    student_registration = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE,
        db_column="id_registro_estudiante", verbose_name=_("Student Registration"))
    
    school_situation = models.ForeignKey(SchoolSituationType, on_delete=models.CASCADE,
        db_column="id_situacion_escolar", verbose_name=_("School Situation"))
    
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,
        db_column="id_grupo_estudio", verbose_name=_("Study Group"))
    
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,
        db_column="id_anno_academico", verbose_name=_("Academic year"))
    
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE,
        db_column='id_periodo_lectivo', verbose_name=_('School period'))
    
    class Meta:
        verbose_name = _("Enrollment cut student")
        verbose_name_plural = _("Enrollment cut students")
        db_table = f"{APP_LABEL.lower()}_tbr_corte_matricula_estudiante"