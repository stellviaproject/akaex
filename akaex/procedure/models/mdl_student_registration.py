from datetime import datetime

from core.generics.generic import BaseAkModel
from core.models import (EducationType, NacionalityType, PersonCategoryType,
                         RegimeType, SchoolSituationType,
                         StructureActivityType, EducationLevelType, SessionType)
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _
from evaluation.models import StudyGroup
from planning.models import Course
from procedure.models.mdl_teaching_status import TeachingStatus
from procedure.nom_types import *
from structure.models import EducativeCenter, SpecialityModality, OrganizatinalUnit
from study_plan.models import (AcademicYear, CourseType, SchoolPeriod,
                               StudyModality, StudyPlanOrganization,
                               StudyPlanVersion)

from .mdl_procedure_student import ProcedureStudent
from .mdl_way_entry import WayEntry


def person_photo_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure>/<photo>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure/photo/{current_date}/{filename}'

    return path


class StudentRegistration(BaseAkModel):
    
    student = models.ForeignKey(ProcedureStudent, on_delete=models.CASCADE, verbose_name=_('student'), db_column='id_estudiante')
    nationality = models.ForeignKey(NacionalityType, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name=_('nacionality'), db_column='id_nacionalidad')
    school_center = models.ForeignKey(EducativeCenter, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('school center'), db_column='id_centro_escolar')
    speciality = models.ForeignKey(SpecialityModality, on_delete=models.CASCADE, null=True, blank=True, db_column='id_especialidad')
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, null=True, blank=True, db_column='id_periodo_escolar')
    study_plan_organization = models.ForeignKey(StudyPlanOrganization, on_delete=models.CASCADE, null=True, blank=True, db_column='id_organizacion_plan_estudio')
    study_modality = models.ForeignKey(StudyModality, on_delete=models.CASCADE, null=True, blank=True, db_column='id_modalidad_estudio')
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE, null=True, blank=True, db_column='id_tipo_curso')
    category = models.ForeignKey(PersonCategoryType, on_delete=models.CASCADE, verbose_name=_('category'), db_column='id_categoria')
    state = models.ForeignKey(TeachingStatus, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('status'), db_column='id_estado')
    school_situation = models.ForeignKey(SchoolSituationType, on_delete=models.CASCADE, verbose_name=_('school situation'), db_column='id_situacion_escolar')
    enrollment_condition = models.ForeignKey(RegimeType, on_delete=models.CASCADE, null=True, blank=True, db_column='id_condicion_matricula')
    included = models.BooleanField(null=True, blank=True, verbose_name=_('included'), db_column='incluido')
    way_entry = models.ForeignKey(WayEntry, on_delete=models.CASCADE, null=True, blank=True, db_column='id_via_ingreso')
    enrollment_tome = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name=_('enrollment volume'), db_column='tomo_matricula')
    enrollment_folio = models.IntegerField(validators=[MaxValueValidator(99)], null=True, blank=True, verbose_name=_('enrollment folio'), db_column='folio_matricula')
    enrollment_number = models.CharField(max_length=6, null=True, blank=True, verbose_name=_('enrollment number'), db_column='numero_matricula')  # TODO: Add regex validator
    current_school_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('course'), db_column='id_curso')

    previous_procedure = models.ForeignKey('StudentProcedure', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('previous procedure'), db_column='id_tramite_anterior')
    procedure_type = models.CharField(max_length=100, choices=STUDENT_PROCEDURE_TYPE, default=CONST_PROCEDURE_NONE, verbose_name=_('procedure type'), db_column='tipo_tramite')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=True, blank=True, default=None, db_column='año_academico')
    photo = models.ImageField(upload_to=person_photo_storage_path, default=None, null=True, blank=True, verbose_name=_('photo'), db_column='foto')
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('study group'), db_column='id_grupo_estudio')
    study_plan_version = models.ForeignKey(StudyPlanVersion, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('study plan version'), db_column='id_version_plan_estudio')
    session = models.ForeignKey(SessionType, on_delete=models.CASCADE, null=True, blank=True, default=None, db_column='sesion')

    activity = models.ForeignKey(StructureActivityType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('activity'),
        db_column='id_actividad_estructura')

    education_type = models.ForeignKey(EducationType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('education_type'),
        db_column='id_educacion')

    education_level_type = models.ForeignKey(EducationLevelType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('education_level_type'),
        db_column='id_nivel_educativo')
    
    organizational_unit = models.ForeignKey(
        OrganizatinalUnit,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('organizational_unit'),
        db_column='id_unidad_organizativa')


    class Meta:
        verbose_name = _('Student Registration')
        verbose_name_plural = _('Student Registrations')
        db_table = f'{APP_LABEL.lower()}_tbd_registro_estudiante'

    def __str__(self):
        return f'Registro - {self.student}'
