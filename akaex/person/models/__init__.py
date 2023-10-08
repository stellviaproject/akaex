from .mdl_educational_worker import EducationalWorker
from .mdl_educational_worker_group import EducationalWorkerGroup
from .mdl_not_educational_worker import NotEducationalWorker
from .mdl_person import Person, person_photo_storage_path
from .mdl_person_discapacity import PersonDiscapacity
from .mdl_person_disease import PersonDisease
from .mdl_person_masive_organization import PersonMasiveOrganization
from .mdl_person_politic_organization import PersonPoliticOrganization
from .mdl_person_structure import PersonStructure
from .mdl_procedure_configuration import ProcedureConfiguration
from .mdl_student import Student
from .mdl_student_group import StudentGroup
from .mdl_student_tutor import StudentTutor
from .mdl_tutor import Tutor
from .mdl_evaluation import Evaluation
from .mdl_years_teaching_experience import YearsTeachingExperience
from .mdl_person_evaluation_by_course import PersonEvaluationByCourse
from .mdl_person_evaluations import PersonEvaluations


from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

# audit Person model
Person.history = AuditlogHistoryField()
auditlog.register(Person)

# audit Tutor model
Tutor.history = AuditlogHistoryField()
auditlog.register(Tutor)

# audit PersonEvaluationByCourse model
PersonEvaluationByCourse.history = AuditlogHistoryField()
auditlog.register(PersonEvaluationByCourse)

# audit YearsTeachingExperience model
YearsTeachingExperience.history = AuditlogHistoryField()
auditlog.register(YearsTeachingExperience)

