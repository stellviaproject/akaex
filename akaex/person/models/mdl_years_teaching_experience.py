from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from person.utils import APP_LABEL


class YearsTeachingExperience(BaseAkModel):
    
    person = models.ForeignKey(
                    "Person", 
                    on_delete=models.CASCADE,
                    verbose_name=_('person'),
                    db_column='id_persona')
    
    evaluations = models.ManyToManyField(
                        to="PersonEvaluationByCourse",
                        through="PersonEvaluations",
                        verbose_name=_('evaluations'),
                        db_column='evaluaciones'
                        )
    
    class Meta:
        verbose_name = _('Years teaching experience')
        verbose_name_plural = _('Years teaching experiences')
        db_table = f'{APP_LABEL.lower()}_tbd_annos_experiencia_docente'
        
    def __str__(self):
        return f"{_('Years teaching experience')}: {self.person}"
