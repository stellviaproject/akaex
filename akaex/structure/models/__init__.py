from .mdl_building import Building
from .mdl_characteristics import Characteristics
from .mdl_characteristic_value import CharacteristicValue
from .mdl_building_characteristics import BuildingCharacteristics
from .mdl_category_attribute import CategoryAttribute
from .mdl_constrction_type import ConstructionType
from .mdl_responsibility import Responsibility
from .mdl_structure_type import StructureType
from .mdl_structure_category import StructureCategory
from .mdl_speciality_modality import SpecialityModality
from .mdl_speciality_modality_avtivity_education import SpecialityModalityAvtivityEducation
from .mdl_structure import Structure
from .mdl_external_center import ExternalCenter
from .mdl_structure_user_object_permission import StructureUserObjectPermission
from .mdl_structure_group_object_permission import StructureGroupObjectPermission
from .mdl_structure_responsibility import StructureResponsibility
from .mdl_structure_building import StructureBuilding
from .mdl_structure_characteristics import StructureCharacteristics
from .mdl_teaching_group import TeachingGroup
from .mdl_structure_eductive_center_type import EducativeCenter
from .mdl_speciality import Speciality
from .mdl_organizational_unit import OrganizatinalUnit
from .mdl_cenetr_group import CenterGroup


from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog


# audit StructureUserObjectPermission model
StructureUserObjectPermission.history = AuditlogHistoryField()
auditlog.register(StructureUserObjectPermission)

# audit StructureGroupObjectPermission model
StructureGroupObjectPermission.history = AuditlogHistoryField()
auditlog.register(StructureGroupObjectPermission)

# audit Building model
Building.history = AuditlogHistoryField()
auditlog.register(Building)

# audit Structure model
Structure.history = AuditlogHistoryField()
auditlog.register(Structure)

# audit StructureType model
StructureType.history = AuditlogHistoryField()
auditlog.register(StructureType)

# audit StructureCategory model
StructureCategory.history = AuditlogHistoryField()
auditlog.register(StructureCategory)

# audit EducativeCenter model
EducativeCenter.history = AuditlogHistoryField()
auditlog.register(EducativeCenter)

# audit Speciality model
Speciality.history = AuditlogHistoryField()
auditlog.register(Speciality)

# audit CenterGroup model
CenterGroup.history = AuditlogHistoryField()
auditlog.register(CenterGroup)

# audit ExternalCenter model
ExternalCenter.history = AuditlogHistoryField()
auditlog.register(ExternalCenter)

# audit SpecialityModality model
SpecialityModality.history = AuditlogHistoryField()
auditlog.register(SpecialityModality)

# audit StructureResponsibility model
StructureResponsibility.history = AuditlogHistoryField()
auditlog.register(StructureResponsibility)

# audit StructureBuilding model
StructureBuilding.history = AuditlogHistoryField()
auditlog.register(StructureBuilding)

# audit OrganizatinalUnit model
OrganizatinalUnit.history = AuditlogHistoryField()
auditlog.register(OrganizatinalUnit)

# audit StructureCharacteristics model
StructureCharacteristics.history = AuditlogHistoryField()
auditlog.register(StructureCharacteristics)

# audit TeachingGroup model
TeachingGroup.history = AuditlogHistoryField()
auditlog.register(TeachingGroup)

# audit Responsibility model
Responsibility.history = AuditlogHistoryField()
auditlog.register(Responsibility)

# audit Characteristics model
Characteristics.history = AuditlogHistoryField()
auditlog.register(Characteristics)

# audit BuildingCharacteristics model
BuildingCharacteristics.history = AuditlogHistoryField()
auditlog.register(BuildingCharacteristics)

# audit CategoryAttribute model
CategoryAttribute.history = AuditlogHistoryField()
auditlog.register(CategoryAttribute)

# audit ConstructionType model
ConstructionType.history = AuditlogHistoryField()
auditlog.register(ConstructionType)