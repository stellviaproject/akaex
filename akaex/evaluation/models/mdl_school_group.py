from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import (APP_LABEL, GROUP_TYPES,
    GROUP_TYPES_DEFAULT, GROUP_STATES, GROUP_STATES_DEFAULT)
from study_plan.models import (AcademicYear, SchoolPeriod,
                               StudyPlanOrganization, SubjectVersion, SubjectType)
from planning.models import Course
from core.models import EducationType, StructureActivityType, EducationLevelType

from structure.models import EducativeCenter, OrganizatinalUnit, SpecialityModality
from .mdl_study_group import StudyGroup


class SchoolGroup(BaseAkModel):
    """
        It gathers school groups that are created in an educational center and 
        where students are enrolled according to their study plan.
    """
    educative_center = models.ForeignKey(
        EducativeCenter,
        on_delete=models.CASCADE,
        db_column='id_centro_educacional',
        verbose_name=_('Educative center')
    )

    organizational_unit = models.ForeignKey(
        OrganizatinalUnit,
        on_delete=models.CASCADE,
        db_column='id_unidad_organizativa',
        verbose_name=_('Organizational unit')
    )

    subject_version = models.ForeignKey(
        SubjectVersion,
        on_delete=models.CASCADE,
        db_column='id_version_asignatura',
        verbose_name=_('Subject version')
    )

    subject_type = models.ForeignKey(
        SubjectType,
        on_delete=models.CASCADE,
        db_column='id_tipo_asignatura',
        verbose_name=_('Subject type')
    )

    study_plan_organization = models.ForeignKey(
        StudyPlanOrganization,
        on_delete=models.CASCADE,
        db_column='id_organizacion_plan_estudio',
        verbose_name=_('Study plan organization')
    )

    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        db_column='id_anno_academico',
        verbose_name=_('Academic year')
    )

    school_period = models.ForeignKey(
        SchoolPeriod,
        on_delete=models.CASCADE,
        db_column='id_periodo_lectivo',
        verbose_name=_('School period')
    )

    study_group = models.ForeignKey(
        StudyGroup,
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        default=None,
        db_column='id_grupo_estudio',
        verbose_name=_('Study Group')
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        db_column='id_curso',
        verbose_name=_('Course')
    )

    group_type = models.CharField(
        max_length=100,
        default=GROUP_TYPES_DEFAULT,
        choices=GROUP_TYPES,
        db_column='tipo_grupo',
        verbose_name=_('Group type')
    )

    group_state = models.CharField(
        max_length=100,
        default=GROUP_STATES_DEFAULT,
        choices=GROUP_STATES,
        db_column='estado_grupo',
        verbose_name=_('Group state')
    )

#    education = models.ForeignKey(
#        EducationType,
#        on_delete=models.CASCADE,
#        null=True,
#        blank=True,
#        verbose_name=_('education_type'),
#        db_column='id_educacion')

#    activity = models.ForeignKey(
#        StructureActivityType,
#        on_delete=models.CASCADE,
#        null=True,
#        blank=True,
#        verbose_name=_('activity'),
#        db_column='id_actividad_estructura')

#    education_level_type = models.ForeignKey(
#        EducationLevelType,
#        on_delete=models.CASCADE,
#        null=True,
#        blank=True,
#        verbose_name=_('education_level_type'),
#        db_column='id_nivel_educativo')


#    speciality = models.ForeignKey(
#        SpecialityModality,
#        on_delete=models.CASCADE,
#        null=True,
#        blank=True,
#        verbose_name=_('speciality'),
#        db_column='id_especialidad')

    class Meta:
        verbose_name = _('School Group')
        verbose_name_plural = _('School Groups')
        db_table = f'{APP_LABEL.lower()}_tbd_grupo_docente'

    def __str__(self):
        return f'{self.name}'
