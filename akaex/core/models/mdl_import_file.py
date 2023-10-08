from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL


class ImportFile(BaseAkModel):
    type = models.CharField(max_length=100, verbose_name=_('type'), db_column='tipo')
    file = models.FileField(upload_to='imports', verbose_name=_('file'), db_column='archivo')
    description = models.TextField(null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    error_file = models.FileField(upload_to='import_error', null=True, blank=True, verbose_name=_('error file'), db_column='fichero_error')

    class Meta:
        verbose_name = _('Import File')
        verbose_name_plural = _('Import Files')
        db_table = f'{APP_LABEL.lower()}_tbn_importacion_archivo'