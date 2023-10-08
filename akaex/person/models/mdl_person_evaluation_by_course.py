from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from person.utils import APP_LABEL
from planning.models import Course


class PersonEvaluationByCourse(BaseAkModel):
    
    person = models.ForeignKey(
                            "Person",
                            on_delete=models.CASCADE,
                            verbose_name=_('person'),
                            db_column='id_persona'
                            )
    
    
    course = models.ForeignKey(
                            Course,
                            on_delete=models.CASCADE,
                            verbose_name=_('course'),
                            db_column='id_curso_escolar'
                            )
    
    evaluation = models.ForeignKey(
                            'Evaluation',
                            on_delete=models.CASCADE,
                            verbose_name=_('evaluation'),
                            db_column='id_evaluacion'
                            )

    class Meta:
        verbose_name = _('Person evaluation by course')
        verbose_name_plural = _('Person evaluations by course')
        db_table = f'{APP_LABEL.lower()}_tbr_persona_evaluacion_curso_escolar'
        unique_together = [['person', 'course', 'evaluation']]
        
    def __str__(self):
        return f"{_('Person evaluation by course')}: {self.person} - {self.course} - {self.evaluation}"
