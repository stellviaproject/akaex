from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from treenode.models import TreeNodeModel
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from core.tree_node_patch import AkTreeNodeModel
from study_plan.nom_types import APP_LABEL


class Theme(BaseAkModel, AkTreeNodeModel):
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    # the field used to display the model instance
    # default value 'pk'
    treenode_display_field = 'name'

    class Meta(BaseAkModel.Meta, AkTreeNodeModel.Meta):
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')
        db_table = f'{APP_LABEL.lower()}_tbd_tema'

    @classmethod
    def async_update_tree(cls):
        """ This function call an async task to update the tree
        """
        from study_plan.tasks import async_theme_update_tree_node
        async_theme_update_tree_node.delay()

    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    # Also we change this function to async update the tree
    @classmethod
    def update_tree(cls):
        cls.async_update_tree()

auditlog.register(Theme)