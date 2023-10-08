from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from structure.models import EducativeCenter
from .mdl_enrollment_registration_period import EnrollmentRegistrationPeriod
from evaluation.nom_types import APP_LABEL
from study_plan import models as study_plan_mdls
from structure import models as structure_mdls


class EnrollmentCutEducativeCenter(BaseAkModel):
    """ 
        It gathers all elements from the initial enrollment at the
        educative centers associated to a school course.
    """
    enrollment_cut = models.ForeignKey(EnrollmentRegistrationPeriod,
        on_delete=models.CASCADE, db_column="id_corte_matricula",
        verbose_name=_("enrollment cut"))
    
    educative_center = models.ForeignKey(EducativeCenter, on_delete=models.CASCADE,
        db_column="id_centro_educacional",verbose_name=_("Educative center"))
    
    speciality_configuration = models.ForeignKey(
        structure_mdls.SpecialityModalityAvtivityEducation,
        on_delete=models.CASCADE, default=None,
        verbose_name=_("SpecialityModalityAvtivityEducation"),
        db_column="id_especialidad_modalidad__actividad__educacion")
    
    date = models.DateField(db_column="fecha_corte_matricula",
        verbose_name="enrollment cut date")

    course_type = models.ForeignKey(study_plan_mdls.CourseType,
        on_delete=models.CASCADE, verbose_name=_("Course type"),
        db_column="id_tipo_curso", default=None)

    class Meta:
        verbose_name = _("Enrollment cut educative center")
        verbose_name_plural = _("Enrollment cut educative center")
        db_table = f"{APP_LABEL.lower()}_tbr_corte_matricula_centro_educacional"