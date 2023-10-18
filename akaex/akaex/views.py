from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse, FileResponse
from django.core.serializers import serialize, deserialize
from structure.models import Structure, Building, StructureBuilding, BuildingCharacteristics, StructureResponsibility, Responsibility, StructureCharacteristics, Characteristics, StructureType, Speciality, SpecialityModality, SpecialityModalityAvtivityEducation
from person.models import Person, PersonStructure, Student, EducationalWorker, NotEducationalWorker, Evaluation, StudentGroup, StudentTutor, PersonEvaluations, PersonEvaluationByCourse, YearsTeachingExperience, Tutor, PersonDiscapacity, PersonDisease, EducationalWorkerGroup, PersonMasiveOrganization, PersonPoliticOrganization
from procedure.models import StudentProcedure, StudentRegistration, EducationChangeProcedure, GroupChangeProcedure, LegalTutor, PeriodChangeProcedure, ProcedureReason, StudentEnrollmentProcedure, StudentGraduation, StudentIncomeProcedure, StudentPlacement, StudentProcedureType, ProcedureStudent, StudentTransferProcedure, StudentUnsubscribementProcedure, StudentStudyContinuityProcedure, WorkerProcedure, WorkerRegistration, WorkerChangeOfFunctionsProcedure, WorkerChangeOfJobPositionProcedure, WorkerEconomicLendingProcedure, WorkerIncomeProcedure, WorkerTransferSettings, WayEntry, TeachingStatus, WorkerUnsubscribementProcedure
from evaluation.models import EducativeCenterSpeciality
from study_plan.models import StudyPlan, StudyPlanVersion, Subject, Discipline, EvaluationWay, DisciplineEvaluation, QualificationRange, EvaluationCategory, EvaluationCulminationStudy, NotLectiveOrganization, NotLectiveSubject, StudyPlanConfiguration, StudyPlanOrganizationEvaluation, SubjectVersionPlan, EvaluationType, SubjectType, StudyModality, CourseType, StudyPlanOrganization, SchoolFrame, AcademicYear, OrganizativeForm, SubjectVersion, SubjectOrganization, SchoolPeriod, EvaluationFormRegistry, EvaluationWayType, OrganizativeFormRegistry, Typology, SchoolFrameRegistry, Cycle, SpecialityStudyPlanConfiguration, Value
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from .django_auto_serializer.auto_serializer import SerializableInstance
from django.db import models
import mimetypes
import json
import io
import zipfile
import os
from .jsonapi import structure_to_school

def index(request):
    return render(request, 'index.html')

# Create your views here.
class Importer(APIView):
    def post(self, request):
        json_str = unzip_json(request.body)
        merged_json = json.loads(json_str)
        for _, serialized_data in merged_json.items():
            # Deserializa los datos
            objs_with_deferred_fields = []
            deserialized_data = deserialize('json', serialized_data)
            for obj in deserialized_data:
                obj.save()
                if obj.deferred_fields is not None:
                    objs_with_deferred_fields.append(obj)
            for obj in objs_with_deferred_fields:
                obj.save_deferred_fields()
        return JsonResponse({}, safe=False)

class Lister(APIView):
    def get(self, request):
        structures = Structure.objects.all()
        schools = [structure_to_school(structure) for structure in structures]
        json_schools = [school.to_dict() for school in schools]
        return JsonResponse(json.dumps(json_schools), safe=False)

class Exporter(APIView):
    def get(self, request, *args, **kwargs):
        id_param = request.query_params.get('id')
    
        #################################################################
        ## NOTA: TODA VARIABLE CON PREFIJO  SE SERIALIZARA A JSON ##
        #################################################################
    
        ## Extract all info from structure##
        #obtener la estructura con el id o nombre
        structure = Structure.objects.get(id=id_param)
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
        subjects = Subject.objects.filter(studyplanversion__in=study_plan_versions)
        #StudyPlanVersion -> Discipline
        disciplines = Discipline.objects.filter(studyplanversion__in=study_plan_versions)
        #StudyPlanVersion -> EvaluationWay
        evaluation_ways = EvaluationWay.objects.filter(studyplanversion__in=study_plan_versions)
        
        #StudyPlanVersion -> DisciplineEvaluation
        discipline_evaluations = DisciplineEvaluation.objects.filter(study_plan_version__in=study_plan_versions)
        #DisciplineEvaluation -> Discipline
        disciplines |= Discipline.objects.filter(disciplineevaluation__in=discipline_evaluations)
        evaluation_ways |= EvaluationWay.objects.filter(disciplineevaluation__in=discipline_evaluations)
        qualification_ranges = QualificationRange.objects.filter(disciplineevaluation__in=discipline_evaluations)
        evaluation_categories = EvaluationCategory.objects.filter(disciplineevaluation__in=discipline_evaluations)
        evaluation_types = EvaluationType.objects.filter(disciplineevaluation__in=discipline_evaluations)
        
        evaluation_culmination_studies = EvaluationCulminationStudy.objects.filter(study_plan_version__in=study_plan_versions)
        evaluation_ways |= EvaluationWay.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
        qualification_ranges |= QualificationRange.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
        evaluation_categories |= EvaluationCategory.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
        evaluation_types |= EvaluationType.objects.filter(evaluationculminationstudy__in=evaluation_culmination_studies)
        
        not_lective_subjects = NotLectiveSubject.objects.filter(study_plan_version__in=study_plan_versions)
        subject_types = SubjectType.objects.filter(notlectivesubject__in=not_lective_subjects)
        
        study_plan_configurations = StudyPlanConfiguration.objects.filter(study_plan_version__in=study_plan_versions)
        study_modalities = StudyModality.objects.filter(studyplanconfiguration__in=study_plan_configurations)
        course_types = CourseType.objects.filter(studyplanconfiguration__in=study_plan_configurations)
        
        study_plan_organizations = StudyPlanOrganization.objects.filter(study_plan_version__in=study_plan_versions)
        subjects |= Subject.objects.filter(studyplanorganization__in=study_plan_organizations)
        evaluation_culmination_studies |= EvaluationCulminationStudy.objects.filter(studyplanorganization__in=study_plan_organizations)
        school_frames = SchoolFrame.objects.filter(studyplanorganization__in=study_plan_organizations)
        academic_years = AcademicYear.objects.filter(schoolframe__in=school_frames)
        
        subject_version_plans = SubjectVersionPlan.objects.filter(study_plan_version__in=study_plan_versions)
        disciplines |= Discipline.objects.filter(subjectversionplan__in=subject_version_plans)
        subjects |= Subject.objects.filter(subjectversionplan__in=subject_version_plans)
        
        subject_versions = SubjectVersion.objects.filter(subject__in=subjects)
        organization_form = OrganizativeForm.objects.filter(subjectversion__in=subject_versions)
        evaluation_form = EvaluationType.objects.filter(subjectversion__in=subject_versions)
        
        subject_organizations = SubjectOrganization.objects.filter(study_plan_organization__in=study_plan_organizations)
        subjects |= Subject.objects.filter(subjectorganization__in=subject_organizations)
        subject_versions |= SubjectVersion.objects.filter(subjectorganization__in=subject_organizations)
        subject_types |= SubjectType.objects.filter(subjectorganization__in=subject_organizations)
        academic_years |= AcademicYear.objects.filter(subjectorganization__in=subject_organizations)
        school_periods = SchoolPeriod.objects.filter(subjectorganization__in=subject_organizations)
        
        evaluation_form_registries = EvaluationFormRegistry.objects.filter(subject_version__in=subject_versions)
        range = QualificationRange.objects.filter(evaluationformregistry__in=evaluation_form_registries)
        evaluation_categories |= EvaluationCategory.objects.filter(evaluationformregistry__in=evaluation_form_registries)
        evaluation_ways |= EvaluationWay.objects.filter(evaluationformregistry__in=evaluation_form_registries)
        evaluation_types |= EvaluationType.objects.filter(evaluationformregistry__in=evaluation_form_registries)
        
        evaluation_way_types = EvaluationWayType.objects.filter(evaluation_way__in=evaluation_ways)
        
        not_lective_organizations = NotLectiveOrganization.objects.filter(study_plan_organization__in=study_plan_organizations)
        not_lective_subjects |= NotLectiveSubject.objects.filter(notlectiveorganization__in=not_lective_organizations)
        academic_years |= AcademicYear.objects.filter(notlectiveorganization__in=not_lective_organizations)
        school_periods |= SchoolPeriod.objects.filter(notlectiveorganization__in=not_lective_organizations)
        
        organizative_form_registries = OrganizativeFormRegistry.objects.filter(organizative_form__in=organization_form)
        organizative_form_registries |= OrganizativeFormRegistry.objects.filter(subject_version__in=subject_versions)
        typologies = Typology.objects.filter(organizativeformregistry__in=organizative_form_registries)
        #crear un diccionario para unir todos los jsons
        study_plan_organization_evaluations = StudyPlanOrganizationEvaluation.objects.filter(study_plan_organization__in=study_plan_organizations)
        study_plan_organization_evaluations |= StudyPlanOrganizationEvaluation.objects.filter(evaluation_culmination_study__in=evaluation_culmination_studies)
        
        school_frame_registries = SchoolFrameRegistry.objects.filter(school_frame__in=school_frames)
        school_frame_registries |= SchoolFrameRegistry.objects.filter(academic_year__in=academic_years)
        school_frame_registries |= SchoolFrameRegistry.objects.filter(school_period__in=school_periods)
        cycles = Cycle.objects.filter(schoolframeregistry__in=school_frame_registries)
        
        speciality_study_plan_configurations = SpecialityStudyPlanConfiguration.objects.filter(study_plan_configuration__in=study_plan_configurations)
        speciality_configuations = SpecialityModalityAvtivityEducation.objects.filter(specialitystudyplanconfiguration__in=speciality_study_plan_configurations)
        
        values = Value.objects.filter(range__in=qualification_ranges)
        
        merged_json = {
            structure._meta.model_name: serialize('json', [structure]),
            name_of_set(person_structures): serialize('json', person_structures),
            name_of_set(persons): serialize('json', persons),
            name_of_set(students): serialize('json', students),
            name_of_set(educational_workers): serialize('json', educational_workers),
            name_of_set(not_educational_workers): serialize('json', not_educational_workers),
            name_of_set(student_groups): serialize('json', student_groups),
            name_of_set(student_tutors): serialize('json', student_tutors),
            name_of_set(tutors): serialize('json', tutors),
            name_of_set(person_evaluation_by_courses): serialize('json', person_evaluation_by_courses),
            name_of_set(evaluations): serialize('json', evaluations),
            name_of_set(person_evaluations): serialize('json', person_evaluations),
            name_of_set(years_teaching_experiences): serialize('json', years_teaching_experiences),
            name_of_set(person_discapacities): serialize('json', person_discapacities),
            name_of_set(person_diseases): serialize('json', person_diseases),
            name_of_set(person_masive_organizations): serialize('json', person_masive_organizations),
            name_of_set(person_politic_organization): serialize('json', person_politic_organization),
            name_of_set(educational_worker_groups): serialize('json', educational_worker_groups),
            name_of_set(student_procedures): serialize('json', student_procedures),
            name_of_set(procedure_students): serialize('json', procedure_students),
            name_of_set(student_registrations): serialize('json', student_registrations),
            name_of_set(student_procedure_types): serialize('json', student_procedure_types),
            name_of_set(education_change_procedures): serialize('json', education_change_procedures),
            name_of_set(group_change_procedures): serialize('json', group_change_procedures),
            name_of_set(student_enrollment_procedures): serialize('json', student_enrollment_procedures),
            name_of_set(student_graduations): serialize('json', student_graduations),
            name_of_set(student_income_procedures): serialize('json', student_income_procedures),
            name_of_set(student_placements): serialize('json', student_placements),
            name_of_set(student_transfer_procedures): serialize('json', student_transfer_procedures),
            name_of_set(student_unsubscribement_procedures): serialize('json', student_unsubscribement_procedures),
            name_of_set(student_study_continuity_procedures): serialize('json', student_study_continuity_procedures),
            name_of_set(student_registrations_teaching_status): serialize('json', student_registrations_teaching_status | student_procedure_initial_teaching_status),
            name_of_set(student_registrations_way_entries): serialize('json', student_registrations_way_entries | student_enrollment_procedure_way_entries),
            name_of_set(student_placement_reasons): serialize('json', student_placement_reasons | student_transfer_procedure_reasons | student_unsubscribement_procedure_reasons),
            name_of_set(legal_tutors): serialize('json', legal_tutors),
            name_of_set(worker_procedures): serialize('json', worker_procedures),
            name_of_set(worker_registrations): serialize('json', worker_registrations),
            name_of_set(worker_change_of_functions_procedures): serialize('json', worker_change_of_functions_procedures),
            name_of_set(worker_change_of_job_position_procedures): serialize('json', worker_change_of_job_position_procedures),
            name_of_set(worker_transfer_settings): serialize('json', worker_transfer_settings),
            name_of_set(worker_unsubscribement_procedures): serialize('json', worker_unsubscribement_procedures),
            name_of_set(specialities): serialize('json', specialities),
            name_of_set(speciality_modalities): serialize('json', speciality_modalities),
            name_of_set(spacility_modality_activity_educations): serialize('json', spacility_modality_activity_educations),
            name_of_set(study_plans): serialize('json', study_plans),
            name_of_set(study_plan_versions): serialize('json', study_plan_versions),
            name_of_set(subjects): serialize('json', subjects),
            name_of_set(disciplines): serialize('json', disciplines),
            name_of_set(evaluation_ways): serialize('json', evaluation_ways),
            name_of_set(discipline_evaluations): serialize('json', discipline_evaluations),
            name_of_set(qualification_ranges): serialize('json', qualification_ranges),
            name_of_set(evaluation_categories): serialize('json', evaluation_categories),
            name_of_set(evaluation_types): serialize('json', evaluation_types),
            name_of_set(evaluation_culmination_studies): serialize('json', evaluation_culmination_studies),
            name_of_set(not_lective_subjects): serialize('json', not_lective_subjects),
            name_of_set(subject_types): serialize('json', subject_types),
            name_of_set(study_plan_configurations): serialize('json', study_plan_configurations),
            name_of_set(study_modalities): serialize('json', study_modalities),
            name_of_set(course_types): serialize('json', course_types),
            name_of_set(study_plan_organizations): serialize('json', study_plan_organizations),
            name_of_set(school_frames): serialize('json', school_frames),
            name_of_set(academic_years): serialize('json', academic_years),
            name_of_set(subject_version_plans): serialize('json', subject_version_plans),
            name_of_set(subject_versions): serialize('json', subject_versions),
            name_of_set(organization_form): serialize('json', organization_form),
            name_of_set(evaluation_form): serialize('json', evaluation_form),
            name_of_set(subject_organizations): serialize('json', subject_organizations),
            name_of_set(school_periods): serialize('json', school_periods),
            name_of_set(evaluation_form_registries): serialize('json', evaluation_form_registries),
            name_of_set(evaluation_way_types): serialize('json', evaluation_way_types),
            name_of_set(not_lective_organizations): serialize('json', not_lective_organizations),
            name_of_set(organizative_form_registries): serialize('json', organizative_form_registries),
            name_of_set(typologies): serialize('json', typologies),
            name_of_set(study_plan_organization_evaluations): serialize('json', study_plan_organization_evaluations),
            name_of_set(school_frame_registries): serialize('json', school_frame_registries),
            name_of_set(cycles): serialize('json', cycles),
            name_of_set(speciality_study_plan_configurations): serialize('json', speciality_study_plan_configurations),
            name_of_set(speciality_configuations): serialize('json', speciality_configuations),
            name_of_set(values): serialize('json', values),
            name_of_set(range): serialize('json', range),
        }
        #unir todos los archivos json
        merged_json_str = json.dumps(merged_json)
        
        #TODO: Retornar un comprimido encriptado.
        
        zipped = zip_json(merged_json_str)
        response = HttpResponse(zipped, content_type='application/zip')
        response['Content-Disposition'] = 'inline; filename=akademos.zip'
        return response
    
def name_of_set(q:models.QuerySet):
    return q.model._meta.model_name
    
def zip_json(json_string):
    # Crea un objeto BytesIO para almacenar los bytes del archivo ZIP
    zip_bytes = io.BytesIO()
     # Crea un objeto ZipFile en modo escritura
    zip_file = zipfile.ZipFile(zip_bytes, 'w', zipfile.ZIP_DEFLATED)
    # Agrega el JSON al archivo ZIP
    zip_file.writestr('data.json', json_string)
    zip_file.close()
    # Obtiene los bytes del archivo ZIP
    
    zip_bytes.seek(0)
    zip_data = zip_bytes.getvalue()
    
    return zip_data

def unzip_json(zip_data):
    # Crea un objeto BytesIO utilizando los bytes del archivo ZIP
    zip_bytes = io.BytesIO(zip_data)
    # Crea un objeto ZipFile en modo lectura
    with zipfile.ZipFile(zip_bytes, 'r') as zip_file:
        # Lee el contenido del archivo ZIP
        json_bytes = zip_file.read('data.json')
    # Decodifica los bytes en una cadena de caracteres
    json_string = json_bytes.decode()
    return json_string