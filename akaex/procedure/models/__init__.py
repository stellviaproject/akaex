from .mdl_education_change_procedure import EducationChangeProcedure
from .mdl_legal_tutor import LegalTutor
from .mdl_procedure_reason import ProcedureReason
from .mdl_procedure_student import ProcedureStudent
from .mdl_student_enrollment_procedure import StudentEnrollmentProcedure
from .mdl_student_income_procedure import StudentIncomeProcedure
from .mdl_student_placement import StudentPlacement
from .mdl_student_procedure import StudentProcedure
from .mdl_student_procedure_type import StudentProcedureType
from .mdl_student_registration import (StudentRegistration,
                                       person_photo_storage_path)
from .mdl_student_transfer_procedure import StudentTransferProcedure
from .mdl_way_entry import WayEntry
from .mdl_worker_change_of_functions_pr import WorkerChangeOfFunctionsProcedure
from .mdl_worker_change_of_job_position_pr import WorkerChangeOfJobPositionProcedure
from .mdl_worker_unsubscribement_pr import WorkerUnsubscribementProcedure
from .mdl_worker_economic_lending_pr import WorkerEconomicLendingProcedure
from .mdl_worker_income_procedure import WorkerIncomeProcedure
from .mdl_worker_procedure import WorkerProcedure
from .mdl_worker_registration import WorkerRegistration
from .mdl_worker_transfer_settings import WorkerTransferSettings
from .mdl_teaching_status import TeachingStatus
from .mdl_student_unsubscribement_procedure import StudentUnsubscribementProcedure
from .mdl_group_change_procedure import GroupChangeProcedure
from .mdl_period_change_procedure import PeriodChangeProcedure
from .mdl_student_graduation import StudentGraduation
from .mdl_study_continuity import StudentStudyContinuityProcedure


from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

# audit LegalTutor model
LegalTutor.history = AuditlogHistoryField()
auditlog.register(LegalTutor)

# audit ProcedureStudent model
ProcedureStudent.history = AuditlogHistoryField()
auditlog.register(ProcedureStudent)

# audit StudentProcedure model
StudentProcedure.history = AuditlogHistoryField()
auditlog.register(StudentProcedure)

# audit StudentRegistration model
StudentRegistration.history = AuditlogHistoryField()
auditlog.register(StudentRegistration)

# audit StudentIncomeProcedure model
StudentIncomeProcedure.history = AuditlogHistoryField()
auditlog.register(StudentIncomeProcedure)

# audit StudentEnrollmentProcedure model
StudentEnrollmentProcedure.history = AuditlogHistoryField()
auditlog.register(StudentEnrollmentProcedure)

# audit StudentPlacement model
StudentPlacement.history = AuditlogHistoryField()
auditlog.register(StudentPlacement)

# audit StudentTransferProcedure model
StudentTransferProcedure.history = AuditlogHistoryField()
auditlog.register(StudentTransferProcedure)




