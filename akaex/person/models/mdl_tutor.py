from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from person.utils import APP_LABEL

class Tutor(BaseAkModel):
    """" It relates all the people who are tutors and all the data about it."""
    full_name = models.CharField(max_length=100, default='', verbose_name=_('full name'), db_column='nombre_completo')
    relationship = models.ForeignKey(RelationshipType, on_delete=models.SET_NULL, null=True, verbose_name=_('relationship'), db_column='relacion')
    ci = models.CharField(max_length=11,
                          validators=[RegexValidator(r"^\d{11}$", message="The CI must have 11 characters")], verbose_name=_('id'), db_column='carne')
    work_center = models.TextField(default='', null=True, blank=True, verbose_name=_('work center'), db_column='centro_trabajo')
    social_origin = models.ForeignKey(SocialOriginType, on_delete=models.SET_NULL, null=True, verbose_name=_('social origin'), db_column='origen_social')
    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            )], verbose_name=_('phone'), db_column='telefono'
    )

    class Meta:
        verbose_name = _('Tutor')
        verbose_name_plural = _('Tutors')
        db_table = f'{APP_LABEL.lower()}_tbr_tutor'

    def __str__(self):
        return self.full_name