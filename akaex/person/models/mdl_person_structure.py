from django.db.models.constraints import UniqueConstraint
from structure.models import *
from django.db import models, transaction, IntegrityError
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from .mdl_person import Person
from core.models import PersonCategoryType
from person.utils import APP_LABEL

class PersonStructure(BaseAkModel):
    """ It relates the person with an structure """
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    category = models.ForeignKey(PersonCategoryType, on_delete=models.CASCADE, default=None, verbose_name=_('category'), db_column='categoria')
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='estructura')
    category_order= models.IntegerField(default=0, verbose_name=_('category_order'), db_column='orden_categoria')

    def __str__(self):
        return f'{self.category} --{self.person} -- Structure: {self.structure_id}'

    class Meta:
        verbose_name = _('Person Structure')
        verbose_name_plural = _('Person Structures')
        indexes = [
            models.Index(fields=['structure']),
        ]
        constraints = [
            UniqueConstraint(fields=['structure', 'person', 'category'], name='uniq_pers_per_struct')
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_persona_estructura'


def associate_person_structure(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                PersonStructure.objects.create(person=instance.person, structure_id=instance.structure_id, category_id=instance.category_id, category_order=instance.category_id.priority)
        except IntegrityError as ex:
            print('It is OK, the person is already associate with the Structure')


def delete_person_structure(sender, instance, **kwargs):
    try:
        person = instance.person
        if not person.is_in_structure_in_different_rol(sender, instance.structure_id):
            structure_person = PersonStructure.objects.get(person_id=person.id, structure_id=instance.structure_id)
            structure_person.delete()
    except Exception as ex:
        raise Exception("Error deleting a Person from Structure")
