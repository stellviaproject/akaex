from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from person.utils import APP_LABEL


class PersonEvaluations(BaseAkModel):
    
    person_evaluation_by_course = models.ForeignKey(
                                        "PersonEvaluationByCourse",
                                        on_delete=models.CASCADE,
                                        verbose_name=_('person evaluation by course'),
                                        db_column='id_evaluacion_person_curso_escolar'
                                        )
    
    person_years_teaching_experience = models.ForeignKey(
                    "YearsTeachingExperience",
                    on_delete=models.CASCADE,
                    verbose_name=_('years teaching experience'),
                    db_column='id_annos_experiencia_docente'
                    )
    
    class Meta:
        verbose_name = _('Person evaluation')
        verbose_name_plural = _('Person evaluations')
        db_table = f'{APP_LABEL.lower()}_tbr_evaluacion_persona'
        
    def __str__(self):
        return f"{self.person_evaluation_by_course}"
