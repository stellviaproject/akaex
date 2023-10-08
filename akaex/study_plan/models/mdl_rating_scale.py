from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan import managers
from study_plan.nom_types import APP_LABEL

from .mdl_scale_range import ScaleRange


class RatingScale(BaseAkModel):
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    min = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    max = models.DecimalField(decimal_places=2, max_digits=6, blank=True)

    type = models.ForeignKey(Nomenclator,
                             on_delete=models.CASCADE,
                             limit_choices_to={'type': NOM_TYPE['SCALE_TYPE']},
                             blank=False, verbose_name=_('type'),db_column='tipo'
                             )

    scale_ranges = models.ManyToManyField(
        ScaleRange, verbose_name=_('scale ranges'), db_column='rango_valor'
        # blank=False,
        # null=True
        # related_name='rating_scale'
        # through='RatingScaleRange',
        # through_fields=('rating_scale', 'scale_range'),
    )

    # using a custom manager
    objects = managers.RatingScaleManager()

    class Meta:
        verbose_name = _('Rating Scale')
        verbose_name_plural = _('Rating Scales')
        db_table = f'{APP_LABEL.lower()}_tbd_rango_evaluacion'


    @property
    def scale_type(self):
        from django.utils.html import format_html
        color = 'blue'
        nom_scale_type_cuantitativa = Nomenclator.objects.get(name='Cuantitativa')

        if self.type == nom_scale_type_cuantitativa:
            color = 'green'

        scale_type_str = f'<span style="color: {color};">{self.type} </span>'

        return format_html(scale_type_str)

    @property
    def ranges(self):
        return self.scale_ranges.all().count()

auditlog.register(RatingScale)