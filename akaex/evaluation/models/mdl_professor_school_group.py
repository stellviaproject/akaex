from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL
from .mdl_school_group import SchoolGroup
from .mdl_professor import Professor


class ProfessorSchoolGroup(BaseAkModel):
    """It gathers all professors that teach in a school group"""
    school_group = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE,
        db_column="id_grupo_docente", verbose_name=_("school group"))
    
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,
        db_column="id_profesor", verbose_name=_("professor"))
    
    principal = models.BooleanField(db_column="principal", verbose_name=_("principal"))

    class Meta:
        verbose_name = _('Professor School Group')
        verbose_name_plural = _('Professors School Groups')
        db_table = f'{APP_LABEL.lower()}_tbr_profesor__grupo_docente'

    def __str__(self):
        professor_name = self.professor.worker.full_name
        principal = self.principal
        output = f"{professor_name}, {self.school_group}"
        
        if principal:
            output += f", {_('principal')}" 
        
        return output