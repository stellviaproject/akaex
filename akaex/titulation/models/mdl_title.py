from core.generics.generic import BaseAkModel
from datetime import date, datetime, timezone
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import TitleConfiguration, StudentCertificationGroup, Endorser
from person.models import Person


def titles_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<titulation-docs>/<titles>/<current_date>/<filename>
    """

    cert_group=instance.student.certification_group
    path = f'titulation-docs/titles/{cert_group}/{filename}'

    return path


class Title(BaseAkModel):
    title_configuration = models.ForeignKey(TitleConfiguration, on_delete=models.CASCADE, verbose_name=_('title_configuration'), db_column='configuracion_titulo')
    student = models.ForeignKey(StudentCertificationGroup, on_delete=models.CASCADE, verbose_name=_('student'), db_column='estudiante')
    status = models.BooleanField(null=True, blank=True, verbose_name=_('status'), choices=[(True, 'Emitido'), (False, 'No emitido')], default=None, db_column='tipo_dato')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    level = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('level'), db_column='nivel')
    education = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('education'), db_column='educacion')
    tipification = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('tipification'), db_column='tipificacion')
    speciality = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('speciality'), db_column='especialdad')
    tome_RMG = models.CharField(max_length=10, null=True, blank=True, default=None, verbose_name=_('tome_RMG'), db_column='tomo_RMG')
    folio_RMG = models.CharField(max_length=10, null=True, blank=True, default=None, verbose_name=_('folio_RMG'), db_column='folio_RMG')
    number_RMG = models.CharField(max_length=10, null=True, blank=True, default=None, verbose_name=_('number_RMG'), db_column='numero_RMG')
    expedition_date = models.DateField(null=True, blank=True, default=None, verbose_name=_('expedition_date'), db_column='fecha_expedicion')
    student_name = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name=_('student_name'), db_column='nombre_estudiante')
    center = models.CharField(max_length=100, null=True, blank=True, default=None,verbose_name=_('center'), db_column='centro')
    course = models.CharField(max_length=10, null=True, blank=True, default=None,verbose_name=_('course'), db_column='curso')
    municipality = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('municipality'), db_column='minocipio')
    tome_RTD = models.CharField(max_length=10, null=True, blank=True, default=None, verbose_name=_('tome_RTD'), db_column='tomo_RTD')
    folio_RTD = models.IntegerField(null=True, blank=True, default=None, verbose_name=_('folio_RTD'), db_column='folio_RTD')
    number_RTD = models.CharField(max_length=10, null=True, blank=True, default=None, verbose_name=_('number_RTD'), db_column='numero_RTD')
    name_endorser_1 = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name=_('name_endorser_1'), db_column='nombre_avalador_1')
    resp_endorser_1 = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('resp_endorser_1'), db_column='resp_avalador_1')
    name_endorser_2 = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name=_('name_endorser_2'), db_column='nombre_avalador_2')
    resp_endorser_2 = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('resp_endorser_2'), db_column='resp_avalador_2')
    name_endorser_3 = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name=_('name_endorser_3'), db_column='nombre_avalador_3')
    resp_endorser_3 = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('resp_endorser_3'), db_column='resp_avalador_3')
    name_endorser_4 = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name=_('name_endorser_4'), db_column='nombre_avalador_4')
    resp_endorser_4 = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('resp_endorser_4'), db_column='resp_avalador_4')
    name_endorser_5 = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name=_('name_endorser_5'), db_column='nombre_avalador_5')
    resp_endorser_5 = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('resp_endorser_5'), db_column='resp_avalador_5')
    doc = models.FileField(upload_to=titles_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('document'), db_column='documento')

    class Meta:
        verbose_name = _('Title')
        verbose_name_plural = _('Titles')
        db_table = f'{APP_LABEL.lower()}_tbd_titulo'

    def __str__(self):
        return f'{str(self.title_configuration)}'