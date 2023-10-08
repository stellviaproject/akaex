from datetime import datetime
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from core.models import *
from structure.models import *
from person.managers import PersonManager
from person.utils import APP_LABEL


def person_photo_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<person>/<photo>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'person/photo/{current_date}/{filename}'

    return path

class Person(BaseAkModel):
    """" It relates all the people who interact (with roles) or whose information is managed."""
    # NOMINAL INFORMATION
    second_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('second name'), db_column='segundo_nombre')
    first_last_name = models.CharField(max_length=100, verbose_name=_('first last name'), db_column='primer_apellido')
    second_last_name = models.CharField(max_length=100, verbose_name=_('second last name'), db_column='segundo_apellido')
    ci = models.CharField(max_length=11,
                          validators=[RegexValidator(r"^\d{11}$", message=_("The CI must have 11 characters.")), 
                            RegexValidator(r"[0-9]{2}((0[1-9]|11|12)|(1[0-9])|(2[0-9])|(3[0-1]))[0-9]{5}", message=_("The CI is not valid."))], db_column='carne') #Represents the person's identity card number.
    ci_serie = models.CharField(max_length=50, null=True, blank=True, db_column='no_serie_ci') #Represents the person's identity card number serie.
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_('date of birth'), db_column='fecha_nacimiento')
    photo = models.ImageField(upload_to=person_photo_storage_path, default=None, null=True, blank=True, verbose_name=_('photo'), db_column='foto')

    # CONTACT DATA
    address = models.TextField(default='', null=True, blank=True, verbose_name=_('address'), db_column='direccion')
    address_province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('address province'), db_column='direccion_provincia')
    address_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('address municipality'), db_column='direccion_municipio')
    address_popular_council = models.ForeignKey(PopularCouncilType, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('address popular_council'), db_column='direccion_consejo_popular')
    address_location = models.ForeignKey(LocationType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('address location'), db_column='direccion_localidad')
    email = models.EmailField(default='', null=True, blank=True, verbose_name=_('email'), db_column='correo_electronico')
    mobile_phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            )], verbose_name=_('mobile phone'), db_column='telefono_movil'
    )
    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message=_("Phone number must be entered in the format '123456789'")
            )],verbose_name=_('phone'), db_column='telefono'
    )

    # PHENOTYPIC FEATURES
    gender = models.ForeignKey(GenderType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('gender'), db_column='genero')
    race = models.ForeignKey(RaceType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('race'), db_column='raza')
    height = models.IntegerField(null=True, blank=True, default=None, db_column='estatura', verbose_name='height')
    weight = models.IntegerField(null=True, blank=True, default=None, db_column='peso', verbose_name='weight')
    
    # SUPERATION DATA
    scholar_level = models.ForeignKey(ScholarLevelType, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('scholar level'), db_column='nivel_escolar')
    teaching_category = models.ForeignKey(TeachingCategoryType, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('teaching category'), db_column='nivel_ensennanza')
    profession = models.ForeignKey(ProfessionType, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('profession'), db_column='profesion')
    academic_grade = models.ForeignKey(AcademicGradeType, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('academic grade'), db_column='anno_academico')
    investigative_category = models.ForeignKey(InvestigativeCategoryType, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('investigative category'), db_column='categoria_investigativa')

    extra_field = models.JSONField(blank=True, null=True, verbose_name=_('extra field'), db_column='archivo_extra')

    # RELATIONS
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('user'), db_column='usuario')
    structures = models.ManyToManyField(Structure, through='PersonStructure', related_name='structures', verbose_name=_('structures'), db_column='estructuras')
    educational_workers = models.ManyToManyField(Structure, through='EducationalWorker',
                                                 related_name='educational_workers', verbose_name=_('educational workers'), db_column='trabajadores_docentes')
    not_educational_workers = models.ManyToManyField(Structure, through='NotEducationalWorker',
                                                     through_fields=('person', 'structure'),
                                                     related_name='not_educational_workers', verbose_name=_('not educational workers'), db_column='trabajadores_no_docentes')
    students = models.ManyToManyField(Structure, through='Student', related_name='students', verbose_name=_('students'), db_column='estudiantes')

    objects = PersonManager()
    
    @property
    def full_name(self):
        return f'{self.name} {self.second_name if self.second_name else ""} {self.first_last_name} {self.second_last_name}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        abstract = False
        db_table = f'{APP_LABEL.lower()}_tbr_persona'

    def __str__(self):
        return self.full_name

    def is_in_structure_in_different_rol(self, rol, structure_id):
        """
            Function to know if a Person is in an Structure with a different Rol

        :param rol: Is a class (NotEducationalWorker, EducationalWorker, Student)
        :param structure_id: Structure id
        :return: True if the person is in the Structure but with a different rol otherwise False

        Ex: If the Person is in Structure 1 as Student and we call this function

        person.is_in_structure_in_different_rol(Student, 1) it will return False
        """
        student = self.student_set.filter(structure_id=structure_id)
        not_educational_worker = self.noteducationalworker_set.filter(structure_id=structure_id)
        educational_worker = self.educationalworker_set.filter(structure_id=structure_id)
        if type(rol) == type(EducationalWorker):
            if student or not_educational_worker:
                return True
        elif type(rol) == type(NotEducationalWorker):
            if student or educational_worker:
                return True
        elif type(rol) == type(Student):
            if not_educational_worker or educational_worker:
                return True

        return False