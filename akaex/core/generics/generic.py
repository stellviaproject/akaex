import uuid
import re
import math
from django.db import models
import django.db.models.fields.related as django_related_fields
from django.urls import reverse, include, path, re_path
from django_auto_prefetching import AutoPrefetchViewSetMixin
from django_filters import rest_framework as filters
from django.contrib import admin
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import FieldDoesNotExist

from base import settings
from guardian.admin import GuardedModelAdmin
from core.middleware import ModelRequestMiddleware
from core.utils import paginate_function
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel


from django.db.models import Q
from guardian.core import ObjectPermissionChecker
from guardian.ctypes import get_content_type
from guardian.exceptions import ObjectNotPersisted
from django.contrib.auth.models import Permission
from django_softdelete.models import SoftDeleteQuerySet

import warnings




class CommonManager(models.Manager):

    @property
    def user_or_group_field(self):
        try:
            self.model._meta.get_field('user')
            return 'user'
        except FieldDoesNotExist:
            return 'group'

    def is_generic(self):
        try:
            self.model._meta.get_field('object_pk')
            return True
        except FieldDoesNotExist:
            return False

    def assign_perm(self, perm, user_or_group, obj):
        """
        Assigns permission with given ``perm`` for an instance ``obj`` and
        ``user``.
        """
        if getattr(obj, 'pk', None) is None:
            raise ObjectNotPersisted("Object %s needs to be persisted first"
                                     % obj)
        ctype = get_content_type(obj)
        if not isinstance(perm, Permission):
            permission = Permission.objects.get(content_type=ctype, codename=perm)
        else:
            permission = perm

        kwargs = {'permission': permission, self.user_or_group_field: user_or_group}
        if self.is_generic():
            kwargs['content_type'] = ctype
            kwargs['object_pk'] = obj.pk
        else:
            kwargs['content_object'] = obj
        obj_perm, _ = self.get_or_create(**kwargs)
        return obj_perm

    def bulk_assign_perm(self, perm, user_or_group, queryset):
        """
        Bulk assigns permissions with given ``perm`` for an objects in ``queryset`` and
        ``user_or_group``.
        """
        if isinstance(queryset, list):
            ctype = get_content_type(queryset[0])
        else:
            ctype = get_content_type(queryset.model)

        if not isinstance(perm, Permission):
            permission = Permission.objects.get(content_type=ctype, codename=perm)
        else:
            permission = perm

        checker = ObjectPermissionChecker(user_or_group)
        checker.prefetch_perms(queryset)

        assigned_perms = []
        for instance in queryset:
            if not checker.has_perm(permission.codename, instance):
                kwargs = {'permission': permission, self.user_or_group_field: user_or_group}
                if self.is_generic():
                    kwargs['content_type'] = ctype
                    kwargs['object_pk'] = instance.pk
                else:
                    kwargs['content_object'] = instance
                assigned_perms.append(self.model(**kwargs))
        self.model.objects.bulk_create(assigned_perms)

        return assigned_perms

    def assign_perm_to_many(self, perm, users_or_groups, obj):
        """
        Bulk assigns given ``perm`` for the object ``obj`` to a set of users or a set of groups.
        """
        ctype = get_content_type(obj)
        if not isinstance(perm, Permission):
            permission = Permission.objects.get(content_type=ctype,
                                                codename=perm)
        else:
            permission = perm

        kwargs = {'permission': permission}
        if self.is_generic():
            kwargs['content_type'] = ctype
            kwargs['object_pk'] = obj.pk
        else:
            kwargs['content_object'] = obj

        to_add = []
        field = self.user_or_group_field
        for user in users_or_groups:
            kwargs[field] = user
            to_add.append(
                self.model(**kwargs)
            )

        return self.model.objects.bulk_create(to_add)

    def assign(self, perm, user_or_group, obj):
        """ Depreciated function name left in for compatibility"""
        warnings.warn(
            "UserObjectPermissionManager method 'assign' is being renamed to 'assign_perm'. Update your code accordingly as old name will be depreciated in 2.0 version.",
            DeprecationWarning)
        return self.assign_perm(perm, user_or_group, obj)

    def remove_perm(self, perm, user_or_group, obj):
        """
        Removes permission ``perm`` for an instance ``obj`` and given ``user_or_group``.
        Please note that we do NOT fetch object permission from database - we
        use ``Queryset.delete`` method for removing it. Main implication of this
        is that ``post_delete`` signals would NOT be fired.
        """
        if getattr(obj, 'pk', None) is None:
            raise ObjectNotPersisted("Object %s needs to be persisted first"
                                     % obj)

        filters = Q(**{self.user_or_group_field: user_or_group})

        if isinstance(perm, Permission):
            filters &= Q(permission=perm)
        else:
            filters &= Q(permission__codename=perm,
                         permission__content_type=get_content_type(obj))

        if self.is_generic():
            filters &= Q(object_pk=obj.pk)
        else:
            filters &= Q(content_object__pk=obj.pk)
        return self.filter(filters).delete()

    def bulk_remove_perm(self, perm, user_or_group, queryset):
        """
        Removes permission ``perm`` for a ``queryset`` and given ``user_or_group``.
        Please note that we do NOT fetch object permission from database - we
        use ``Queryset.delete`` method for removing it. Main implication of this
        is that ``post_delete`` signals would NOT be fired.
        """
        filters = Q(**{self.user_or_group_field: user_or_group})

        if isinstance(perm, Permission):
            filters &= Q(permission=perm)
        else:
            ctype = get_content_type(queryset.model)
            filters &= Q(permission__codename=perm,
                         permission__content_type=ctype)

        if self.is_generic():
            filters &= Q(object_pk__in=[str(pk) for pk in queryset.values_list('pk', flat=True)])
        else:
            filters &= Q(content_object__in=queryset)

        return self.filter(filters).delete()

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(is_deleted=False)


#    def __init__(self, ignore_disable):
#        super().__init__()
#        self.ignore_disable = ignore_disable


class BaseAkModel(SoftDeleteModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_('name'), max_length=255, null=False, db_column='nombre')
    owner_id = models.UUIDField(_('owner_id'), null=True, default=None, blank=True, db_column='autor_id')
    is_disable = models.BooleanField(_('is_disable'), default=False, db_column='deshabilitado')
    create_date = models.DateTimeField(_('create_date'), auto_now_add=True, db_column='fecha_creacion')
    update_date = models.DateTimeField(_('update_date'), null=True, auto_now=True, db_column='fecha_modificacion')
    ignore_disable = False

    objects = CommonManager()

#    objects = CommonManager(ignore_disable=ignore_disable)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['name']),
        ]
        # ordering = ['-create_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        model_request = ModelRequestMiddleware.get_request()
        if model_request and model_request.user and not self.owner_id:
            self.owner_id = model_request.user.id

        super().save(*args, **kwargs)


class BaseAkAdmin(GuardedModelAdmin):

    search_fields = ('type', )
    exclude = ('owner_id',)


    def save_model(self, request, obj, form, change):
        if hasattr(obj, 'owner_id'):
            if not obj.owner_id:
                obj.owner_id = request.user.id

        super().save_model(request, obj, form, change)

    def get_urls(self):
            urls = super().get_urls()
            custom_urls = [
                path(
                    r'soft_deleted_objects/',
                    self.admin_site.admin_view(self.soft_deleted_objects),
                    name='soft-deleted',
                ),
            ]
            return custom_urls + urls

    def soft_deleted_objects(self, request):
            paginate=10
            context = ""
            response = super(BaseAkAdmin, self).changelist_view(request, context)
            qs = self.model.deleted_objects.all().order_by('-deleted_at')

            action = request.POST.get('action') if request.POST.get('action') else None

            if request.method == 'POST':
                if action == "":
                    return HttpResponseRedirect(request.build_absolute_uri())

                if action == "restore_selected":
                    for obj in request.POST.getlist('checkbox-deleted'):
                        qs = (self.model.deleted_objects.get(id=obj)).restore()
                    return HttpResponseRedirect(request.build_absolute_uri())

                else:
                    obj = request.POST.get('restore')
                    qs=(self.model.deleted_objects.get(id=obj)).restore()
                    return HttpResponseRedirect(request.build_absolute_uri())

            page_range = range(math.ceil(qs.count() / paginate))

            if request.GET.get('q'):
                qs = self.model.deleted_objects.filter(name__contains=request.GET.get('q')).order_by('-deleted_at')
                page_range = range(math.ceil(qs.count() / paginate))

            if request.GET.get('all'):
                qs = self.model.deleted_objects.all().order_by('-deleted_at')
                if request.GET.get('q'):
                    qs = self.model.deleted_objects.filter(name__contains=request.GET.get('q')).order_by('-deleted_at')

            else:
                if request.GET.get('p'):
                    qs = paginate_function(qs, int(request.GET.get('p')), paginate)
                else:
                    qs = paginate_function(qs, 0, paginate)

            extra_content = {
                'qs': qs,
                'title': f"Seleccione {str(self.model._meta.verbose_name_plural)} a restaurar",
                'name': str(self.model._meta.verbose_name_plural),
                'result_count': qs.count(),
                'pagination_required': False if (request.GET.get('all') or page_range==range(0,1)) else True,
                'page_range': page_range if page_range else None,
            }

            response.context_data.update(extra_content)

            return TemplateResponse(
                request,
                'core/deleted_objects.html',
                response.context_data,
            )

class BaseAkFilterSet(filters.FilterSet):
    """When initialized, adds in filters labels, its related model url address.

    Usage: 
    
    For generated filters it will search automatically its related model, the first 
    viewset with this model in the queryset, and then look for the list
    url endpoint.
    
    For declared filters it can be added an attribute 'related_model' which 
    would be the model to look and then follow next steps as with generated filters.
    Example:

        from core.models import EducationLevelType

        ...

        education_level_type = filters.UUIDFilter(label='Nivel educativo',
            method='by_education_level_type')
        education_level_type.related_model = EducationLevelType

        ...

    Asumptions:
        
        * The locations of (api) views and urls for every app.
        * Only one endpoint for each model.
    """
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        
        if settings.DEBUG:
            from core.api.generics.generic import BaseAkViewSet

            mdl = self.Meta().model

            for __, filter in self.filters.items():
                try:
                    mdl_attribute = getattr(mdl, filter.field_name)
                    attribute_field = mdl_attribute.field
                    field_class = attribute_field.__class__
                    class_name = field_class.__name__
                except AttributeError:
                    try:
                        related_mdl = filter.related_model
                    except AttributeError:
                        continue
                else:
                    if class_name in django_related_fields.__dir__():
                        attribute_field = mdl_attribute.field
                        related_mdl = attribute_field.related_model
                    else:
                        continue
                
                if related_mdl:
                    module_name = related_mdl.__module__
                    app_name = module_name.split(".")[0]

                    lcls = locals()
                    code = f"import {app_name}.api.views; api_views = {app_name}.api.views"
                    exec(code, globals(), lcls) 
                    api = lcls['api_views']
                    viewset_name = None
                    for view_name, view in api.__dict__.items():
                        if type(view) == type and view.__base__ in (BaseAkViewSet, AutoPrefetchViewSetMixin):
                            if view.queryset.model == related_mdl:
                                viewset_name = view_name
                                break
                    
                    code = f'import {app_name}.api.urls; api_urls = {app_name}.api.urls' 
                    exec(code, globals(), lcls)
                    api = lcls['api_urls']
                    router = api.router
                    url_not_found = False
                    related_mdl_url = None
                    if viewset_name:
                        for url in router.urls:
                            if viewset_name in url.lookup_str:
                                if "list" in url.name:
                                    viewset_name_list = url.name
                                    try:
                                        related_mdl_url = reverse(f"{api.app_name}:{viewset_name_list}")
                                        break
                                    except Exception as e:
                                        url_not_found = True
                                        break
                        
                    if related_mdl_url and not url_not_found:
                        if not filter.label:
                            filter.label = _(filter.field_name).capitalize()
                            
                        filter.label += f" ({related_mdl_url})"
                    else:
                        filter.label += f" (?)"


class HiddenModelAdmin(BaseAkAdmin):
    def get_model_perms(self, *args, **kwargs):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


