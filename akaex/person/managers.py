from django.db import models
from procedure.nom_types import *
from django.db.models import ObjectDoesNotExist
class PersonQuerySet(models.QuerySet):
    """
        With this class we can chain `get_students_queryset` function with others queryset methods
        Ex: Person.objects.get_students_queryset().filter(...).order_by(...)
    """
    
    def get_students_queryset(self):
        from procedure.models import ProcedureStudent
        students_uuids_qs = ProcedureStudent.objects.all().values_list('person_id')
        students_ids = [str(student_uuid[0]) for student_uuid in students_uuids_qs]
        return self.filter(pk__in=students_ids)

    def get_students_registered_queryset(self):
        from procedure.models import StudentRegistration
        students_uuids_qs = StudentRegistration.objects.filter(procedure_type=CONST_PROCEDURE_REGISTRATION, is_disable=False).values_list('student__person_id')
        return self.filter(pk__in=students_uuids_qs)

    def get_students_placement_queryset(self):
        from procedure.models import StudentRegistration
        students_uuids_qs = StudentRegistration.objects.filter(procedure_type=CONST_PROCEDURE_PLACEMENT, is_disable=False).values_list('student__person_id')
        return self.filter(pk__in=students_uuids_qs)

    def get_students_enrrollment_queryset(self):
        from procedure.models import StudentRegistration
        students_uuids_qs = StudentRegistration.objects.filter(procedure_type=CONST_PROCEDURE_ENROLLMENT, is_disable=False).values_list('student__person_id')
        return self.filter(pk__in=students_uuids_qs)

    def get_students_transfered_queryset(self):
        from procedure.models import StudentRegistration
        students_uuids_qs = StudentRegistration.objects.filter(procedure_type=CONST_PROCEDURE_TRANSFER, is_disable=False).values_list('student__person_id')
        return self.filter(pk__in=students_uuids_qs)
    
    def get_students_education_change_queryset(self):
        from procedure.models import StudentRegistration
        students_uuids_qs = StudentRegistration.objects.filter(procedure_type=CONST_PROCEDURE_CHANGE_OF_EDUCATION, is_disable=False).values_list('student__person_id')
        return self.filter(pk__in=students_uuids_qs)

    def get_not_students_queryset(self):
        from procedure.models import ProcedureStudent
        students_uuids_qs = ProcedureStudent.objects.all().values_list('person_id')
        students_ids = [str(student_uuid[0]) for student_uuid in students_uuids_qs ]       
        return self.exclude(pk__in=students_ids)

    def get_admissible_students_queryset(self, procedure):
        from procedure.models import StudentRegistration, StudentProcedureType
        if procedure not in dict(STUDENT_PROCEDURE_TYPE).keys():
            raise ObjectDoesNotExist("No existe dicho tipo de trámite")
        else:
            try:
                student_procedure_type = StudentProcedureType.objects.get(procedure_type=procedure)
            except ObjectDoesNotExist as err:
                raise ObjectDoesNotExist('No existe una configuración para dicho trámite: {0}'.format(err))
            
            if procedure==CONST_PROCEDURE_REGISTRATION:
                return self.get_not_students_queryset()
            else:
                initial_states = student_procedure_type.initial_states.all()
                students_uuids_qs = StudentRegistration.objects.filter(state__in=initial_states, is_disable=False).values_list('student__person_id')
                return self.filter(pk__in=students_uuids_qs)
    
    def get_workers_queryset(self):
        pass

class PersonManager(models.Manager):
    
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)
    
    def get_students(self):
        return self.get_queryset().get_students_queryset()

    def get_students_registered_queryset(self):
        return self.get_queryset().get_students_registered_queryset()

    def get_students_placement_queryset(self):
        return self.get_queryset().get_students_placement_queryset()

    def get_students_enrrollment_queryset(self):
        return self.get_queryset().get_students_enrrollment_queryset()

    def get_students_transfered_queryset(self):
        return self.get_queryset().get_students_transfered_queryset()
    
    def get_students_education_change_queryset(self):
        return self.get_queryset().get_students_education_change_queryset()

    def get_admissible_students_queryset(self, procedure):
        return self.get_queryset().get_admissible_students_queryset(procedure)

    def get_not_students(self):
            return self.get_queryset().get_not_students_queryset()
    
    def get_workers(self):
        return self.get_queryset().get_workers_queryset()