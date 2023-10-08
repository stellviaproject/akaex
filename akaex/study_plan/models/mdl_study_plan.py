from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from treenode.models import TreeNodeModel
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from core.tree_node_patch import AkTreeNodeModel
from structure.models import SpecialityModality
from study_plan.nom_types import APP_LABEL


class StudyPlan(BaseAkModel, AkTreeNodeModel):
    """Represents the study plans associated with specialties"""
    treenode_display_field = 'name'

    speciality = models.ForeignKey(SpecialityModality, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('speciality'), db_column='especialidad')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta(BaseAkModel.Meta, AkTreeNodeModel.Meta):
        verbose_name = _('Study plan')
        verbose_name_plural = _('Study plans')
        db_table = f'{APP_LABEL.lower()}_tbd_plan_estudio'

    @classmethod
    def async_update_tree(cls):
        """ This function call an async task to update the tree
        """
        from study_plan.tasks import async_study_plan_update_tree_node
        async_study_plan_update_tree_node.delay()

    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    # Also we change this function to async update the tree
    @classmethod
    def update_tree(cls):
        cls.async_update_tree()

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(StudyPlan)