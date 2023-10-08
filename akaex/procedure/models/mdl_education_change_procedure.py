from datetime import date, datetime

from core.generics.generic import BaseAkModel
from core.models import (EducationalCenterType, EducationLevelType,
                         EducationType, Municipality, OrganismType, Province,
                         SchoolSituationType, StructureActivityType)
from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from person.models import Person
from procedure.nom_types import APP_LABEL
from structure.models import ExternalCenter, Structure, SpecialityModality

from .mdl_procedure_reason import ProcedureReason
from .mdl_student_procedure import StudentProcedure



def procedure_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure-docs>/<movements>/<education-change>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure-docs/movements/education-change/{current_date}/{filename}'

    return path


class EducationChangeProcedure(BaseAkModel):
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.CASCADE, default=None, verbose_name=_('student procedure'), db_column='tramite_estudiante')
    center_date = models.DateField(verbose_name=_('center date'), default=date.today, db_column='fecha_centro')
    center_order = models.CharField(max_length=6) # TODO: add validator
    made_by_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='%(class)s_made_by_person', verbose_name=_('made by person'), default=None)

    destination_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=None)
    municipality_date_change = models.DateField(verbose_name=_('municipality_date'), default=None, db_column='fecha_municipio')
    municipality_order = models.CharField(max_length=6) # TODO: add validator
    municipality_approval_person = models.ForeignKey(Person, on_delete=models.CASCADE,  related_name='%(class)s_municipality_approval_person', verbose_name=_('municipality approval person'), default=None)

    destination_province = models.ForeignKey(Province, on_delete=models.CASCADE, default=None)
    province_date_change = models.DateField(verbose_name=_('province_date'),null=True, blank=True, default=None, db_column='fecha_provincia')
    province_order = models.CharField(max_length=6,null=True, blank=True, default='') # TODO: add validator
    province_approval_person = models.ForeignKey(Person, on_delete=models.CASCADE,  related_name='%(class)s_province_approval_person', verbose_name=_('province approval person'),null=True, blank=True, default=None)

    procedure_reason = models.ForeignKey(ProcedureReason, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name=_('procedure_reason'), default=None)

    forming_organism = models.ForeignKey(OrganismType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('forming_organism'), default=None)
    educational_center_type = models.ForeignKey(EducationalCenterType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('educational_center_type'), default=None)
    educational_center = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('educational_center'), default=None)
    external_center = models.ForeignKey(ExternalCenter, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('external_center'), default=None)
    education = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name=_('education'), default=None, null=True, blank=True,)
    speciality = models.ForeignKey(SpecialityModality, on_delete=models.CASCADE, null=True, blank=True, db_column='especialidad', default=None)
    typification = models.ForeignKey(StructureActivityType, on_delete=models.CASCADE, verbose_name=_('typification'), default=None, null=True, blank=True,)
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    school_situation = models.ForeignKey(SchoolSituationType, on_delete=models.CASCADE, verbose_name=_('school situation'), default=None)
    url_doc = models.CharField(max_length=255,verbose_name=_('documento'), null=True, blank=True, default=None, db_column='documento') # TODO: add validator
    doc = models.FileField(upload_to=procedure_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('doc'), db_column='doc')

    class Meta:
        verbose_name = _('Education Change')
        verbose_name_plural = _('Education Changes')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_cambio_educacion_estudiante'

    def __str__(self):
        return f'Trámite cambio de educación a estudiante: {self.student_procedure}'
