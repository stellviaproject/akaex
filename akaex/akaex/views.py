from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.serializers import serialize, deserialize
from structure.models import Structure, Building, StructureBuilding, BuildingCharacteristics, StructureResponsibility, Responsibility, StructureCharacteristics, Characteristics, StructureType, Speciality, SpecialityModality, SpecialityModalityAvtivityEducation
from person.models import Person, PersonStructure, Student, EducationalWorker, NotEducationalWorker, Evaluation, StudentGroup, StudentTutor, PersonEvaluations, PersonEvaluationByCourse, YearsTeachingExperience, Tutor, PersonDiscapacity, PersonDisease, EducationalWorkerGroup, PersonMasiveOrganization, PersonPoliticOrganization
from procedure.models import StudentProcedure, StudentRegistration, EducationChangeProcedure, GroupChangeProcedure, LegalTutor, PeriodChangeProcedure, ProcedureReason, StudentEnrollmentProcedure, StudentGraduation, StudentIncomeProcedure, StudentPlacement, StudentProcedureType, ProcedureStudent, StudentTransferProcedure, StudentUnsubscribementProcedure, StudentStudyContinuityProcedure, WorkerProcedure, WorkerRegistration, WorkerChangeOfFunctionsProcedure, WorkerChangeOfJobPositionProcedure, WorkerEconomicLendingProcedure, WorkerIncomeProcedure, WorkerTransferSettings, WayEntry, TeachingStatus, WorkerUnsubscribementProcedure
from evaluation.models import EducativeCenterSpeciality
from study_plan.models import StudyPlan, StudyPlanVersion, Subject, Discipline, EvaluationWay, DisciplineEvaluation, QualificationRange, EvaluationCategory
from django.http import HttpResponse
from django.conf import settings
from encrypted_files.base import EncryptedFile
from django.shortcuts import render
from .django_auto_serializer.auto_serializer import SerializableInstance

import mimetypes
import json
import io
import zipfile
import os

def index(request):
    return render(request, 'index.html')

# Create your views here.
class Importer(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        for obj in deserialize('json', data["Structure"]):
            obj.save()

class Lister(APIView):
    def get(self, request):
        structures = Structure.objects.all()
        json_structures = serialize('json', structures)
        
        return JsonResponse(json_structures, safe=False)

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
        disciplines |= Discipline.objects.filter(studyplanversion__in=study_plan_versions)
        #DisciplineEvaluation -> EvaluationWay
        evaluation_ways |= EvaluationWay.objects.filter(disciplineevaluation__in=discipline_evaluations)
        #DisciplineEvaluation -> EvaluationCategory
        evaluation_categories = EvaluationCategory.objects.filter(disciplineevaluation__in=discipline_evaluations)
        #DisciplineEvaluation -> QualificationRange
        qualification_ranges = QualificationRange.objects.filter(disciplineevaluation__in=discipline_evaluations)
        #QualitificationRange -> EvaluationCategory
        evaluation_categories |= EvaluationCategory.objects.filter(qualificationrange__in=qualification_ranges)
        
        #crear un diccionario para unir todos los jsons
        merged_json = {
            "Structure": serialize('json', [structure]),
            "PersonStructure": serialize('json', person_structures),
            "Person": serialize('json', persons),
            "Student": serialize('json', students),
            "EducationalWorker": serialize('json', educational_workers),
            "NotEducationalWorker": serialize('json', not_educational_workers),
            "StudentGroup": serialize('json', student_groups),
            "StudentTutor": serialize('json', student_tutors),
            "Tutor": serialize('json', tutors),
            "PersonEvaluationByCourse": serialize('json', person_evaluation_by_courses),
            "Evaluation": serialize('json', evaluations),
            "PersonEvaluation": serialize('json', person_evaluations),
            "YearsTeachingExperience": serialize('json', years_teaching_experiences),
            "PersonDiscapacity": serialize('json', person_discapacities),
            "PersonDiseases": serialize('json', person_diseases),
            "PersonMasiveOrganization": serialize('json', person_masive_organizations),
            "PersonPoliticOrganization": serialize('json', person_politic_organization),
            "EducationalWorkerGroup": serialize('json', educational_worker_groups),
            "StudentProcedure": serialize('json', student_procedures),
            "ProcedureStudent": serialize('json', procedure_students),
            "StudentRegistration": serialize('json', student_registrations),
            "StudentProcedureTypes": serialize('json', student_procedure_types),
            "EducationChangeProcedure": serialize('json', education_change_procedures),
            "GroupChangeProcedure": serialize('json', group_change_procedures),
            "StudentEnrollmentProcedure": serialize('json', student_enrollment_procedures),
            "StudentGraduation": serialize('json', student_graduations),
            "StudentIncomeProcedure": serialize('json', student_income_procedures),
            "StudentPlacement": serialize('json', student_placements),
            "StudentTransferProcedure": serialize('json', student_transfer_procedures),
            "StudentUnsubscribementProcedure": serialize('json', student_unsubscribement_procedures),
            "StudentStudyContinuityProcedure": serialize('json', student_study_continuity_procedures),
            "TeachingStatus": serialize('json', student_registrations_teaching_status | student_procedure_initial_teaching_status),
            "WayEntry": serialize('json', student_registrations_way_entries | student_enrollment_procedure_way_entries),
            "ProcedureReason": serialize('json', student_placement_reasons | student_transfer_procedure_reasons | student_unsubscribement_procedure_reasons),
            "LegalTutor": serialize('json', legal_tutors),
            "WorkerProcedure": serialize('json', worker_procedures),
            "WorkerRegistration": serialize('json', worker_registrations),
            "WorkerChangeOfFunctionProcedure": serialize('json', worker_change_of_functions_procedures),
            "WorkerChangeOfJobPositionProcedure": serialize('json', worker_change_of_job_position_procedures),
            "WorkerTransferSettings": serialize('json', worker_transfer_settings),
            "WorkerUnsubscribementProcedure": serialize('json', worker_unsubscribement_procedures),
            "Speciality": serialize('json', specialities),
        }
        #unir todos los archivos json
        merged_json_str = json.dumps(merged_json)
        
        #TODO: Retornar un comprimido encriptado.
        
        #zipped = zip_json(merged_json_str)
        
        #encrypted = encrypt_file(zipped)
        
        return JsonResponse(merged_json_str, safe=False)
    
def zip_json(json_string):
    # Crea un objeto BytesIO para almacenar los bytes del archivo ZIP
    zip_bytes = io.BytesIO()
     # Crea un objeto ZipFile en modo escritura
    with zipfile.ZipFile(zip_bytes, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Agrega el JSON al archivo ZIP
        zip_file.writestr('data.json', json_string)
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

def encrypt_file(file_bytes):
    # Obtiene la clave del servidor de Django
    key = settings.SECRET_KEY.encode()
    # Crea un objeto EncryptedFile utilizando la clave y los bytes del archivo
    encrypted_file = EncryptedFile(file_bytes, key=key)
    # Lee los bytes encriptados del archivo
    encrypted_bytes = encrypted_file.read()
    return encrypted_bytes

def decrypt_file(encrypted_bytes):
    # Obtiene la clave del servidor de Django
    key = settings.SECRET_KEY.encode()
    # Crea un objeto EncryptedFile utilizando la clave y los bytes encriptados del archivo
    encrypted_file = EncryptedFile(encrypted_bytes, key=key)
    # Lee los bytes desencriptados del archivo
    decrypted_bytes = encrypted_file.read()
    return decrypted_bytes
