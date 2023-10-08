from datetime import datetime
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from fuc.nom_types import *


class FUCPersonList(BaseAkModel):
    id_akademos = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('id akademos'), db_column='id_akademos')
    fuc_id = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('fuc id'), db_column='fuc_id')
    ci = models.CharField(max_length=11, validators=[
        RegexValidator(r"^\d{11}$", message=_("The CI must have 11 characters.")),
        RegexValidator(r"[0-9]{2}((0[1-9]|11|12)|(1[0-9])|(2[0-9])|(3[0-1]))[0-9]{5}",
                       message=_("The CI is not valid."))], db_column='carnet_identidad', unique=True)
    ci_series = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('ci serie'), db_column='num_serie_ci')
    migrate_state = models.CharField(max_length=255, choices=CONST_FUC_MIGRATE_STATE_CHOICES, default=None, verbose_name=_('migrate state'), null=True, blank=True, db_column='estado_migracion')
    internal_state = models.CharField(max_length=255, choices=CONST_FUC_INTERNAL_STATE_CHOICES, default=CONST_FUC_INTERNAL_STATE_UNDEFINED, verbose_name=_('internal state'), null=True, blank=True, db_column='estado_interno')
    person_type = models.CharField(max_length=255, choices=CONST_PERSON_TYPES, verbose_name=_('person type'), null=True, blank=True, db_column='tipo_persona')
    second_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('second name'), db_column='segundo_nombre')
    first_last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('first last name'), db_column='primer_apellido')
    second_last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('second last name'), db_column='segundo_apellido')
    gender = models.CharField(max_length=255, verbose_name=_('gender'), db_column='sexo')
    race = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('race'), db_column='raza')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_('date of birth'), db_column='fecha_nacimiento')
    center_code = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('center code'), db_column='cod_centro')
    province = models.CharField(max_length=255, verbose_name=_('province'), db_column='provincia')
    province_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('province code'), db_column='codigo_provincia')
    municipality = models.CharField(max_length=255,  null=True, blank=True, verbose_name=_('municipality'), db_column='municipio')
    municipality_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('municipality code'), db_column='codigo_municipio')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('address'), db_column='direccion')
    location = models.CharField(max_length=255,  null=True, blank=True, verbose_name=_('location'), db_column='localidad')
    citizenship = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('citizenship'), db_column='ciudadana')
    citizenship_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('citizenship code'), db_column='codigo_ciudadania')
    phone = models.CharField(max_length=16, blank=True, null=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{8,15}$',
            message=_("Phone number must be entered in the format '123456789'")
        )], verbose_name=_('phone'), db_column='telefono'
                             )
    mobile_phone = models.CharField(max_length=16, blank=True, null=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{8,15}$',
            message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
        )], verbose_name=_('mobile phone'), db_column='telefono_movil'
                                    )
    responsibility = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('responsibility'), db_column='responsabilidad')
    scholar_level = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('scholar level'), db_column='nivel_escolar')
    scientific_category = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('scientific category'), db_column='categoria_cientifica')
    popular_council = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('popular council'), db_column='consejo_popular')
    academic_grade = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('academic grade'), db_column='grado_academico')

    class Meta:
        verbose_name = _('FUC Person List')
        verbose_name_plural = _('FUC Person Lists')
        db_table = f'{APP_LABEL.lower()}_tbn_person_list'


