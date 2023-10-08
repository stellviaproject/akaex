from datetime import datetime
from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from structure.models import ExternalCenter, Structure, SpecialityModality
from core.models import Municipality, Province, OrganismType, SpecialityType

from .mdl_procedure_reason import ProcedureReason
from .mdl_student_procedure import StudentProcedure
from .mdl_way_entry import WayEntry

def procedure_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure-docs>/<placement>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure-docs/placement/{current_date}/{filename}'

    return path

class StudentPlacement(BaseAkModel):
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name=_('student procedure'), db_column='tramite_estudiante')
    origin_center = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name=_('origin center'), db_column='centro_origen')
    # way_of_entry = models.ForeignKey(WayEntry, on_delete=models.SET_NULL, null=True, blank=True,
    #                                  verbose_name=_('way of entry'), db_column='via_ingreso')
    procedure_reason = models.ForeignKey(ProcedureReason, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name=_('procedure reason'), db_column='motivo_tramite')
    external_center = models.ForeignKey(ExternalCenter, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name=_('external center'), db_column='centro_externo')
    origin_municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                            verbose_name=_('origin municipality'), db_column='municipio_origen')
    origin_province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True,
                                        default=None, verbose_name=_('origin province'), db_column='provincia_origen')
    organism = models.ForeignKey(OrganismType, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                 verbose_name=_('forming organism'), db_column='organismo')
    speciality = models.ForeignKey(SpecialityModality, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                                   verbose_name=_('speciality'), db_column='especialidad')

    origin = models.CharField(max_length=500, null=True, blank=True, default=None)

    doc = models.FileField(upload_to=procedure_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('doc'), db_column='doc')

    class Meta:
        verbose_name = _('Student Placement')
        verbose_name_plural = _('Student Placements')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_ubicacion_estudiante'
        permissions = [
            ("add_procedure_placement_by_register", _("Can procedure placement by register")),
            ("view_procedure_placement_by_register", _("Can view procedure placement by register")),
            ("change_procedure_placement_by_register", _("Can procedure placement by register")),
            ("delete_procedure_placement_by_register", _("Can procedure_placement by register")),

            ("add_procedure_placement_by_transfer", _("Can procedure placement by transfer")),
            ("view_procedure_placement_by_transfer", _("Can view procedure placement by transfer")),
            ("change_procedure_placement_by_transfer", _("Can procedure placement by transfer")),
            ("delete_procedure_placement_by_transfer", _("Can procedure_placement by transfer")),

            ("add_procedure_placement_by_education_change", _("Can procedure placement by education change")),
            ("view_procedure_placement_by_education_change", _("Can view procedure placement by education change")),
            ("change_procedure_placement_by_education_change", _("Can procedure placement by education change")),
            ("delete_procedure_placement_by_education_change", _("Can procedure_placement by education change")),

            ("add_procedure_placement_by_study_continuity", _("Can procedure placement by study continuity")),
            ("view_procedure_placement_by_study_continuity", _("Can view procedure placement by study continuity")),
            ("change_procedure_placement_by_study_continuity", _("Can procedure placement by study continuity")),
            ("delete_procedure_placement_by_study_continuity", _("Can procedure_placement by study continuity")),

            ("add_procedure_placement_by_unenrollment", _("Can procedure placement by unenrollment")),
            ("view_procedure_placement_by_unenrollment", _("Can view procedure placement by unenrollment")),
            ("change_procedure_placement_by_unenrollment", _("Can procedure placement by unenrollment")),
            ("delete_procedure_placement_by_unenrollment", _("Can procedure_placement by unenrollment")),

        ]

    def __str__(self):
        return f'Trámite de ubicación a estudiante: {self.student_procedure}'
