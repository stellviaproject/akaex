from django.db import transaction
from django.utils.text import slugify
from treenode.cache import update_cache
from treenode.debug import debug_performance
from django import forms
from treenode.memory import update_refs
from treenode.models import TreeNodeModel
from treenode.utils import join_pks, PKS_SEPARATOR


class AkTreeNodeModel(TreeNodeModel):
    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    @classmethod
    def internal_update_tree(cls):
        debug_message_prefix = '[treenode] update %s.%s tree: ' % (
            cls.__module__, cls.__name__,)

        with debug_performance(debug_message_prefix):
            # update db
            objs_data = cls.__get_nodes_data()

            with transaction.atomic():
                for obj_key, obj_data in objs_data.items():
                    obj_pk = obj_key
                    cls.objects.filter(pk=obj_pk).update(**obj_data)

            # update in-memory instances
            update_refs(cls, objs_data)

            # update cache instances
            update_cache(cls)

    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    @classmethod
    def __get_nodes_data(cls):

        objs_qs = cls.objects.select_related('tn_parent')
        objs_list = list(objs_qs)
        objs_dict = {str(obj.pk): obj for obj in objs_list}
        objs_data_dict = {str(obj.pk): obj.__get_node_data(objs_list, objs_dict) for obj in objs_list}
        objs_data_sort = lambda obj: objs_data_dict[str(obj['pk'])]['tn_order_str']
        objs_data_list = list(objs_data_dict.values())
        objs_data_list.sort(key=objs_data_sort)
        objs_pks_by_parent = {}
        objs_order_cursor = 0
        objs_index_cursors = {}
        objs_index_cursor = 0

        # index objects by parent pk
        for obj_data in objs_data_list:
            obj_parent_key = str(obj_data['tn_parent_pk'])
            if not obj_parent_key in objs_pks_by_parent:
                objs_pks_by_parent[obj_parent_key] = []
            objs_pks_by_parent[obj_parent_key].append(obj_data['pk'])

            # update global order with normalized value
            obj_data['tn_order'] = objs_order_cursor
            objs_order_cursor += 1

            # update child index
            obj_parent_key = str(obj_data['tn_parent_pk'])
            objs_index_cursor = objs_index_cursors.get(obj_parent_key, 0)
            obj_data['tn_index'] = objs_index_cursor
            objs_index_cursor += 1
            objs_index_cursors[obj_parent_key] = objs_index_cursor

        for obj_data in sorted(objs_data_list, key=lambda obj: obj['tn_level'], reverse=True):

            # update children
            children_parent_key = str(obj_data['pk'])
            obj_data['tn_children_pks'] = list(
                objs_pks_by_parent.get(children_parent_key, []))
            obj_data['tn_children_count'] = len(obj_data['tn_children_pks'])

            # update siblings
            siblings_parent_key = str(obj_data['tn_parent_pk'])
            obj_data['tn_siblings_pks'] = list(
                objs_pks_by_parent.get(siblings_parent_key, []))
            obj_data['tn_siblings_pks'].remove(obj_data['pk'])
            obj_data['tn_siblings_count'] = len(obj_data['tn_siblings_pks'])

            # update descendants and depth
            if obj_data['tn_children_count'] > 0:
                obj_children_pks = obj_data['tn_children_pks']
                obj_descendants_pks = list(obj_children_pks)
                obj_depth = 1
                for obj_child_pk in obj_children_pks:
                    obj_child_key = str(obj_child_pk)
                    obj_child_data = objs_data_dict[obj_child_key]
                    obj_child_descendants_pks = obj_child_data.get('tn_descendants_pks', [])
                    if obj_child_descendants_pks:
                        obj_descendants_pks += obj_child_descendants_pks
                        obj_depth = max(obj_depth, obj_child_data['tn_depth'] + 1)

                if obj_descendants_pks:
                    obj_descendants_sort = lambda obj_pk: objs_data_dict[str(obj_pk)]['tn_order']
                    obj_descendants_pks.sort(key=obj_descendants_sort)
                    obj_data['tn_descendants_pks'] = obj_descendants_pks
                    obj_data['tn_descendants_count'] = len(obj_data['tn_descendants_pks'])
                    obj_data['tn_depth'] = obj_depth

        for obj_data in objs_data_list:
            obj = obj_data['instance']
            obj_key = str(obj_data['pk'])

            # join all pks lists
            obj_data['tn_ancestors_pks'] = join_pks(obj_data['tn_ancestors_pks'])
            obj_data['tn_children_pks'] = join_pks(obj_data['tn_children_pks'])
            obj_data['tn_descendants_pks'] = join_pks(obj_data['tn_descendants_pks'])
            obj_data['tn_siblings_pks'] = join_pks(obj_data['tn_siblings_pks'])

            # clean data
            obj_data.pop('instance', None)
            obj_data.pop('pk', None)
            obj_data.pop('tn_parent_pk', None)
            obj_data.pop('tn_order_str', None)

            if obj_data['tn_ancestors_count'] == obj.tn_ancestors_count:
                obj_data.pop('tn_ancestors_count')

            if obj_data['tn_ancestors_pks'] == obj.tn_ancestors_pks:
                obj_data.pop('tn_ancestors_pks', None)

            if obj_data['tn_children_count'] == obj.tn_children_count:
                obj_data.pop('tn_children_count', None)

            if obj_data['tn_children_pks'] == obj.tn_children_pks:
                obj_data.pop('tn_children_pks', None)

            if obj_data['tn_depth'] == obj.tn_depth:
                obj_data.pop('tn_depth', None)

            if obj_data['tn_descendants_count'] == obj.tn_descendants_count:
                obj_data.pop('tn_descendants_count', None)

            if obj_data['tn_descendants_pks'] == obj.tn_descendants_pks:
                obj_data.pop('tn_descendants_pks', None)

            if obj_data['tn_index'] == obj.tn_index:
                obj_data.pop('tn_index', None)

            if obj_data['tn_level'] == obj.tn_level:
                obj_data.pop('tn_level', None)

            if obj_data['tn_order'] == obj.tn_order:
                obj_data.pop('tn_order', None)

            if obj_data['tn_siblings_count'] == obj.tn_siblings_count:
                obj_data.pop('tn_siblings_count', None)

            if obj_data['tn_siblings_pks'] == obj.tn_siblings_pks:
                obj_data.pop('tn_siblings_pks', None)

            if len(obj_data) == 0:
                objs_data_dict.pop(obj_key, None)

        return objs_data_dict

    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    def __get_node_data(self, objs_list, objs_dict):

        obj_dict = {}

        # update ancestors
        parent_pk = self.tn_parent_id

        ancestors_list = []
        ancestor_pk = parent_pk
        while ancestor_pk:
            ancestor_obj = objs_dict.get(str(ancestor_pk))
            ancestors_list.insert(0, ancestor_obj)
            ancestor_pk = ancestor_obj.tn_parent_id
        ancestors_pks = [obj.pk for obj in ancestors_list]
        ancestors_count = len(ancestors_pks)

        order_objs = list(ancestors_list) + [self]
        order_strs = [obj.__get_node_order_str() for obj in order_objs]
        order_str = ''.join(order_strs)

        obj_dict = {
            'instance': self,
            'pk': self.pk,
            'tn_parent_pk': parent_pk,
            'tn_ancestors_pks': ancestors_pks,
            'tn_ancestors_count': ancestors_count,
            'tn_children_pks': [],
            'tn_children_count': 0,
            'tn_descendants_pks': [],
            'tn_descendants_count': 0,
            'tn_siblings_pks': [],
            'tn_siblings_count': 0,
            'tn_depth': 0,
            'tn_level': (ancestors_count + 1),
            'tn_order': 0,
            'tn_order_str': order_str,
        }

        return obj_dict

    # Ignore this function, It was copied from TreeNodeModel due to problems with UUID
    def __get_node_order_str(self):
        priority_max = 9999999999
        priority_len = len(str(priority_max))
        priority_val = priority_max - min(self.tn_priority, priority_max)
        priority_key = str(priority_val).zfill(priority_len)
        alphabetical_val = slugify(str(self))
        alphabetical_key = alphabetical_val.ljust(priority_len, str('z'))
        alphabetical_key = alphabetical_key[0:priority_len]
        pk_val = min(self.pk.int, priority_max)
        pk_key = str(pk_val).zfill(priority_len)
        s = '%s%s%s' % (priority_key, alphabetical_key, pk_key,)
        s = s.upper()
        return s

    class Meta:
        abstract = True
        ordering = ['tn_order']


class AkTreeNodeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'tn_parent' not in self.fields:
            return
        exclude_pks = []
        obj = self.instance
        if obj.pk:
            exclude_pks += [obj.pk]
            exclude_pks += self.split_pks2(obj.tn_descendants_pks)
        manager = obj.__class__.objects
        self.fields['tn_parent'].queryset = manager.exclude(pk__in=exclude_pks)

    def split_pks2(self, s):
        if not s:
            return []
        l = [str(v) for v in s.split(PKS_SEPARATOR) if v]
        return l
