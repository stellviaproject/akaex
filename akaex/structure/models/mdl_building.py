from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from structure.nom_types import *
from core.models import *
from structure.models.mdl_constrction_type import ConstructionType

class Building(BaseAkModel):
    """Represents the buildings"""
    code_building = models.CharField(max_length=50, default='', verbose_name=_('code_building'), db_column='codigo')
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, default='', verbose_name=_('province'), db_column='id_provincia')
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, default='', verbose_name=_('municipality'), db_column='id_municipio')
    address = models.CharField(max_length=255, default='', verbose_name=_('address'), db_column='direccion')
    location = models.ForeignKey(LocationType, on_delete=models.SET_NULL, null=True, default='', verbose_name=_('location'), db_column='id_localidad')
    popular_council = models.ForeignKey(PopularCouncilType, on_delete=models.SET_NULL, null=True, default='', verbose_name=_('popular_council'), db_column='id_consejo_popular')
    constructive_state = models.ForeignKey(BuildingConstructiveStateType, on_delete=models.SET_NULL, null=True, default='', verbose_name=_('constructive_state'), db_column='id_estado_constructivo_inmueble')
    delivered = models.BooleanField(default=False, verbose_name=_('delivered'), db_column='entregado')
    use_state = models.CharField(default=STATE_USE_TYPE, choices=STATE_USE_TYPES,verbose_name=_('use_state'),db_column='estado_uso',max_length=100)
    construction_type = models.ForeignKey(ConstructionType, on_delete=models.SET_NULL, null=True, verbose_name=_('construction_type'), db_column='id_construccion')
    patrimony_type = models.ForeignKey(PatrimonyType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('patrimony_type'), db_column='id_patrimonio')
    destination = models.CharField(max_length=300, default='', verbose_name=_('destination'), db_column='destino')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')
        db_table = f'{APP_LABEL.lower()}_tbd_inmueble'


    def __str__(self):
        return self.code_building