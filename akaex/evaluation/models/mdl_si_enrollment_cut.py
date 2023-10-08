from core import models as core_mdls
from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from evaluation.nom_types import APP_LABEL
from evaluation.nom_types import VERBOSE_NAMES as eval_vn
from evaluation.nom_types import VERBOSE_NAMES_PLURAL as eval_vnplural
from structure import models as structure_mdls
from study_plan import models as study_plan_mdls

from .mdl_enrollment_cut_educative_center import EnrollmentCutEducativeCenter
from .mdl_study_group import StudyGroup

vn_enrollment_cut = eval_vn.get("EnrollmentCutEducativeCenter")
vn_si_enrollment_cut = eval_vn.get("SIEnrollmentCut")
vn_atomic_total = eval_vn.get("atomic_total")

class SIEnrollmentCut(BaseAkModel):
    """
        It relates the Statistical Information (SI) in the form of a cube of 
        data related to the initial enrollment. Relates the atomic values ​​of
        the intersection of the data cube parameters.
    """
    enrollment_cut_educative_center = models.ForeignKey(
        EnrollmentCutEducativeCenter, on_delete=models.CASCADE,
        db_column="id_corte_matricula_centro_educacional",
        verbose_name=_(vn_enrollment_cut)
        )
    
    educative_center = models.ForeignKey(structure_mdls.EducativeCenter,
            on_delete=models.CASCADE, verbose_name=_("Educative Center"))
    
    education_level = models.ForeignKey(core_mdls.EducationLevelType,
        on_delete=models.CASCADE, db_column="id_nivel_educativo",
        verbose_name=_("Education Level"))
    
    education = models.ForeignKey(core_mdls.EducationType,
        on_delete=models.CASCADE, db_column="id_educacion",
        verbose_name=_("Education"))
    
    # tipificacion
    activity = models.ForeignKey(core_mdls.StructureActivityType,
        on_delete=models.CASCADE, db_column="id_actividad_estructura",
        verbose_name=_("Structure Activity"))
    
    course_type = models.ForeignKey(study_plan_mdls.CourseType,
        on_delete=models.CASCADE, db_column="id_tipo_curso",
        verbose_name=_("Course type"))
    
    school_situation = models.ForeignKey(core_mdls.SchoolSituationType,
        on_delete=models.CASCADE, db_column="id_situacion_escolar", 
        verbose_name=_("School Situation"))
    
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,
        db_column="id_grupo_estudio", verbose_name=_("Study Group"))
    
    academic_year = models.ForeignKey(study_plan_mdls.AcademicYear,
        on_delete=models.CASCADE, db_column="id_anno_academico",
        verbose_name=_("School Situation"))
    
    school_period = models.ForeignKey(study_plan_mdls.SchoolPeriod,
        on_delete=models.CASCADE, db_column="id_periodo_lectivo",
        verbose_name=_("School period"))
    
    speciality = models.ForeignKey(structure_mdls.Speciality,
        on_delete=models.CASCADE, db_column="id_especialidad",
        verbose_name=_("Speciality"))
    
    enrollment_condition = models.ForeignKey(core_mdls.RegimeType,
        on_delete=models.CASCADE, db_column="id_condicion_matricula",
        verbose_name=_("Enrollment Condition"))
    
    province = models.ForeignKey(core_mdls.Province,
        on_delete=models.CASCADE, db_column="id_provincia",
        verbose_name=_("Province"))
    
    municipality = models.ForeignKey(core_mdls.Municipality,
        on_delete=models.CASCADE, db_column="id_municipio",
        verbose_name=_("Municipality"))
    
    gender = models.ForeignKey(core_mdls.GenderType,
        on_delete=models.CASCADE, db_column="id_genero",
        verbose_name=_("Gender"))
    
    included = models.BooleanField(null=True, blank=True, db_column="incluido")
    
    disease = models.ForeignKey(core_mdls.DiseaseType,
            null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Disease"),
            db_column="id_enfermedad")
    
    center_type = models.ForeignKey(core_mdls.EducationalCenterType, 
        on_delete=models.CASCADE, verbose_name=_("center_type"),
        db_column="id_tipo_centro")
    
    turquino_plan = models.BooleanField(db_column="plan_turquino")
    
    is_mixed = models.BooleanField(default=False, 
        verbose_name=_('is_mixed'), db_column='mixta')
    
    is_rural = models.BooleanField(default=False,
        verbose_name=_('is_rural'), db_column='rural')
    
    vinculation = models.ForeignKey(core_mdls.VinculationType,
                                    null=True, blank=True,
            on_delete=models.CASCADE, verbose_name=_("Vinculation"),
            db_column="id_vinculacion")
    
    nationality = models.ForeignKey(core_mdls.NacionalityType, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        default=None, 
        verbose_name=_('nacionality'), 
        db_column='id_nacionalidad')
    
    atomic_total = models.IntegerField(db_column="total_atomico",
            verbose_name=_(vn_atomic_total)
            )

    class Meta:
        verbose_name = _(vn_si_enrollment_cut)
        verbose_name_plural = _(vn_si_enrollment_cut)
        db_table = f"{APP_LABEL.lower()}_tbd_ie_corte_matricula"
        
