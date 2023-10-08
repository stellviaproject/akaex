# from colorfield.fields import ColorField
# from django.utils.translation import gettext_lazy as _
# from .generics.generic import BaseAkModel
# from django.db.models.signals import pre_save, post_delete
# from django.db import models, IntegrityError
# from django.db.models import F
# from django.core.validators import RegexValidator
#
# from .utils import APP_LABEL
#
# NOM_TYPE = {
#     'EYES_COLOR': 'EYES_COLOR',
#     'HAIR_COLOR': 'HAIR_COLOR',
#     'GENDER': 'GENDER',
#     'QUALIFICATION_TYPE': 'QUALIFICATION_TYPE',
#     'SCALE_TYPE': 'SCALE_TYPE',
#     'SKIN_COLOR': 'SKIN_COLOR',
#     'RACE': 'RACE',
#     'STATUS': 'STATUS',
#     'SPECIALTY': 'SPECIALTY',
#     'TEACHING_CATEGORY': 'TEACHING_CATEGORY',
#     'TEACHER_STATUS': 'TEACHER_STATUS',
#     'CATEGORY': 'CATEGORY',
#     'CONSTRUCTION_STATE': 'CONSTRUCTION_STATE',
#     'STRUCTURE_SECTOR': 'STRUCTURE_SECTOR',
#     'STRUCTURE_MAIN_ACTIVITY': 'STRUCTURE_MAIN_ACTIVITY',
#     'STRUCTURE_SCHOOL_TYPE': 'STRUCTURE_SCHOOL_TYPE',
#     'DISCAPACITY_TYPE': 'DISCAPACITY_TYPE',
#     'NACIONALITY_TYPE': 'NACIONALITY_TYPE',
#     'DISEASE_TYPE': 'DISEASE_TYPE',
#     'RELATIONSHIP_TYPE': 'RELATIONSHIP_TYPE',
#     'CHARACTERISTIC_TYPE': 'CHARACTERISTIC_TYPE',
#     'CHARACTERISTIC_CATEGORY_TYPE': 'CHARACTERISTIC_CATEGORY_TYPE',
# }
#
#
# class NomType(BaseAkModel):
#     type = models.CharField(_('type'), max_length=100, db_column='tipo')
#
#     class Meta:
#         verbose_name = _('Nom Type')
#         verbose_name_plural = _('Nom Types')
#         indexes = [
#             models.Index(fields=['name', 'type']),
#         ]
#         db_table = f'{APP_LABEL.lower()}_tbn_tipo'
#
#     def __str__(self):
#         return f'{self.type} ({self.name})'
#
#
# class Nomenclator(BaseAkModel):
#     type = models.CharField(max_length=100, verbose_name=_('type'), db_column='tipo')
#     nom_type = models.ForeignKey(NomType, on_delete=models.CASCADE,  verbose_name=_('nom type'), db_column='nomenclador')
#
#     class Meta:
#         verbose_name = _('Nomenclator')
#         verbose_name_plural = _('Nomenclators')
#         indexes = [
#             models.Index(fields=['name', 'type']),
#         ]
#         db_table = f'{APP_LABEL.lower()}_tbn_nomenclador'
#
#     def __str__(self):
#         return f'{self.type} ({self.name})'
#
#
# class Province(BaseAkModel):
#     short_name = models.CharField(_('short name'), max_length=50, db_column='nombre_corto')
#     code = models.CharField(_('code'), max_length=50, db_column='codigo')
#
#     class Meta:
#         verbose_name = _('Province')
#         verbose_name_plural = _('Provinces')
#         db_table = f'{APP_LABEL.lower()}_tbn_provincia'
#
#
# class Municipality(BaseAkModel):
#     short_name = models.CharField(_('short name'), max_length=50, db_column='nombre_corto')
#     code = models.CharField(_('code'), max_length=50, db_column='codigo')
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
#
#     class Meta:
#         verbose_name = _('Municipality')
#         verbose_name_plural = _('Municipalities')
#         db_table = f'{APP_LABEL.lower()}_tbn_municipio'
#
# class ImportFile(BaseAkModel):
#     type = models.CharField(max_length=100, verbose_name=_('type'), db_column='tipo')
#     file = models.FileField(upload_to='imports', verbose_name=_('file'), db_column='archivo')
#     description = models.TextField(null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
#     error_file = models.FileField(upload_to='import_error', null=True, blank=True, verbose_name=_('error file'), db_column='fichero_error')
#
#     class Meta:
#         verbose_name = _('Import File')
#         verbose_name_plural = _('Import Files')
#         db_table = f'{APP_LABEL.lower()}_tbn_importacion_archivo'
#
# class BaseType(BaseAkModel):
#     type = models.CharField(max_length=100, unique=True, verbose_name=_('type'), db_column='tipo')
#     description = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name=_('description'), db_column='descripcion')
#
#     class Meta:
#         verbose_name = _('Base')
#         verbose_name_plural = _('Bases')
#         abstract = True
#         indexes = [
#             models.Index(fields=['name', 'type']),
#         ]
#
#     def save(self, *args, **kwargs):
#         try:
#             if not self.type:
#                 type = (self.__class__.__name__ + '_' + self.name).strip().upper()
#                 self.type = type.replace(" ", "_")
#                 try:
#                     if self.municipality:
#                         short_name = self.municipality.short_name + '_' + self.province.short_name
#                         type = (self.__class__.__name__ + '_' + self.name + '_' + short_name).strip().upper()
#                         self.type = type.replace(" ", "_")
#
#                 except AttributeError as e:
#                     pass
#
#             super(BaseType, self).save(*args, **kwargs)
#
#         except IntegrityError as e:
#             raise ('El elemento que trata de registrar ya existe')
#
#
# class BuildingConstructiveStateType(BaseType):
#     """
#         Used in Building
#     """
#
#     class Meta:
#         verbose_name = _('Building Constructive Status')
#         verbose_name_plural = _('Building Constructive Status')
#         db_table = f'{APP_LABEL.lower()}_tbn_estado_constructivo_inmueble'
#
#
# class StructureSectorType(BaseType):
#     """
#         Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Structure Sector')
#         verbose_name_plural = _('Structure Sectors')
#         db_table = f'{APP_LABEL.lower()}_tbn_sector_estructura'
#
#
# class RegimeType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Regime')
#         verbose_name_plural = _('Regimes')
#         db_table = f'{APP_LABEL.lower()}_tbn_regimen'
#
#
# class StructureActivityType(BaseType):
#     """
#         Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Structure Activity')
#         verbose_name_plural = _('Structure Activities')
#         db_table = f'{APP_LABEL.lower()}_tbn_actividad_estructura'
#
#
# class EyesColorType(BaseType):
#     """
#         Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Eyes Color')
#         verbose_name_plural = _('Eyes Colors')
#         db_table = f'{APP_LABEL.lower()}_tbn_color_ojos'
#
#
# class HairColorType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Hair Color')
#         verbose_name_plural = _('Hair Colors')
#         db_table = f'{APP_LABEL.lower()}_tbn_color_pelo'
#
#
# class GenderType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Gender')
#         verbose_name_plural = _('Genders')
#         db_table = f'{APP_LABEL.lower()}_tbn_genero'
#
#
# class SkinColorType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Skin Color')
#         verbose_name_plural = _('Skin Colors')
#         db_table = f'{APP_LABEL.lower()}_tbn_color_piel'
#
#
# class PersonCategoryType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Person Category')
#         verbose_name_plural = _('Person Categories')
#         db_table = f'{APP_LABEL.lower()}_tbn_categoria_persona'
#
#
# class TeachingCategoryType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Teaching Category')
#         verbose_name_plural = _('Teaching Categories')
#         db_table = f'{APP_LABEL.lower()}_tbn_categoria_ensennanza'
#
#
# class TeacherSpecialityType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Teacher Speciality')
#         verbose_name_plural = _('Teacher Specialities')
#         db_table = f'{APP_LABEL.lower()}_tbn_especialidad_ensennanza'
#
#
# class TeacherStatusType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Teacher Status')
#         verbose_name_plural = _('Teacher Status')
#         db_table = f'{APP_LABEL.lower()}_tbn_estado_profesor'
#
#
# class RaceType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Race')
#         verbose_name_plural = _('Races')
#         db_table = f'{APP_LABEL.lower()}_tbn_raza'
#
#
# class StudentStatusType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Student Status')
#         verbose_name_plural = _('Student Status')
#         db_table = f'{APP_LABEL.lower()}_tbn_estado_estudiante'
#
#
# class DiscapacityType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Discapacity')
#         verbose_name_plural = _('Discapacities')
#         db_table = f'{APP_LABEL.lower()}_tbn_discapacidad'
#
#
# class NacionalityType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Nacionality')
#         verbose_name_plural = _('Nacionalities')
#         db_table = f'{APP_LABEL.lower()}_tbn_nacionalidad'
#
#
# class DiseaseType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Disease')
#         verbose_name_plural = _('Diseases')
#         db_table = f'{APP_LABEL.lower()}_tbn_enfermedad'
#
#
# class RelationshipType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Relationship')
#         verbose_name_plural = _('Relationships')
#         db_table = f'{APP_LABEL.lower()}_tbn_parentesco'
#
#
# class EducationLevelType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#     orden = models.PositiveIntegerField(default=0, db_column='orden')
#
#     class Meta:
#         verbose_name = _('Education Level')
#         verbose_name_plural = _('Education Levels')
#         db_table = f'{APP_LABEL.lower()}_tbn_nivel_educativo'
#
# class PatrimonyType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#
#     class Meta:
#         verbose_name = _('Patrimony')
#         verbose_name_plural = _('Patrimonies')
#         db_table = f'{APP_LABEL.lower()}_tbn_patrimonio'
#
#
# class SessionType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#
#     class Meta:
#         verbose_name = _('Session')
#         verbose_name_plural = _('Sessions')
#         db_table = f'{APP_LABEL.lower()}_tbn_sesion'
#
#
# class CompositionType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#
#     class Meta:
#         verbose_name = _('Composition')
#         verbose_name_plural = _('Compositions')
#         db_table = f'{APP_LABEL.lower()}_tbn_composicion'
#
#
# class OrganismType(BaseType):
#     acronym = models.CharField(max_length=10, unique=True, null=True, verbose_name=_('acronym'), db_column='sigla')
#
#     class Meta:
#         verbose_name = _('Organism')
#         verbose_name_plural = _('Organisms')
#         db_table = f'{APP_LABEL.lower()}_tbn_organismo'
#
#
# class EducationalCenterType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#     color = ColorField(default='#FFFFFF')
#     short_name = models.CharField(_('short_name'), max_length=50, db_column='nombre_corto')
#     organism = models.ForeignKey(OrganismType, on_delete=models.SET_NULL, null=True, verbose_name=_('organism'), db_column='id_organismo')
#
#     class Meta:
#         verbose_name = _('Educational Center')
#         verbose_name_plural = _('Educational Centers')
#         db_table = f'{APP_LABEL.lower()}_tbn_centro_educacional'
#
#
# class AcronymType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#
#     class Meta:
#         verbose_name = _('Acronym')
#         verbose_name_plural = _('Acronyms')
#         db_table = f'{APP_LABEL.lower()}_tbn_sigla'
#
#
# class CountryType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#     name_es = models.CharField(_('name_es'),max_length=100, default='', db_column='nombre_es')
#     name_en = models.CharField(_('name_en'),max_length=100, default='', db_column='nombre_en')
#     iso2 = models.CharField(max_length=2, default='', verbose_name=_('iso2'))
#     iso3 = models.CharField(max_length=3, default='', verbose_name=_('iso3'))
#     phone_code = models.IntegerField(default=0, verbose_name=_('phone code'), db_column='codigo_telefonico')
#     capital = models.CharField(null=True, max_length=100, blank=True, verbose_name=_('capital'), db_column='capital')
#     demonym = models.CharField(null=True, max_length=100, blank=True, verbose_name=_('demonym'), db_column='gentilicio')
#     icon_flat = models.ImageField(null=True, blank=True, verbose_name=_('icon flat'), db_column='icono')
#
#     class Meta:
#         verbose_name = _('Country')
#         verbose_name_plural = _('Countries')
#         db_table = f'{APP_LABEL.lower()}_tbn_pais'
#
#
# class CharacteristicType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#
#     class Meta:
#         verbose_name = _('Characteristic')
#         verbose_name_plural = _('Characteristics')
#         db_table = f'{APP_LABEL.lower()}_tbn_caracteristica'
#
#
# class CharacteristicCategoryType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#
#     class Meta:
#         verbose_name = _('Characteristic Category')
#         verbose_name_plural = _('Characteristic Categories')
#         db_table = f'{APP_LABEL.lower()}_tbn_categoria_caracteristica'
#
#
# class AttentionAreaType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
#     municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'), db_column='id_municipio')
#
#     class Meta:
#         verbose_name = _('Attention Area')
#         verbose_name_plural = _('Attention Areas')
#         db_table = f'{APP_LABEL.lower()}_tbn_area_atencion'
#
#
# class HealthCouncilType(BaseType):
#     """
#             Use it on structure/configuration
#     """
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
#     municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'), db_column='id_municipio')
#
#     class Meta:
#         verbose_name = _('Health Council')
#         verbose_name_plural = _('Health Councils')
#         db_table = f'{APP_LABEL.lower()}_tbn_consejo_salud'
#
# class EducationType(BaseType):
#     color = ColorField(default='#FFFFFF')
#     education_levels = models.ManyToManyField(EducationLevelType, through='EducationTypeEducationLevelType', related_name='education_levels')
#     obligatory = models.BooleanField(default=False, verbose_name=_('obligatory'), db_column='obligatorio')
#
#     class Meta:
#         verbose_name = _('Education')
#         verbose_name_plural = _('Educations')
#         db_table = f'{APP_LABEL.lower()}_tbn_educacion'
#
#
# class EducationTypeEducationLevelType(BaseAkModel):
#     education = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name=_('Education'), db_column='id_educacion')
#     education_level = models.ForeignKey(EducationLevelType, on_delete=models.CASCADE, verbose_name=_('Education Level'), db_column='id_nivel_educativo')
#
#     class Meta:
#         verbose_name = _('education_level')
#         db_table = f'{APP_LABEL.lower()}_tbr_educacion__nivel_educativo'
#
# class CategoryOcupationType(BaseType):
#     """
#             Use it on structure/resonsability
#     """
#
#     class Meta:
#         verbose_name = _('Category Occupation')
#         verbose_name_plural = _('Category Occupations')
#         db_table = f'{APP_LABEL.lower()}_tbn_categoria_ocupacional'
#
#
# class ResponsibilityType(BaseType):
#     """
#             Use it on structure/resonsability
#     """
#
#     class Meta:
#         verbose_name = _('Responsibility')
#         verbose_name_plural = _('Responsibilities')
#         db_table = f'{APP_LABEL.lower()}_tbn_responsabilidad'
#     #person_category_id = models.CharField(max_length=100, unique=False, null=True)
#     #categoría_ocupacional = models.CharField(max_length=100, unique=True)
#     #tipo_responsabilidad = models.CharField(max_length=100, unique=True, null=True)
#    # nivel_preparacion = models.CharField(max_length=100, unique=True)
#     #frente_aula = models.BooleanField(null=True, blank=True)
#
#
# class LocationType(BaseType):
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
#     municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'), db_column='id_municipio')
#
#     class Meta:
#         verbose_name = _('Location')
#         verbose_name_plural = _('Locations')
#         db_table = f'{APP_LABEL.lower()}_tbn_localidad'
#
#
# class PopularCouncilType(BaseType):
#     postal_code = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[0-9]+$')], verbose_name=_('postal_code'), db_column='codigo_postal')
#     population = models.IntegerField(null=True, verbose_name=_('population'), db_column='no_poblacion')
#     location = models.ForeignKey(LocationType, on_delete=models.SET_NULL, null=True, verbose_name=_('location'), db_column='id_localidad')
#
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
#     municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'), db_column='id_municipio')
#
#     class Meta:
#         verbose_name = _('Popular Council')
#         verbose_name_plural = _('Popular Councils')
#         db_table = f'{APP_LABEL.lower()}_tbn_consejor_popular'
#
#
# class ProductiveActivityType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Productive Activity')
#         verbose_name_plural = _('Productive Activities')
#         db_table = f'{APP_LABEL.lower()}_tbn_actividad_productiva'
#
#
# class ScholarLevelType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Scholar Level')
#         verbose_name_plural = _('Scholar Levels')
#         db_table = f'{APP_LABEL.lower()}_tbn_nivel_escolar'
#
#
# class ProfessionType(BaseType):
#     """
#             Used in Person
#     """
#     code = models.CharField(_('code'), max_length=50, validators=[RegexValidator(r"[0-9-]+", message="The code is not valid.")], db_column='codigo')
#
#     class Meta:
#         verbose_name = _('Profession')
#         verbose_name_plural = _('Professions')
#         db_table = f'{APP_LABEL.lower()}_tbn_profesion'
#
#
# class AcademicGradeType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Academic Grade')
#         verbose_name_plural = _('Academic Grades')
#         db_table = f'{APP_LABEL.lower()}_tbn_grado_academico'
#
#
# class InvestigativeCategoryType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Investigative Category')
#         verbose_name_plural = _('Investigative Categories')
#         db_table = f'{APP_LABEL.lower()}_tbn_categoria_investigativa'
#
#
# class CivilStateType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Civil Status')
#         verbose_name_plural = _('Civil Status')
#         db_table = f'{APP_LABEL.lower()}_tbn_estado_civil'
#
#
# class PersonType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Person')
#         verbose_name_plural = _('Persons')
#         db_table = f'{APP_LABEL.lower()}_tbn_tipo_persona'
#
#
# class OrphanType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Orphan')
#         verbose_name_plural = _('Orphans')
#         db_table = f'{APP_LABEL.lower()}_tbn_huerfano'
#
#
# class PoliticOrganizationType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Politic Organization')
#         verbose_name_plural = _('Politic Organizations')
#         db_table = f'{APP_LABEL.lower()}_tbn_organizacion_politica'
#
#
# class MasiveOrganizationType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Massive Organization')
#         verbose_name_plural = _('Massive Organizations')
#         db_table = f'{APP_LABEL.lower()}_tbn_organizacion_masiva'
#
#
# class SocialOriginType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('SocialOrigin')
#         verbose_name_plural = _('Social Origins')
#         db_table = f'{APP_LABEL.lower()}_tbn_origen_social'
#
#
# class ValidatedType(BaseType):
#
#     STATUS = (
#         ('YES', _('Yes')),
#         ('NOT', _('No')),
#     )
#     name = models.CharField(_('validated'),
#                                  max_length=50,
#                                  choices=STATUS,
#                                  default='NOT',
#                                  db_column='nombre')
#
#     class Meta:
#         verbose_name = _('Validated')
#         verbose_name_plural = _('Validated')
#
#
#
# class StructureCategoryType(BaseType):
#     """
#             Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Structure Category')
#         verbose_name_plural = _('Structure Categories')
#         db_table = f'{APP_LABEL.lower()}_tbn_categoria_estructura'
#
#
# class StructureLevelType(BaseType):
#     """
#             Used in Structure
#     """
#     category = models.ForeignKey(StructureCategoryType, on_delete=models.SET_NULL, null=True, blank=True, default='', verbose_name=_('category'), db_column='id_categoria_estructura')
#
#     class Meta:
#         verbose_name = _('Structure Level')
#         verbose_name_plural = _('Structure Levels')
#         db_table = f'{APP_LABEL.lower()}_tbn_nivel_estructura'
#
#
# def get_default_level_pk():
#     levels = StructureLevelType.objects.get_or_create(
#         name='Nacional')
#     levels = StructureLevelType.objects.first()
#     if levels is None:
#         data={
#              "name": "Nacional",
#              "is_disable": False
#         }
#         levels=StructureLevelType.objects.create(**data)
#     return levels.pk
#
#
# class SpecialityType(BaseType):
#     """
#             Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Speciality')
#         verbose_name_plural = _('Specialities')
#         db_table = f'{APP_LABEL.lower()}_tbn_especialidad'
#
#
# class BranchType(BaseType):
#     """
#             Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Branch')
#         verbose_name_plural = _('Branches')
#         db_table = f'{APP_LABEL.lower()}_tbn_rama'
#
#
# class LevelTitleType(BaseType):
#     """
#             Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Level Title')
#         verbose_name_plural = _('Level Titles')
#         db_table = f'{APP_LABEL.lower()}_tbn_nivel_titulo'
#
#
# class VinculationType(BaseType):
#     """
#             Used in Structure
#     """
#
#     class Meta:
#         verbose_name = _('Vinculation')
#         verbose_name_plural = _('Vinculations')
#         db_table = f'{APP_LABEL.lower()}_tbn_vinculacion'
#
#
# class FamilyType(BaseType):
#     branch = models.ForeignKey(BranchType, on_delete=models.SET_NULL, null=True, verbose_name=_('branch'), db_column='id_rama')
#
#     class Meta:
#         verbose_name = _('FamilyType')
#         verbose_name_plural = _('FamilyTypes')
#         db_table = f'{APP_LABEL.lower()}_tbn_familia'
# class ProcedureStateType(BaseType):
#     """
#             Used in Person
#     """
#
#     class Meta:
#         verbose_name = _('Procedure Status')
#         verbose_name_plural = _('Procedure Status')
#         db_table = f'{APP_LABEL.lower()}_tbn_estado_tramite'
#
# class SchoolSituationType(BaseType):
#     """
#         Used in Procedure
#     """
#
#     class Meta:
#         verbose_name = _('School Situation')
#         verbose_name_plural = _('School Situations')
#         db_table = f'{APP_LABEL.lower()}_tbn_situacion_escolar'
#
# class EmploymentRelationshipType(BaseType):
#     """
#         Used in Procedure
#     """
#
#     class Meta:
#         verbose_name = _('Employment Relationship')
#         verbose_name_plural = _('Employment Relationships')
#         db_table = f'{APP_LABEL.lower()}_tbn_vinculacion_laboral'
#
# class LaboralSectorType(BaseType):
#     """
#         Used in Procedure
#     """
#
#     class Meta:
#         verbose_name = _('Laboral Sector')
#         verbose_name_plural = _('Laboral Sectors')
#         db_table = f'{APP_LABEL.lower()}_tbn_sector_laboral'
#
# def update_educative_levels_orden_pre_save(sender, instance, **kwargs):
#     try:
#         if not instance.is_disable:
#             old_orden = EducationLevelType.objects.filter(pk=instance.pk).first()
#             if old_orden and not old_orden.is_disable:
#                 update_educative_levels_orden(instance.orden, old_orden.orden, instance.pk)
#             else:
#                 update_educative_levels_orden(instance.orden, None, instance.pk)
#         else:
#             old_orden = EducationLevelType.objects.filter(pk=instance.pk, is_disable=False).values('orden')
#             if old_orden.count() > 0:
#                 update_educative_levels_orden(None, old_orden, instance.pk)
#
#     except Exception as ex:
#         raise Exception("Error update orden in educative levels")
#
#
# def update_educative_levels_orden(new_orden, old_orden, pk):
#     try:
#         if old_orden is None and not pk is None:
#             EducationLevelType.objects.filter(orden__gte=new_orden).exclude(pk=pk).update(orden=F('orden') + 1)
#         elif new_orden is None and not pk is None:
#             EducationLevelType.objects.filter(orden__gte=old_orden).exclude(pk=pk).update(orden=F('orden') - 1)
#         elif new_orden > old_orden and not pk is None:
#             EducationLevelType.objects.filter(orden__range=(old_orden, new_orden)).exclude(pk=pk).update(orden=F('orden')-1)
#         elif new_orden < old_orden and not pk is None:
#             EducationLevelType.objects.filter(orden__range=(new_orden, old_orden)).exclude(pk=pk).update(orden=F('orden')+1)
#
#     except Exception as ex:
#         raise Exception("Error update orden in educative levels")
#
#
# def update_educative_levels_orden_post_delete(sender, instance, **kwargs):
#     try:
#         update_educative_levels_orden(None, instance.orden, instance.pk)
#     except Exception as ex:
#         raise Exception("Error update orden in educative levels")
#
#
#
