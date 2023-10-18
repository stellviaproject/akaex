from .excel import excel_bytes_to_queryset, queryset_to_excel_bytes
from .zip import zip_files, unzip_files
from django.db import models
from structure.models import Structure, Building, StructureBuilding, BuildingCharacteristics, StructureResponsibility, Responsibility, StructureCharacteristics, Characteristics, StructureType, Speciality, SpecialityModality, SpecialityModalityAvtivityEducation
from person.models import Person, PersonStructure, Student, EducationalWorker, NotEducationalWorker, Evaluation, StudentGroup, StudentTutor, PersonEvaluations, PersonEvaluationByCourse, YearsTeachingExperience, Tutor, PersonDiscapacity, PersonDisease, EducationalWorkerGroup, PersonMasiveOrganization, PersonPoliticOrganization
from procedure.models import StudentProcedure, StudentRegistration, EducationChangeProcedure, GroupChangeProcedure, LegalTutor, PeriodChangeProcedure, ProcedureReason, StudentEnrollmentProcedure, StudentGraduation, StudentIncomeProcedure, StudentPlacement, StudentProcedureType, ProcedureStudent, StudentTransferProcedure, StudentUnsubscribementProcedure, StudentStudyContinuityProcedure, WorkerProcedure, WorkerRegistration, WorkerChangeOfFunctionsProcedure, WorkerChangeOfJobPositionProcedure, WorkerEconomicLendingProcedure, WorkerIncomeProcedure, WorkerTransferSettings, WayEntry, TeachingStatus, WorkerUnsubscribementProcedure
from evaluation.models import EducativeCenterSpeciality
from study_plan.models import StudyPlan, StudyPlanVersion, Subject, Discipline, EvaluationWay, DisciplineEvaluation, QualificationRange, EvaluationCategory, EvaluationCulminationStudy, NotLectiveOrganization, NotLectiveSubject, StudyPlanConfiguration, StudyPlanOrganizationEvaluation, SubjectVersionPlan, EvaluationType, SubjectType, StudyModality, CourseType, StudyPlanOrganization, SchoolFrame, AcademicYear, OrganizativeForm, SubjectVersion, SubjectOrganization, SchoolPeriod, EvaluationFormRegistry, EvaluationWayType, OrganizativeFormRegistry, Typology, SchoolFrameRegistry, Cycle, SpecialityStudyPlanConfiguration, Value

def name_of_set(m:models.Model):
    return m._meta.model_name

MODELS = {
    name_of_set(Structure): Structure,
    name_of_set(PersonStructure): PersonStructure,
    name_of_set(Person): Person,
    name_of_set(Student): Student,
    name_of_set(EducationalWorker): EducationalWorker,
    name_of_set(NotEducationalWorker): NotEducationalWorker,
    name_of_set(StudentGroup): StudentGroup,
    name_of_set(StudentTutor): StudentTutor,
    name_of_set(Tutor): Tutor,
    name_of_set(PersonEvaluationByCourse): PersonEvaluationByCourse,
    name_of_set(Evaluation): Evaluation,
    name_of_set(PersonEvaluations): PersonEvaluations,
    name_of_set(YearsTeachingExperience): YearsTeachingExperience,
    name_of_set(PersonDiscapacity): PersonDiscapacity,
    name_of_set(PersonDisease): PersonDisease,
    name_of_set(PersonMasiveOrganization): PersonMasiveOrganization,
    name_of_set(PersonPoliticOrganization): PersonPoliticOrganization,
    name_of_set(EducationalWorkerGroup): EducationalWorkerGroup,
    name_of_set(StudentProcedure): StudentProcedure,
    name_of_set(ProcedureStudent): ProcedureStudent,
    name_of_set(StudentRegistration): StudentRegistration,
    name_of_set(StudentProcedureType): StudentProcedureType,
    name_of_set(EducationChangeProcedure): EducationChangeProcedure,
    name_of_set(GroupChangeProcedure): GroupChangeProcedure,
    name_of_set(StudentEnrollmentProcedure): StudentEnrollmentProcedure,
    name_of_set(StudentGraduation): StudentGraduation,
    name_of_set(StudentIncomeProcedure): StudentIncomeProcedure,
    name_of_set(StudentPlacement): StudentPlacement,
    name_of_set(StudentTransferProcedure): StudentTransferProcedure,
    name_of_set(StudentUnsubscribementProcedure): StudentUnsubscribementProcedure,
    name_of_set(StudentStudyContinuityProcedure): StudentStudyContinuityProcedure,
    name_of_set(TeachingStatus): TeachingStatus,
    name_of_set(WayEntry): WayEntry,
    name_of_set(ProcedureReason): ProcedureReason,
    name_of_set(LegalTutor): LegalTutor,
    name_of_set(WorkerProcedure): WorkerProcedure,
    name_of_set(WorkerRegistration): WorkerRegistration,
    name_of_set(WorkerChangeOfFunctionsProcedure): WorkerChangeOfFunctionsProcedure,
    name_of_set(WorkerChangeOfJobPositionProcedure): WorkerChangeOfJobPositionProcedure,
    name_of_set(WorkerTransferSettings): WorkerTransferSettings,
    name_of_set(WorkerUnsubscribementProcedure): WorkerUnsubscribementProcedure,
    name_of_set(Speciality): Speciality,
    name_of_set(SpecialityModality): SpecialityModality,
    name_of_set(SpecialityModalityAvtivityEducation): SpecialityModalityAvtivityEducation,
    name_of_set(StudyPlan): StudyPlan,
    name_of_set(StudyPlanVersion): StudyPlanVersion,
    name_of_set(Subject): Subject,
    name_of_set(Discipline): Discipline,
    name_of_set(EvaluationWay): EvaluationWay,
    name_of_set(DisciplineEvaluation): DisciplineEvaluation,
    name_of_set(QualificationRange): QualificationRange,
    name_of_set(EvaluationCategory): EvaluationCategory,
    name_of_set(EvaluationType): EvaluationType,
    name_of_set(EvaluationCulminationStudy): EvaluationCulminationStudy,
    name_of_set(NotLectiveSubject): NotLectiveSubject,
    name_of_set(SubjectType): SubjectType,
    name_of_set(StudyPlanConfiguration): StudyPlanConfiguration,
    name_of_set(StudyModality): StudyModality,
    name_of_set(CourseType): CourseType,
    name_of_set(StudyPlanOrganization): StudyPlanOrganization,
    name_of_set(SchoolFrame): SchoolFrame,
    name_of_set(AcademicYear): AcademicYear,
    name_of_set(SubjectVersionPlan): SubjectVersionPlan,
    name_of_set(SubjectVersion): SubjectVersion,
    name_of_set(OrganizativeForm): OrganizativeForm,
    name_of_set(SubjectOrganization): SubjectOrganization,
    name_of_set(SchoolPeriod): SchoolPeriod,
    name_of_set(EvaluationFormRegistry): EvaluationFormRegistry,
    name_of_set(EvaluationWayType): EvaluationWayType,
    name_of_set(NotLectiveOrganization): NotLectiveOrganization,
    name_of_set(OrganizativeFormRegistry): OrganizativeFormRegistry,
    name_of_set(Typology): Typology,
    name_of_set(StudyPlanOrganizationEvaluation): StudyPlanOrganizationEvaluation,
    name_of_set(SchoolFrameRegistry): SchoolFrameRegistry,
    name_of_set(Cycle): Cycle,
    name_of_set(SpecialityStudyPlanConfiguration): SpecialityStudyPlanConfiguration,
    name_of_set(Value): Value,
    name_of_set(QualificationRange): QualificationRange,
}

def export_zip(data):
    files = {}
    for name, bytes in data.items():
        files[name] = queryset_to_excel_bytes(bytes)
    return zip_files(files)

def import_zip(data):
    pass