from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL
from planning.models import Course
from person.models import Person
from study_plan.models import (StudyPlanOrganization, SubjectVersion, AcademicYear,
                                SchoolPeriod, EvaluationFormRegistry)
from structure.models import SpecialityModalityAvtivityEducation
from .mdl_evaluation_concept import EvaluationConcept
from .mdl_student_evaluation import StudentEvaluation
from procedure.models import StudentRegistration


class FinalGradeRegistry(BaseAkModel):

    person = models.ForeignKey(Person, on_delete=models.CASCADE,
        db_column='id_persona', verbose_name=_('person'))
    
    student_registration = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE,
        db_column="id_registro_estudiante", verbose_name=_("student registration"))
    
    student_evaluation = models.ForeignKey(StudentEvaluation, on_delete=models.CASCADE, null=True, blank=True,default=None,
        db_column='id_evaluacion_estudiante', verbose_name=_('student evaluation'))
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='id_curso',
        verbose_name=_('course'))
    
    study_plan_organization = models.ForeignKey(StudyPlanOrganization, on_delete=models.CASCADE,
        db_column='id_organizacion_plan_estudio')
    
    speciality_configuration = models.ForeignKey(SpecialityModalityAvtivityEducation,
        on_delete=models.CASCADE, verbose_name=_('speciality configuration'), 
        db_column='id_configuracion_especialidad')
    
    subject_version = models.ForeignKey(SubjectVersion, on_delete=models.CASCADE,
        db_column='id_version_asignatura', verbose_name=_('subject version'))
    
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,
        db_column='id_anno_academico', verbose_name=_('academic year'))
    
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE,
        db_column='id_periodo_lectivo', verbose_name=_('school period'))
    
    processor_person_id = models.UUIDField(null=True, default=None, blank=True,
        verbose_name=_('processor person id'), db_column='persona_procesa')
    
    grade = models.CharField(max_length=10, db_column="nota", verbose_name=_("grade"))

    reference_value = models.PositiveIntegerField(db_column="valor_referencia", 
        verbose_name=_("reference value"))
    
    evaluation_form_registry = models.ForeignKey(EvaluationFormRegistry, on_delete=models.CASCADE,
        db_column="id_registro_forma_evaluacion")
    
    evaluation_concept = models.ForeignKey(EvaluationConcept, on_delete=models.CASCADE,
        db_column="id_concepto_evaluacion", verbose_name=_("evaluation concept"))
    
    evaluation_status = models.BooleanField(default=False, verbose_name=_('evaluation status'),
        db_column='estado_evaluacion')
    

    class Meta:
        verbose_name = _('Final grade registry')
        verbose_name_plural = _('Final grade registries')
        db_table = f'{APP_LABEL.lower()}_tbd_registro_nota_final'
        permissions = [
            ("add_historical_evaluation", _("Can add historical evaluation")),
            ("add_final_evaluation", _("Can add final evaluation")),
            ("view_center_organization_group", _("Can view center organization group")),
            ("add_center_organization_group", _("Can add center organization group")),
            ("delete_center_organization_group", _("Can delete center organization group")),

        ]
