from datetime import date, datetime
from core.generics.generic import BaseAkModel
from core.models import Municipality, Province
from django.db import models
from django.utils.translation import gettext as _
from person.models import Person
from procedure.nom_types import APP_LABEL
from structure.models import Structure

from .mdl_procedure_reason import ProcedureReason
from .mdl_student_procedure import StudentProcedure


def procedure_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure-docs>/<movements>/<transfer>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure-docs/movements/transfer/{current_date}/{filename}'

    return path


class StudentTransferProcedure(BaseAkModel):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('name'))
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.CASCADE, verbose_name=_('student procedure'), db_column='tramite_estudiante')
    center_date = models.DateField(verbose_name=_('center date'), db_column='fecha_centro')
    municipality_date = models.DateField(verbose_name=_('municipality date'), db_column='fecha_municipio')
    province_date = models.DateField(null=True, blank=True, verbose_name=_('province date'), db_column='fecha_provincia')
    center_order_number = models.CharField(max_length=6, verbose_name=_('center order number'), db_column='numero_orden_centro')  # TODO: add validator
    municipality_order_number = models.CharField(max_length=6, verbose_name=_('municipality order number'), db_column='numero_orden_municipio')  # TODO: add validator
    province_order_number = models.CharField(max_length=6, null=True, blank=True, verbose_name=_('province order number'), db_column='numero_orden_provincia')  # TODO: add validator
    center_approval_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='%(class)s_center_approval_person', verbose_name=_('center approval person'), db_column='persona_aprueba_en_centro')
    municipality_approval_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='%(class)s_municipality_approval_person', verbose_name=_('municipality approval person'), db_column='persona_aprueba_en_municipio')
    province_approval_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='%(class)s_province_approval_person', null=True, blank=True, verbose_name=_('province approval person'), db_column='persona_aprueba_en_provincia')
    procedure_reason = models.ForeignKey(ProcedureReason, on_delete=models.CASCADE, verbose_name=_('procedure reason'), db_column='motivo_tramite')
    destination_province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('destination province'), db_column='provincia_destino')
    destination_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('destination municipality'), db_column='municipio_destino')
    destination_center = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('destination center'), db_column='centro_destino')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    doc = models.FileField(upload_to=procedure_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('doc'), db_column='doc')

    class Meta:
        verbose_name = _('Student Transfer Procedure')
        verbose_name_plural = _('Student Transfer Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_traslado_estudiante'

    def __str__(self):
        return f'Trámite de traslado a estudiante: {self.student_procedure}'
