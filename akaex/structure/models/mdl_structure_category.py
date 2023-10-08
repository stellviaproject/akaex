from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from .mdl_category_attribute import CategoryAttribute

class StructureCategory(BaseAkModel):
    """Represents the categories of a structure"""
    attribute = models.ForeignKey(
        CategoryAttribute, on_delete=models.SET_NULL, null=True, verbose_name=_('attribute'), db_column='id_atributo_categoria')

    class Meta:
        verbose_name = _('StructureCategory')
        verbose_name_plural = _('StructureCategories')
        db_table = f'{APP_LABEL.lower()}_tbd_categoria_estructura'


    def __str__(self):
        return self.name