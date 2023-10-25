from import_export import resources
from import_export import resources
from person.models import Person, PersonStructure, Student, EducationalWorker, NotEducationalWorker, Evaluation, StudentGroup, StudentTutor, PersonEvaluations, PersonEvaluationByCourse, YearsTeachingExperience, Tutor, PersonDiscapacity, PersonDisease, EducationalWorkerGroup, PersonMasiveOrganization, PersonPoliticOrganization, ProcedureConfiguration
from evaluation.models import EducativeCenterSpeciality, Cloister, EnrollmentCutEducativeCenter, EnrollmentCutStudents, EnrollmentRegistrationPeriod, EvaluationConcept, FinalGradeRegistry, OrganizativeUnitSpeciality, Professor, ProfessorSchoolGroup, SchoolGroup, SchoolGroupGroupObjectPermission, SchoolGroupUserObjectPermission, SIEnrollmentCut, StudentEvaluation, StudentSchoolGroup, StudyGroup
from structure.models import Structure, Building, StructureBuilding, BuildingCharacteristics, StructureResponsibility, Responsibility, StructureCharacteristics, Characteristics, StructureType, Speciality, SpecialityModality, SpecialityModalityAvtivityEducation, CategoryAttribute, CenterGroup, CharacteristicValue, ConstructionType, ExternalCenter, OrganizatinalUnit, StructureCategory, EducativeCenter, StructureGroupObjectPermission, StructureUserObjectPermission, TeachingGroup
from procedure.models import StudentProcedure, StudentRegistration, EducationChangeProcedure, GroupChangeProcedure, LegalTutor, PeriodChangeProcedure, ProcedureReason, StudentEnrollmentProcedure, StudentGraduation, StudentIncomeProcedure, StudentPlacement, StudentProcedureType, ProcedureStudent, StudentTransferProcedure, StudentUnsubscribementProcedure, StudentStudyContinuityProcedure, WorkerProcedure, WorkerRegistration, WorkerChangeOfFunctionsProcedure, WorkerChangeOfJobPositionProcedure, WorkerEconomicLendingProcedure, WorkerIncomeProcedure, WorkerTransferSettings, WayEntry, TeachingStatus, WorkerUnsubscribementProcedure
from study_plan.models import StudyPlan, StudyPlanVersion, Subject, Discipline, EvaluationWay, DisciplineEvaluation, QualificationRange, EvaluationCategory, EvaluationCulminationStudy, NotLectiveOrganization, NotLectiveSubject, StudyPlanConfiguration, StudyPlanOrganizationEvaluation, SubjectVersionPlan, EvaluationType, SubjectType, StudyModality, CourseType, StudyPlanOrganization, SchoolFrame, AcademicYear, OrganizativeForm, SubjectVersion, SubjectOrganization, SchoolPeriod, EvaluationFormRegistry, EvaluationWayType, OrganizativeFormRegistry, Typology, SchoolFrameRegistry, Cycle, SpecialityStudyPlanConfiguration, Value, ScaleRange, RatingScale, SpecialCapacity, TeachingLevel, RatingScaleRange, Theme

class AcademicYearResource(resources.ModelResource):
    class Meta:
        model = AcademicYear
        fields = ('description','code')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CourseTypeResource(resources.ModelResource):
    class Meta:
        model = CourseType
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CycleResource(resources.ModelResource):
    class Meta:
        model = Cycle
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class DisciplineResource(resources.ModelResource):
    class Meta:
        model = Discipline
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class DisciplineEvaluationResource(resources.ModelResource):
    class Meta:
        model = DisciplineEvaluation
        fields = ('name','study_plan_version','discipline','evaluation_way','evaluation_type','range','evaluation_category')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationCategoryResource(resources.ModelResource):
    class Meta:
        model = EvaluationCategory
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationCulminationStudyResource(resources.ModelResource):
    class Meta:
        model = EvaluationCulminationStudy
        fields = ('name','study_plan_version','evaluation_way','evaluation_type','range','evaluation_category')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationFormRegistryResource(resources.ModelResource):
    class Meta:
        model = EvaluationFormRegistry
        fields = ('name','subject_version','evaluation_way','evaluation_type','range','evaluation_category','amount','order')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationTypeResource(resources.ModelResource):
    class Meta:
        model = EvaluationType
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationWayResource(resources.ModelResource):
    class Meta:
        model = EvaluationWay
        fields = ('description','acronym','evaluation_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationWayTypeResource(resources.ModelResource):
    class Meta:
        model = EvaluationWayType
        fields = ('name','evaluation_type','evaluation_way')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class NotLectiveOrganizationResource(resources.ModelResource):
    class Meta:
        model = NotLectiveOrganization
        fields = ('study_plan_organization','not_lective_subject','academic_year','school_period')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class NotLectiveSubjectResource(resources.ModelResource):
    class Meta:
        model = NotLectiveSubject
        fields = ('name','study_plan_version','subject_type','amount')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class OrganizativeFormResource(resources.ModelResource):
    class Meta:
        model = OrganizativeForm
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class OrganizativeFormRegistryResource(resources.ModelResource):
    class Meta:
        model = OrganizativeFormRegistry
        fields = ('name','subject_version','typology','organizative_form','hours')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class QualificationRangeResource(resources.ModelResource):
    class Meta:
        model = QualificationRange
        fields = ('description','value_type','category','min_value','min_ref','max_value','max_ref','approv_value','approv_ref','decimals')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class RatingScaleResource(resources.ModelResource):
    class Meta:
        model = RatingScale
        fields = ('description','min','max','type','scale_ranges')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class RatingScaleRangeResource(resources.ModelResource):
    class Meta:
        model = RatingScaleRange
        fields = ('rating_scale','scale_range','is_approved')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ScaleRangeResource(resources.ModelResource):
    class Meta:
        model = ScaleRange
        fields = ('min','max','value','acronym','qualification_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SchoolFrameResource(resources.ModelResource):
    class Meta:
        model = SchoolFrame
        fields = ('description','school_frame_registry')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SchoolFrameRegistryResource(resources.ModelResource):
    class Meta:
        model = SchoolFrameRegistry
        fields = ('name','school_frame','academic_year','school_period','cycle','order')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SchoolPeriodResource(resources.ModelResource):
    class Meta:
        model = SchoolPeriod
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SpecialityStudyPlanConfigurationResource(resources.ModelResource):
    class Meta:
        model = SpecialityStudyPlanConfiguration
        fields = ('name','study_plan_configuration','speciality_configuration')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SpecialCapacityResource(resources.ModelResource):
    class Meta:
        model = SpecialCapacity
        fields = ('description','teaching_level')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyModalityResource(resources.ModelResource):
    class Meta:
        model = StudyModality
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyPlanResource(resources.ModelResource):
    class Meta:
        model = StudyPlan
        fields = ('treenode_display_field','speciality','description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyPlanConfigurationResource(resources.ModelResource):
    class Meta:
        model = StudyPlanConfiguration
        fields = ('name','study_plan_version','study_modality','course_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyPlanOrganizationResource(resources.ModelResource):
    class Meta:
        model = StudyPlanOrganization
        fields = ('description','school_frame','study_plan_version','resolution','subject_organization','evaluation')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyPlanOrganizationEvaluationResource(resources.ModelResource):
    class Meta:
        model = StudyPlanOrganizationEvaluation
        fields = ('name','study_plan_organization','evaluation_culmination_study')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyPlanVersionResource(resources.ModelResource):
    class Meta:
        model = StudyPlanVersion
        fields = ('study_plan','description','discipline_subject','discipline_evaluation','evaluation_culmination')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject
        fields = ('description','acronym')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SubjectOrganizationResource(resources.ModelResource):
    class Meta:
        model = SubjectOrganization
        fields = ('name','study_plan_organization','subject','subject_version','subject_type','discipline','academic_year','school_period')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SubjectTypeResource(resources.ModelResource):
    class Meta:
        model = SubjectType
        fields = ('description','color')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SubjectVersionResource(resources.ModelResource):
    class Meta:
        model = SubjectVersion
        fields = ('subject','description','is_average','thematic_plan','school_hours','organizative_form','evaluation_form')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SubjectVersionPlanResource(resources.ModelResource):
    class Meta:
        model = SubjectVersionPlan
        fields = ('name','study_plan_version','discipline','subject','school_hours')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class TeachingLevelResource(resources.ModelResource):
    class Meta:
        model = TeachingLevel
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ThemeResource(resources.ModelResource):
    class Meta:
        model = Theme
        fields = ('description','treenode_display_field')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class TypologyResource(resources.ModelResource):
    class Meta:
        model = Typology
        fields = ('description','acronym','organizative_form')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ValueResource(resources.ModelResource):
    class Meta:
        model = Value
        fields = ('reference_value','range')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class BuildingResource(resources.ModelResource):
    class Meta:
        model = Building
        fields = ('code_building','province','municipality','address','location','popular_council','constructive_state','delivered','use_state','construction_type','patrimony_type','destination','description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class BuildingCharacteristicsResource(resources.ModelResource):
    class Meta:
        model = BuildingCharacteristics
        fields = ('building','characteristics','existence','quantity')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CategoryAttributeResource(resources.ModelResource):
    class Meta:
        model = CategoryAttribute
        fields = ()
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CenterGroupResource(resources.ModelResource):
    class Meta:
        model = CenterGroup
        fields = ('group','educatinal_center','organizatinal_unit')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CharacteristicsResource(resources.ModelResource):
    class Meta:
        model = Characteristics
        fields = ('characteristic_type','characteristic_category_type','structure_type','description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CharacteristicValueResource(resources.ModelResource):
    class Meta:
        model = CharacteristicValue
        fields = ('characteristic','value')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ConstructionTypeResource(resources.ModelResource):
    class Meta:
        model = ConstructionType
        fields = ('description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ExternalCenterResource(resources.ModelResource):
    class Meta:
        model = ExternalCenter
        fields = ('educational_center_type','province','municipality','description','forming_organism')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class OrganizatinalUnitResource(resources.ModelResource):
    class Meta:
        model = OrganizatinalUnit
        fields = ('center_type','educatinal_center','description','specialities')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ResponsibilityResource(resources.ModelResource):
    class Meta:
        model = Responsibility
        fields = ('occupational_category','description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SpecialityResource(resources.ModelResource):
    class Meta:
        model = Speciality
        fields = ('short_name','description','is_mined_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SpecialityModalityResource(resources.ModelResource):
    class Meta:
        model = SpecialityModality
        fields = ('speciality','speciality_type','code','family','branch','activity_education_level')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SpecialityModalityAvtivityEducationResource(resources.ModelResource):
    class Meta:
        model = SpecialityModalityAvtivityEducation
        fields = ('name','speciality','activity','education_type','education_level_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureResource(resources.ModelResource):
    class Meta:
        model = Structure
        fields = ('id', 'history','treenode_display_field','type','country','province','municipality','building','responsibility','characteristics','address','popular_council','location_type','educational_center_type','session_type','regime','location','code','health_council','attention_area','plan_turquino','university_seat','email','is_mixed','is_rural','is_closed','description','phone','main_phone','extra_field','is_validated','specialities','category','vinculation')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureBuildingResource(resources.ModelResource):
    class Meta:
        model = StructureBuilding
        fields = ('structure','building')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureCategoryResource(resources.ModelResource):
    class Meta:
        model = StructureCategory
        fields = ('attribute')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureCharacteristicsResource(resources.ModelResource):
    class Meta:
        model = StructureCharacteristics
        fields = ('structure','characteristics','existence','quantity')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EducativeCenterResource(resources.ModelResource):
    class Meta:
        model = EducativeCenter
        fields = ()
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureGroupObjectPermissionResource(resources.ModelResource):
    class Meta:
        model = StructureGroupObjectPermission
        fields = ('name','content_object')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureResponsibilityResource(resources.ModelResource):
    class Meta:
        model = StructureResponsibility
        fields = ('structure','responsibility','amount','ocupada')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureTypeResource(resources.ModelResource):
    class Meta:
        model = StructureType
        fields = ('code','admit_child','color','short_name','category','level')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StructureUserObjectPermissionResource(resources.ModelResource):
    class Meta:
        model = StructureUserObjectPermission
        fields = ('name','content_object')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class TeachingGroupResource(resources.ModelResource):
    class Meta:
        model = TeachingGroup
        fields = ('structure')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EducationChangeProcedureResource(resources.ModelResource):
    class Meta:
        model = EducationChangeProcedure
        fields = ('student_procedure','center_date','center_order','made_by_person','destination_municipality','municipality_date_change','municipality_order','municipality_approval_person','destination_province','province_date_change','province_order','province_approval_person','procedure_reason','forming_organism','educational_center_type','educational_center','external_center','education','speciality','typification','description','school_situation','url_doc','doc')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class GroupChangeProcedureResource(resources.ModelResource):
    class Meta:
        model = GroupChangeProcedure
        fields = ('student_procedure','origen_course','origen_group','destination_course','destination_group')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class LegalTutorResource(resources.ModelResource):
    class Meta:
        model = LegalTutor
        fields = ('name','legal_tutor','relationship','employment_relationship','social_origin','workplace','laboral_sector','formalized','description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PeriodChangeProcedureResource(resources.ModelResource):
    class Meta:
        model = PeriodChangeProcedure
        fields = ('student_procedure','origen_year','destination_year','origen_period','destination_period','destination_course')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ProcedureReasonResource(resources.ModelResource):
    class Meta:
        model = ProcedureReason
        fields = ('name','procedures','description','status')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ProcedureStudentResource(resources.ModelResource):
    class Meta:
        model = ProcedureStudent
        fields = ('name','person','legal_tutors','discapacity','orphan','diseases')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentEnrollmentProcedureResource(resources.ModelResource):
    class Meta:
        model = StudentEnrollmentProcedure
        fields = ('name','student_procedure','origin_center','way_of_entry','enrollment_date','doc')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentGraduationResource(resources.ModelResource):
    class Meta:
        model = StudentGraduation
        fields = ('student_procedure','certification_group')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentIncomeProcedureResource(resources.ModelResource):
    class Meta:
        model = StudentIncomeProcedure
        fields = ('student_procedure','date','doc')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentPlacementResource(resources.ModelResource):
    class Meta:
        model = StudentPlacement
        fields = ('student_procedure','origin_center','procedure_reason','external_center','origin_municipality','origin_province','organism','speciality','origin','doc')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentProcedureResource(resources.ModelResource):
    class Meta:
        model = StudentProcedure
        fields = ('student_registration','second_name','first_last_name','second_last_name','ci','student_procedure_type','school_center','school_situation','photo','processor_person_id','start_date','end_date','state','previous_procedure')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentProcedureTypeResource(resources.ModelResource):
    class Meta:
        model = StudentProcedureType
        fields = ('description','changes_state','changes_scholar_situation','changes_structure','initial_states','final_state','school_situations','procedure_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentRegistrationResource(resources.ModelResource):
    class Meta:
        model = StudentRegistration
        fields = ('student','nationality','school_center','speciality','school_period','study_plan_organization','study_modality','course_type','category','state','school_situation','enrollment_condition','included','way_entry','enrollment_tome','enrollment_folio','enrollment_number','current_school_course','previous_procedure','procedure_type','academic_year','photo','study_group','study_plan_version','session','activity','education_type','education_level_type','organizational_unit')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentTransferProcedureResource(resources.ModelResource):
    class Meta:
        model = StudentTransferProcedure
        fields = ('name','student_procedure','center_date','municipality_date','province_date','center_order_number','municipality_order_number','province_order_number','center_approval_person','municipality_approval_person','province_approval_person','procedure_reason','destination_province','destination_municipality','destination_center','description','doc')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentUnsubscribementProcedureResource(resources.ModelResource):
    class Meta:
        model = StudentUnsubscribementProcedure
        fields = ('name','student_procedure','procedure_reason','unsubscribement_date','center_date','center_order','made','municipality_date','municipality_order','approved_municipality','province_date','province_order','approved_province','description','doc')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentStudyContinuityProcedureResource(resources.ModelResource):
    class Meta:
        model = StudentStudyContinuityProcedure
        fields = ('name','student_procedure','external_speciality','educational_center','external_center','forming_organism','speciality','continuity_course')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class TeachingStatusResource(resources.ModelResource):
    class Meta:
        model = TeachingStatus
        fields = ('name','color','description','type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WayEntryResource(resources.ModelResource):
    class Meta:
        model = WayEntry
        fields = ('name','description')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerChangeOfFunctionsProcedureResource(resources.ModelResource):
    class Meta:
        model = WorkerChangeOfFunctionsProcedure
        fields = ('worker_procedure','change_functions_start_date','change_functions_end_date','function')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerChangeOfJobPositionProcedureResource(resources.ModelResource):
    class Meta:
        model = WorkerChangeOfJobPositionProcedure
        fields = ('worker_procedure','date','worker_registration')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerEconomicLendingProcedureResource(resources.ModelResource):
    class Meta:
        model = WorkerEconomicLendingProcedure
        fields = ('worker_procedure','economic_lending_start_date','economic_lending_end_date','inactivity_period','reason')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerIncomeProcedureResource(resources.ModelResource):
    class Meta:
        model = WorkerIncomeProcedure
        fields = ('worker_procedure','date','worker_income_type','origin')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerProcedureResource(resources.ModelResource):
    class Meta:
        model = WorkerProcedure
        fields = ('worker_registration','structure','responsibility','start_date','end_date','state','previous_procedure','processor_person_id','procedure_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerRegistrationResource(resources.ModelResource):
    class Meta:
        model = WorkerRegistration
        fields = ('person','structure','responsibility','category','contract','qualified','does_study','professional','member_of_directors_board','state','occupied_position','previous_procedure','procedure_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerTransferSettingsResource(resources.ModelResource):
    class Meta:
        model = WorkerTransferSettings
        fields = ('worker_procedure','worker_unsubscribement_date')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class WorkerUnsubscribementProcedureResource(resources.ModelResource):
    class Meta:
        model = WorkerUnsubscribementProcedure
        fields = ('worker_procedure','date','worker_unsubscribement_type','worker_unsubscribement_reason')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EducationalWorkerResource(resources.ModelResource):
    class Meta:
        model = EducationalWorker
        fields = ('name','structure','person','teaching_category','specialty','teaching_status','scientific_grade','research_category','profession','groups')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EducationalWorkerGroupResource(resources.ModelResource):
    class Meta:
        model = EducationalWorkerGroup
        fields = ('name','teacher','group','structure')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationResource(resources.ModelResource):
    class Meta:
        model = Evaluation
        fields = ('name','acronym')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class NotEducationalWorkerResource(resources.ModelResource):
    class Meta:
        model = NotEducationalWorker
        fields = ('name','structure','person','profession')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = ('second_name','first_last_name','second_last_name','ci','ci_serie','date_of_birth','photo','address','address_province','address_municipality','address_popular_council','address_location','email','mobile_phone','phone','gender','race','height','weight','scholar_level','teaching_category','profession','academic_grade','investigative_category','extra_field','user','structures','educational_workers','not_educational_workers','students')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonDiscapacityResource(resources.ModelResource):
    class Meta:
        model = PersonDiscapacity
        fields = ('name','person','discapacity')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonDiseaseResource(resources.ModelResource):
    class Meta:
        model = PersonDisease
        fields = ('name','person','disease')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonEvaluationsResource(resources.ModelResource):
    class Meta:
        model = PersonEvaluations
        fields = ('person_evaluation_by_course','person_years_teaching_experience')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonEvaluationByCourseResource(resources.ModelResource):
    class Meta:
        model = PersonEvaluationByCourse
        fields = ('person','course','evaluation')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonMasiveOrganizationResource(resources.ModelResource):
    class Meta:
        model = PersonMasiveOrganization
        fields = ('name','person','organization')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonPoliticOrganizationResource(resources.ModelResource):
    class Meta:
        model = PersonPoliticOrganization
        fields = ('name','person','organization')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class PersonStructureResource(resources.ModelResource):
    class Meta:
        model = PersonStructure
        fields = ('name','person','category','structure','category_order')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ProcedureConfigurationResource(resources.ModelResource):
    class Meta:
        model = ProcedureConfiguration
        fields = ('name','changes_state','changes_scholar_situation','changes_structure','initials_procedure_states','final_procedure_state')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ('name','no_expedient','structure','person','status','tutor','productive_activity','groups','tutors')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentGroupResource(resources.ModelResource):
    class Meta:
        model = StudentGroup
        fields = ('name','student','group','structure')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentTutorResource(resources.ModelResource):
    class Meta:
        model = StudentTutor
        fields = ('name','student','tutor','structure')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class TutorResource(resources.ModelResource):
    class Meta:
        model = Tutor
        fields = ('full_name','relationship','ci','work_center','social_origin','phone')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class YearsTeachingExperienceResource(resources.ModelResource):
    class Meta:
        model = YearsTeachingExperience
        fields = ('person','evaluations')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class CloisterResource(resources.ModelResource):
    class Meta:
        model = Cloister
        fields = ('course','center','unity')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EducativeCenterSpecialityResource(resources.ModelResource):
    class Meta:
        model = EducativeCenterSpeciality
        fields = ('name','educative_center','educative_level','education','tipification','speciality')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EnrollmentCutEducativeCenterResource(resources.ModelResource):
    class Meta:
        model = EnrollmentCutEducativeCenter
        fields = ('enrollment_cut','educative_center','speciality_configuration','date','course_type')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EnrollmentCutStudentsResource(resources.ModelResource):
    class Meta:
        model = EnrollmentCutStudents
        fields = ('enrollment_cut_educative_center','student_registration','school_situation','study_group','academic_year','school_period')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EnrollmentRegistrationPeriodResource(resources.ModelResource):
    class Meta:
        model = EnrollmentRegistrationPeriod
        fields = ('enrollment_cut','course','closing_date')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class EvaluationConceptResource(resources.ModelResource):
    class Meta:
        model = EvaluationConcept
        fields = ('description','acronym')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class FinalGradeRegistryResource(resources.ModelResource):
    class Meta:
        model = FinalGradeRegistry
        fields = ('person','student_registration','student_evaluation','course','study_plan_organization','speciality_configuration','subject_version','academic_year','school_period','processor_person_id','grade','reference_value','evaluation_form_registry','evaluation_concept','evaluation_status')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class OrganizativeUnitSpecialityResource(resources.ModelResource):
    class Meta:
        model = OrganizativeUnitSpeciality
        fields = ('name','organizative_unit','educative_level','education','tipification','speciality')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ProfessorResource(resources.ModelResource):
    class Meta:
        model = Professor
        fields = ('worker','subjects','cloister')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class ProfessorSchoolGroupResource(resources.ModelResource):
    class Meta:
        model = ProfessorSchoolGroup
        fields = ('school_group','professor','principal')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SchoolGroupResource(resources.ModelResource):
    class Meta:
        model = SchoolGroup
        fields = ('educative_center','organizational_unit','subject_version','subject_type','study_plan_organization','academic_year','school_period','study_group','course','group_type','group_state')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SchoolGroupGroupObjectPermissionResource(resources.ModelResource):
    class Meta:
        model = SchoolGroupGroupObjectPermission
        fields = ('name','content_object')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SchoolGroupUserObjectPermissionResource(resources.ModelResource):
    class Meta:
        model = SchoolGroupUserObjectPermission
        fields = ('name','content_object')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class SIEnrollmentCutResource(resources.ModelResource):
    class Meta:
        model = SIEnrollmentCut
        fields = ('enrollment_cut_educative_center','educative_center','education_level','education','activity','course_type','school_situation','study_group','academic_year','school_period','speciality','enrollment_condition','province','municipality','gender','included','disease','center_type','turquino_plan','is_mixed','is_rural','vinculation','nationality','atomic_total')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentEvaluationResource(resources.ModelResource):
    class Meta:
        model = StudentEvaluation
        fields = ('student_registration','school_group','professor','grade','reference_value','evaluation_form_registry','evaluation_concept','processor_person_id')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudentSchoolGroupResource(resources.ModelResource):
    class Meta:
        model = StudentSchoolGroup
        fields = ('school_group','student_registration','placement_concept')
    def dehydrate_id(self, obj):
        return str(obj.id)
    

class StudyGroupResource(resources.ModelResource):
    class Meta:
        model = StudyGroup
        fields = ('speciality','course_type','academic_year','short_name')
    def dehydrate_id(self, obj):
        return str(obj.id)
    
