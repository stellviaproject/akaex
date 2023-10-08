from django.db import models
from core.nom_types import STRUCTURE_TYPE


class StructureQuerySet(models.QuerySet):
    """
        With this class we can chain `get_school_queryset` function with others queryset methods
        Ex: Structure.objects.get_school_queryset().filter(...).order_by(...)
    """

    def get_school_queryset(self):
        return self.filter(type__type=STRUCTURE_TYPE['STRUCTURE_SCHOOL_TYPE']).order_by('name')

    def get_structures_queryset(self):
        return self.exclude(type__type=STRUCTURE_TYPE['STRUCTURE_SCHOOL_TYPE'])

    def get_structures_father_queryset(self):
        return self.filter(type__type__in=[STRUCTURE_TYPE['STRUCTURE_MINED_TYPE'], STRUCTURE_TYPE['STRUCTURE_DIR_PROVINCIAL_TYPE'], STRUCTURE_TYPE['STRUCTURE_DIR_MUNICIPALITY_TYPE']])


class StructureManager(models.Manager):

    def get_queryset(self):
        return StructureQuerySet(self.model, using=self._db)

    def get_school_queryset(self):
        return self.get_queryset().get_school_queryset()

    def get_structures_queryset(self):
        return self.get_queryset().get_structures_queryset()

    def get_structures_father_queryset(self):
        return self.get_queryset().get_structures_father_queryset()

    def create_school(self, **kwargs):
        from structure.models import StructureType

        structure_type = StructureType.objects.get(code='07')
        kwargs.update({'type_id': structure_type.id})

        return self.create(**kwargs)

        
class EcducativeCenterManager(models.Manager):

    def get_queryset(self):
        return  StructureQuerySet(self.model, using=self._db).get_school_queryset()


    def create(self, **kwargs):
        from structure.models import StructureType
        # from core.nom_types import STRUCTURE_TYPE

        structure_type = StructureType.objects.get(code='07')
        kwargs.update({'type_id': structure_type.id})

        return self.create(**kwargs)