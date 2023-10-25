from django.db.models import QuerySet
from evaluation.models import EducativeCenterSpeciality
from structure.models import Structure, Building, StructureBuilding, BuildingCharacteristics, StructureResponsibility, Responsibility, StructureCharacteristics, Characteristics, StructureType, Speciality, SpecialityModality, SpecialityModalityAvtivityEducation
from person.models import Person, PersonStructure, Student, EducationalWorker, NotEducationalWorker, Evaluation, StudentGroup, StudentTutor, PersonEvaluations, PersonEvaluationByCourse, YearsTeachingExperience, Tutor, PersonDiscapacity, PersonDisease, EducationalWorkerGroup, PersonMasiveOrganization, PersonPoliticOrganization
from study_plan.models import StudyPlan, StudyPlanVersion, Subject, Discipline, EvaluationWay, DisciplineEvaluation, QualificationRange, EvaluationCategory, EvaluationCulminationStudy, NotLectiveOrganization, NotLectiveSubject, StudyPlanConfiguration, StudyPlanOrganizationEvaluation, SubjectVersionPlan, EvaluationType, SubjectType, StudyModality, CourseType, StudyPlanOrganization, SchoolFrame, AcademicYear, OrganizativeForm, SubjectVersion, SubjectOrganization, SchoolPeriod, EvaluationFormRegistry, EvaluationWayType, OrganizativeFormRegistry, Typology, SchoolFrameRegistry, Cycle, SpecialityStudyPlanConfiguration, Value
from procedure.models import StudentProcedure, StudentRegistration, EducationChangeProcedure, GroupChangeProcedure, LegalTutor, PeriodChangeProcedure, ProcedureReason, StudentEnrollmentProcedure, StudentGraduation, StudentIncomeProcedure, StudentPlacement, StudentProcedureType, ProcedureStudent, StudentTransferProcedure, StudentUnsubscribementProcedure, StudentStudyContinuityProcedure, WorkerProcedure, WorkerRegistration, WorkerChangeOfFunctionsProcedure, WorkerChangeOfJobPositionProcedure, WorkerEconomicLendingProcedure, WorkerIncomeProcedure, WorkerTransferSettings, WayEntry, TeachingStatus, WorkerUnsubscribementProcedure

def query_struct(struct_id):
    ## Extract all info from structure##
    #obtener la estructura con el id o nombre
    structure = Structure.objects.get(id=struct_id)
    ##Extract all info related to person##
    #Structure -> PersonStructure -> Person
    person_structures = structure.personstructure_set.all()
    persons = Person.objects.filter(personstructure__structure=structure)
    #Person -> Student
    students = Student.objects.filter(person__in=persons)
    #Person -> EducationalWorker
    educational_workers = EducationalWorker.objects.filter(person__in=persons)
    #Person -> NotEducationalWorker
    not_educational_workers = NotEducationalWorker.objects.filter(person__in=persons)
    #Student -> StudentGroups
    student_groups = StudentGroup.objects.filter(student__in=students)
    #Student -> StudentTutor
    student_tutors = StudentTutor.objects.filter(student__in=students)
    #Student -> Tutor
    tutors = Tutor.objects.filter(studenttutor__student__in=students)
    #Person -> PersonEvaluationByCourses
    person_evaluation_by_courses = PersonEvaluationByCourse.objects.filter(person__in=persons)
    #PersonEvaluationByCourses -> Evaluation
    evaluations = Evaluation.objects.filter(personevaluationbycourse__in=person_evaluation_by_courses)
    #PersonEvaluationByCourses -> PersonEvaluation
    person_evaluations = PersonEvaluations.objects.filter(person_evaluation_by_course__in=person_evaluation_by_courses)
    #PersonEvaluation -> YearsTeachingExperiences
    years_teaching_experiences = YearsTeachingExperience.objects.filter(person__in=persons)
    #Person -> PersonDiscapacity
    person_discapacities = PersonDiscapacity.objects.filter(person__in=persons)
    #Person -> PersonDisease
    person_diseases = PersonDisease.objects.filter(person__in=persons)
    #Person -> PersonMasiveOrganization
    person_masive_organizations = PersonMasiveOrganization.objects.filter(person__in=persons)
    #Person -> PersonPoliticOrganization
    person_politic_organization = PersonPoliticOrganization.objects.filter(person__in=persons)
    #EducationalWorker -> EducationalWorkerGroup
    educational_worker_groups = EducationalWorkerGroup.objects.filter(teacher__in=educational_workers)
    
    ##Extract all info related to procedure##
    #Structure -> StudentProcedure
    student_procedures = StudentProcedure.objects.filter(school_center=structure)
    #Person -> ProcedureStudent
    procedure_students = ProcedureStudent.objects.filter(person__in=persons)
    #ProcedureStudent -> StudentRegistration
    student_registrations = StudentRegistration.objects.filter(student__in=procedure_students)
    student_registrations_way_entries = WayEntry.objects.filter(studentregistration__in=student_registrations)
    student_registrations_teaching_status = TeachingStatus.objects.filter(studentregistration__in=student_registrations)
    #StudentProcedure -> StudentProcedureType
    student_procedure_types = StudentProcedureType.objects.filter(studentprocedure__in=student_procedures)
    student_procedure_initial_teaching_status = TeachingStatus.objects.filter(initial_states__in=student_procedure_types)
    #Nota: no se puede extraer porque se obtiene
    #Cannot resolve keyword 'final_state' into field.
    #student_procedure_final_teaching_status = TeachingStatus.objects.filter(final_state__in=student_procedure_types)
    
    #StudentProcedure -> EducationChangeProcedure
    education_change_procedures = EducationChangeProcedure.objects.filter(student_procedure__in=student_procedures)
    education_change_procedure_reasons = ProcedureReason.objects.filter(educationchangeprocedure__in=education_change_procedures)
    #StudentProcedure -> GroupChangeProcedure
    group_change_procedures = GroupChangeProcedure.objects.filter(student_procedure__in=student_procedures)
    #StudentProcedure -> PeriodChangeProcedure
    period_change_procedures = PeriodChangeProcedure.objects.filter(student_procedure__in=student_procedures)
    #StudentProcedure -> StudentEnrollmentProcedure
    student_enrollment_procedures = StudentEnrollmentProcedure.objects.filter(student_procedure__in=student_procedures)
    student_enrollment_procedure_way_entries = WayEntry.objects.filter(studentenrollmentprocedure__in=student_enrollment_procedures)
    #StudentProcedure -> StudentGraduation
    student_graduations = StudentGraduation.objects.filter(student_procedure__in=student_procedures)
    #StudentProcedure -> StudentIncomeProcedure
    student_income_procedures = StudentIncomeProcedure.objects.filter(student_procedure__in=student_procedures)
    #StudentProcedure -> StudentPlacement
    student_placements = StudentPlacement.objects.filter(student_procedure__in=student_procedures)
    student_placement_reasons = ProcedureReason.objects.filter(studentplacement__in=student_placements)
    #StudentProcedure -> StudentTransferProcedure
    student_transfer_procedures = StudentTransferProcedure.objects.filter(student_procedure__in=student_procedures)
    student_transfer_procedure_reasons = ProcedureReason.objects.filter(studenttransferprocedure__in=student_transfer_procedures)
    #StudentProcedure -> StudentUnsubscribementProcedure
    student_unsubscribement_procedures = StudentUnsubscribementProcedure.objects.filter(student_procedure__in=student_procedures)
    student_unsubscribement_procedure_reasons = ProcedureReason.objects.filter(studentunsubscribementprocedure__in=student_unsubscribement_procedures)
    #StudentProcedure -> StudentStudyContinuityProcedure
    student_study_continuity_procedures = StudentStudyContinuityProcedure.objects.filter(student_procedure__in=student_procedures)
    #Person -> LegalTutor
    legal_tutors = LegalTutor.objects.filter(legal_tutor__in=persons)
    #Structure -> WorkerProcedure
    worker_procedures = WorkerProcedure.objects.filter(structure=structure)
    #Person -> WorkerRegistration
    worker_registrations = WorkerRegistration.objects.filter(person__in=persons)
    #WorkerProcedure -> WorkerChangeOfFunctionsProcedure
    worker_change_of_functions_procedures = WorkerChangeOfFunctionsProcedure.objects.filter(worker_procedure__in=worker_procedures)
    #WorkerProcedure -> WorkerChangeOfJobPositionProcedure
    worker_change_of_job_position_procedures = WorkerChangeOfJobPositionProcedure.objects.filter(worker_procedure__in=worker_procedures)
    #WorkerProcedure -> WorkerEconomicLendingProcedure
    worker_economic_lending_procedures = WorkerEconomicLendingProcedure.objects.filter(worker_procedure__in=worker_procedures)
    #WorkerProcedure -> WorkerIncomeProcedure
    worker_income_procedures = WorkerIncomeProcedure.objects.filter(worker_procedure__in=worker_procedures)
    #WorkerProcedure -> WorkerTransferSettings
    worker_transfer_settings = WorkerTransferSettings.objects.filter(worker_procedure__in=worker_procedures)
    #WorkerProcedure -> WorkerUnsubscribementProcedure
    worker_unsubscribement_procedures = WorkerUnsubscribementProcedure.objects.filter(worker_procedure__in=worker_procedures)
    
    ##Extract all info related to Structure##
    structure_buildings = structure.structurebuilding_set.all()
    #Structure -> Building
    buildings = Building.objects.filter(structurebuilding__structure=structure)
    #Building -> BuildingCharacteristics
    building_characteristics = BuildingCharacteristics.objects.filter(building__in=buildings)
    #Structure -> StructureResponsability
    structure_responsibilities = structure.structureresponsibility_set.all()
    #Structure -> Responsibility
    responsibilities = Responsibility.objects.filter(structureresponsibility__structure=structure)
    #Structure -> StructureCharacteristics
    structure_characteristics = structure.structurecharacteristics_set.all()
    #Structure -> Characteristic
    characteristics = Characteristics.objects.filter(structurecharacteristics__structure=structure)
    #Characteristic -> StructureType
    structure_types = StructureType.objects.filter(characteristics__in=characteristics)
    #Structure -> EducativeCenterSpeciality
    educative_center_specialities = EducativeCenterSpeciality.objects.filter(educative_center=structure)
    #Structure -> Speciality
    specialities = structure.specialities.all()
    #Speciality -> SpecialityModality
    speciality_modalities = SpecialityModality.objects.filter(speciality__in=specialities)
    #SpecialityModality -> SpecialityModalityAvtivityEducation
    spacility_modality_activity_educations = SpecialityModalityAvtivityEducation.objects.filter(speciality__in=speciality_modalities)
    
    ## save all about study_plan ##
    #SpecialityModality -> StudyPlan
    study_plans = StudyPlan.objects.filter(speciality__in=speciality_modalities)
    
    #StudyPlan -> StudyPlanVersion
    study_plan_versions = StudyPlanVersion.objects.filter(study_plan__in=study_plans)
    #StudyPlanVersion -> Subject
    discipline_evaluations = DisciplineEvaluation.objects.filter(study_plan_version__in=study_plan_versions)
    subject_version_plans = SubjectVersionPlan.objects.filter(study_plan_version__in=study_plan_versions)
    
    #StudyPlanVersion -> Discipline
    disciplines_1 = Discipline.objects.filter(studyplanversion__in=study_plan_versions)
    disciplines_2 = Discipline.objects.filter(disciplineevaluation__in=discipline_evaluations)
    disciplines_3 = Discipline.objects.filter(subjectversionplan__in=subject_version_plans)
    disciplines = disciplines_1 | disciplines_2 | disciplines_3
    #StudyPlanVersion -> EvaluationWay
    
    study_plan_organizations = StudyPlanOrganization.objects.filter(study_plan_version__in=study_plan_versions)
    subject_organizations = SubjectOrganization.objects.filter(study_plan_organization__in=study_plan_organizations)
    
    school_frames = SchoolFrame.objects.filter(studyplanorganization__in=study_plan_organizations)
    subjects_1 = Subject.objects.filter(studyplanversion__in=study_plan_versions)
    subjects_2 = Subject.objects.filter(studyplanorganization__in=study_plan_organizations)
    subjects_3 = Subject.objects.filter(subjectversionplan__in=subject_version_plans)
    subjects_4 = Subject.objects.filter(subjectorganization__in=subject_organizations)
    subjects = subjects_1 | subjects_2 | subjects_3 | subjects_4
    #StudyPlanVersion -> DisciplineEvaluation
    #DisciplineEvaluation -> Discipline
    subject_versions_1 = SubjectVersion.objects.filter(subject__in=subjects)
    subject_versions_2 = SubjectVersion.objects.filter(subjectorganization__in=subject_organizations)
    subject_versions = subject_versions_1 | subject_versions_2
    
    evaluation_form_registries = EvaluationFormRegistry.objects.filter(subject_version__in=subject_versions)    

    evaluation_culmination_studies_1 = EvaluationCulminationStudy.objects.filter(study_plan_version__in=study_plan_versions)
    evaluation_culmination_studies_2 = EvaluationCulminationStudy.objects.filter(studyplanorganization__in=study_plan_organizations)
    evaluation_culmination_studies = evaluation_culmination_studies_1 | evaluation_culmination_studies_2
    
    evaluation_categories_1 = EvaluationCategory.objects.filter(disciplineevaluation__in=discipline_evaluations)
    evaluation_categories_2 = EvaluationCategory.objects.filter(evaluationformregistry__in=evaluation_form_registries)
    evaluation_categories_3 = EvaluationCategory.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
    evaluation_categories = evaluation_categories_1 | evaluation_categories_2 | evaluation_categories_3
    
    evaluation_types_1 = EvaluationType.objects.filter(disciplineevaluation__in=discipline_evaluations)
    evaluation_types_2 = EvaluationType.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
    evaluation_types_3 = EvaluationType.objects.filter(evaluationformregistry__in=evaluation_form_registries)
    evaluation_types_4 = EvaluationType.objects.filter(subjectversion__in=subject_versions)
    evaluation_types = evaluation_types_1 | evaluation_types_2 | evaluation_types_3 | evaluation_types_4
    
    qualification_ranges_1 = QualificationRange.objects.filter(disciplineevaluation__in=discipline_evaluations)
    qualification_ranges_2 = QualificationRange.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
    qualification_ranges_3 = QualificationRange.objects.filter(evaluationformregistry__in=evaluation_form_registries)
    qualification_ranges = qualification_ranges_1 | qualification_ranges_2 | qualification_ranges_3
    
    evaluation_ways_1 = EvaluationWay.objects.filter(studyplanversion__in=study_plan_versions)
    evaluation_ways_2 = EvaluationWay.objects.filter(disciplineevaluation__in=discipline_evaluations)
    evaluation_ways_3 = EvaluationWay.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
    evaluation_ways_4 = EvaluationWay.objects.filter(evaluationformregistry__in=evaluation_form_registries)
    evaluation_ways = evaluation_ways_1 | evaluation_ways_2 | evaluation_ways_3 | evaluation_ways_4

    not_lective_organizations = NotLectiveOrganization.objects.filter(study_plan_organization__in=study_plan_organizations)

    not_lective_subjects_1 = NotLectiveSubject.objects.filter(study_plan_version__in=study_plan_versions)
    not_lective_subjects_2 = NotLectiveSubject.objects.filter(notlectiveorganization__in=not_lective_organizations)
    not_lective_subjects = not_lective_subjects_1 | not_lective_subjects_2
        
    study_plan_configurations = StudyPlanConfiguration.objects.filter(study_plan_version__in=study_plan_versions)
    study_modalities = StudyModality.objects.filter(studyplanconfiguration__in=study_plan_configurations)
    course_types = CourseType.objects.filter(studyplanconfiguration__in=study_plan_configurations)
    
    academic_years_1 = AcademicYear.objects.filter(schoolframe__in=school_frames)
    academic_years_2 = AcademicYear.objects.filter(notlectiveorganization__in=not_lective_organizations)
    academic_years_3 = AcademicYear.objects.filter(subjectorganization__in=subject_organizations)
    academic_years = academic_years_1 | academic_years_2 | academic_years_3
    
    organization_form = OrganizativeForm.objects.filter(subjectversion__in=subject_versions)
    
    subject_types_1 = SubjectType.objects.filter(subjectorganization__in=subject_organizations)
    subject_types_2 = SubjectType.objects.filter(notlectivesubject__in=not_lective_subjects)
    subject_types = subject_types_1 | subject_types_2
    
    school_periods_1 = SchoolPeriod.objects.filter(subjectorganization__in=subject_organizations)
    school_periods_2 = SchoolPeriod.objects.filter(notlectiveorganization__in=not_lective_organizations)
    school_periods = school_periods_1 | school_periods_2
    
    evaluation_form_registries = EvaluationFormRegistry.objects.filter(subject_version__in=subject_versions)

    evaluation_way_types = EvaluationWayType.objects.filter(evaluation_way__in=evaluation_ways)

    organizative_form_registries_1 = OrganizativeFormRegistry.objects.filter(organizative_form__in=organization_form)
    organizative_form_registries_2 = OrganizativeFormRegistry.objects.filter(subject_version__in=subject_versions)
    organizative_form_registries = organizative_form_registries_1 | organizative_form_registries_2
    
    typologies = Typology.objects.filter(organizativeformregistry__in=organizative_form_registries)
    #crear un diccionario para unir todos los jsons
    study_plan_organization_evaluations_1 = StudyPlanOrganizationEvaluation.objects.filter(study_plan_organization__in=study_plan_organizations)
    study_plan_organization_evaluations_2 = StudyPlanOrganizationEvaluation.objects.filter(evaluation_culmination_study__in=evaluation_culmination_studies)
    study_plan_organization_evaluations = study_plan_organization_evaluations_1 | study_plan_organization_evaluations_2
    
    school_frame_registries_1 = SchoolFrameRegistry.objects.filter(school_frame__in=school_frames)
    school_frame_registries_2 = SchoolFrameRegistry.objects.filter(academic_year__in=academic_years)
    school_frame_registries_3 = SchoolFrameRegistry.objects.filter(school_period__in=school_periods)
    school_frame_registries = school_frame_registries_1 | school_frame_registries_2 | school_frame_registries_3
    
    cycles = Cycle.objects.filter(schoolframeregistry__in=school_frame_registries)
    
    speciality_study_plan_configurations = SpecialityStudyPlanConfiguration.objects.filter(study_plan_configuration__in=study_plan_configurations)
    speciality_configuations = SpecialityModalityAvtivityEducation.objects.filter(specialitystudyplanconfiguration__in=speciality_study_plan_configurations)
    
    values = Value.objects.filter(range__in=qualification_ranges)
    
    data = [
        structure,
        person_structures,
        persons,
        students,
        educational_workers,
        not_educational_workers,
        student_groups,
        student_tutors,
        tutors,
        person_evaluation_by_courses,
        evaluations,
        person_evaluations,
        years_teaching_experiences,
        person_discapacities,
        person_diseases,
        person_masive_organizations,
        person_politic_organization,
        educational_worker_groups,
        student_procedures,
        procedure_students,
        student_registrations,
        student_registrations_way_entries,
        student_registrations_teaching_status,
        student_procedure_types,
        student_procedure_initial_teaching_status,
        education_change_procedures,
        education_change_procedure_reasons,
        group_change_procedures,
        period_change_procedures,
        student_enrollment_procedures,
        student_enrollment_procedure_way_entries,
        student_graduations,
        student_income_procedures,
        student_placements,
        student_placement_reasons,
        student_transfer_procedures,
        student_transfer_procedure_reasons,
        student_unsubscribement_procedures,
        student_unsubscribement_procedure_reasons,
        student_study_continuity_procedures,
        legal_tutors,
        worker_procedures,
        worker_registrations,
        worker_change_of_functions_procedures,
        worker_change_of_job_position_procedures,
        worker_economic_lending_procedures,
        worker_income_procedures,
        worker_transfer_settings,
        worker_unsubscribement_procedures,
        structure_buildings,
        buildings,
        building_characteristics,
        structure_responsibilities,
        responsibilities,
        structure_characteristics,
        characteristics,
        structure_types,
        educative_center_specialities,
        specialities,
        speciality_modalities,
        spacility_modality_activity_educations,
        study_plans,
        study_plan_versions,
        discipline_evaluations,
        subject_version_plans,
        disciplines,
        evaluation_categories,
        evaluation_types,
        study_plan_organizations,
        evaluation_culmination_studies,
        qualification_ranges,
        evaluation_ways,
        not_lective_subjects,
        study_plan_configurations,
        study_modalities,
        course_types,
        subjects,
        school_frames,
        academic_years,
        subject_versions,
        organization_form,
        subject_organizations,
        subject_types,
        school_periods,
        evaluation_form_registries,
        evaluation_way_types,
        not_lective_organizations,
        organizative_form_registries,
        typologies,
        study_plan_organization_evaluations,
        school_frame_registries,
        cycles,
        speciality_study_plan_configurations,
        speciality_configuations,
        values,
    ]
    query_dict = {}
    for obj in data:
        if isinstance(obj, QuerySet):
            query_dict[obj.model._meta.model_name] = obj
        else:
            query_dict[obj._meta.model_name] = obj
    return query_dict