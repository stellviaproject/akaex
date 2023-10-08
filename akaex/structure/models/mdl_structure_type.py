from django.db.models.functions import Cast
from django.db.models.fields import IntegerField
from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from colorfield.fields import ColorField
from structure.utils import APP_LABEL
from core.models import *

class StructureType(BaseType):
    """Represents the types of structures"""
    code = models.CharField(max_length=10, unique=True, error_messages={'unique':_('Exist a type of structure with this code')}, verbose_name=_('code'), db_column='codigo')
    admit_child = models.BooleanField(default=False, verbose_name=_('admit_child'), db_column='admite_hijo')
    # type = models.CharField(max_length=100, unique=True)
    color = ColorField(default='#FFFFFF')
    short_name = models.CharField(_('short_name'), null=True, blank=True, max_length=50, db_column='nombre_corto')
    # description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(StructureCategoryType, on_delete=models.SET_NULL, null=True, verbose_name=_('category'), db_column='id_categoria_estructura')
    level = models.ForeignKey(StructureLevelType, on_delete=models.SET_NULL, null=True, verbose_name=_('level'), db_column='id_nivel_estructura')

    class Meta:
        verbose_name = _('StructureType')
        verbose_name_plural = _('StructureTypes')
        db_table = f'{APP_LABEL.lower()}_tbd_tipo_estructura'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.code:
            last = StructureType.objects.annotate(
                code_int=Cast('code', output_field=IntegerField()),
            ).order_by('-code').first()
            if last is None:
                self.code = str('01')
            else:
                next= str(last.code)
                print(int(next))
                if int(next) >= 9:
                    self.code =int(next) + 1
                elif int(next) < 9:
                    value = int(next[1])+1
                    self.code = str(f'0{value}')
        super().save(*args, **kwargs)