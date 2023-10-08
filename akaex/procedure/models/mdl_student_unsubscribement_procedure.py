from datetime import date, datetime
from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from person.models import Person

from .mdl_procedure_reason import ProcedureReason
from .mdl_student_procedure import StudentProcedure

def procedure_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure-docs>/<movements>/<unsubscribe>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure-docs/movements/unsubscribe/{current_date}/{filename}'

    return path

class StudentUnsubscribementProcedure(BaseAkModel):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('name'))
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name=_('student procedure'), db_column='tramite docente')
    procedure_reason = models.ForeignKey(ProcedureReason, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name=_('procedure reason'), db_column='motivo tramite')
    unsubscribement_date = models.DateField(auto_now=True, null=True, blank=True, verbose_name=_('unsubscribement date'), db_column='fecha baja')
    center_date = models.DateField(null=True, blank=True,
                                   verbose_name=_('center date'), db_column='fecha centro')
    center_order = models.CharField(max_length=6, null=True, blank=True,
                                    verbose_name=_('center order'), db_column='orden centro')
    made = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_made',
                             verbose_name=_('made'), db_column='confeccionado')
    municipality_date = models.DateField(null=True, blank=True,
                                         verbose_name=_('municipality date'), db_column='fecha municipio')
    municipality_order = models.CharField(max_length=6, null=True, blank=True,
                                          verbose_name=_('municipality order'), db_column='orden municipio')
    approved_municipality = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_approved_municipality',
                                              verbose_name=_('approved municipality'), db_column='aprobado municipio')
    province_date = models.DateField(null=True, blank=True, default=None,
                                     verbose_name=_('province date'), db_column='fecha provincia')
    province_order = models.CharField(max_length=6, null=True, blank=True, default=None,
                                      verbose_name=_('province order'), db_column='orden provincia')
    approved_province = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='%(class)s_approved_province',
                                          verbose_name=_('approved province'), db_column='aprobado provincia')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    doc = models.FileField(upload_to=procedure_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('doc'), db_column='doc')

    class Meta:
        verbose_name = _('Student Unsubscribement Procedure')
        verbose_name_plural = _('Student Unsubscribement Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_baja_estudiante'

    def __str__(self):
        return f'Trámite de baja a estudiante: {self.student_procedure}'