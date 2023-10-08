from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL
from core.generics.generic import BaseAkModel
from procedure.models import StudentRegistration
from study_plan.models import EvaluationFormRegistry
from .mdl_school_group import SchoolGroup
from .mdl_evaluation_concept import EvaluationConcept
from .mdl_professor import Professor


class StudentEvaluation(BaseAkModel):
    """It gathers every associated evaluation for each estudent related to evaluation registery"""
    student_registration = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE,
        db_column="id_registro_estudiante", verbose_name=_("student registration"))
    
    school_group = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE,
        db_column="id_grupo_docente", verbose_name=_("school group"))
    
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,
        db_column="id_profesor", verbose_name=_("professor"), default=None)

    grade = models.CharField(max_length=10, null=True, blank=True, default=None, db_column="nota", verbose_name=_("grade"))

    reference_value = models.FloatField(db_column="valor_referencia", null=True, blank=True,  default=None,
        verbose_name=_("reference value"))
    
    evaluation_form_registry = models.ForeignKey(EvaluationFormRegistry, on_delete=models.CASCADE,
        db_column="id_registro_forma_evaluacion")
    
    evaluation_concept = models.ForeignKey(EvaluationConcept, on_delete=models.CASCADE,
        db_column="id_concepto_evaluacion", verbose_name=_("evaluation concept"))
    
    processor_person_id = models.UUIDField(null=True, default=None, blank=True,
        verbose_name=_('processor person id'), db_column='persona_procesa')
    
    
    class Meta:
        verbose_name = _('Student Evaluation')
        verbose_name_plural = _('Student Evaluations')
        db_table = f'{APP_LABEL.lower()}_tbr_evaluacion_estudiante'