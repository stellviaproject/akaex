from procedure.models.mdl_education_change_procedure import EducationChangeProcedure
from procedure.models.mdl_student_registration import StudentRegistration
from procedure.models.mdl_student_income_procedure import StudentIncomeProcedure

from user.models import User
from person.models.mdl_person import Person
from procedure.nom_types import CONST_PROCEDURE_CHANGE_OF_EDUCATION, CONST_PROCEDURE_TRANSFER, CONST_PROCEDURE_ENROLLMENT
from procedure.models.mdl_student_procedure import StudentProcedure

from base.celery import app
from core.middleware import ModelRequestMiddleware
from core.utils import send_sentry_error
import os
from datetime import date, datetime, timezone
from os import path

from django.db.models import F
from django.conf import settings
from django.core.files import File
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration



#export wxcel
import xlwt




def async_generate_pdf(query_data, template, file_name):
    """
        Generate PDF file.

        query_data: Datos.
        template: Plantilla html.
        file_name: Nombre del fichero.
    """

    try:

        html_string = render_to_string(template, {'data': query_data})

        html = HTML(string=html_string)

        ROOT_DIR = os.getcwd()
        PDF_DIR = f"{ROOT_DIR}/server/upload/procedure_docs"
        PDF_PATH = PDF_DIR + '/' + file_name

        if not path.exists(PDF_DIR):
            os.makedirs(PDF_DIR)

        # output pdf file
        html.write_pdf(target=PDF_PATH)

        return PDF_PATH

    except Exception as ex:
        send_sentry_error(ex)



# columns: nombre de las columnas del documento
# rows: datos para rellenar el documento
# file_name: nombre del fichero de salida

def async_generate_xsl(self, columns, rows, file_name):
    try:
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Hoja1') # this will make a sheet named 

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save("./server/upload/"+file_name+".xls")

    except Exception as ex:
        send_sentry_error(ex)



def procedure_generate_doc(template, data, file_name, instance):

    file_path = async_generate_pdf(data, template, file_name)

    if path.exists(file_path):

        with open(file_path, 'rb') as f:
            myfile = File(f)

            if instance:
                instance.doc.save(file_name, myfile)

            # remove file after upload to model
            os.remove(file_path)

        myfile.closed


@app.task(bind=True)
def async_moving_student_pdf_education_change(self, person_obj, student_registration_obj, procedure_education_change, centro_origen, address_origen):
    try:
        hoy = date.today()
        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

        date_of_birth = person_obj.date_of_birth

        centro_destino_address = student_registration_obj.school_center.address if student_registration_obj.school_center else ''
        centro_destino_province = student_registration_obj.school_center.province.name if student_registration_obj.school_center else ''
        centro_destino_municipality = student_registration_obj.school_center.municipality.name if student_registration_obj.school_center else ''

        fecha_matricula = None
        if student_registration_obj.speciality:
            fecha_matricula = StudentProcedure.objects.filter(student_registration__student__person=person_obj.id, student_registration__speciality=student_registration_obj.speciality.speciality.id, student_registration__procedure_type=CONST_PROCEDURE_CHANGE_OF_EDUCATION).order_by('end_date').values('end_date').first()

        # years old
        _years_old = hoy.year-date_of_birth.year - ((hoy.month, hoy.day) < (date_of_birth.month, date_of_birth.day))

        # tutors data
        tutores = student_registration_obj.student.legal_tutors.all()

        _tutors = [{'nombre': obj.legal_tutor.full_name,
                    'parentesco': obj.relationship.name if obj.relationship else '',
                    'vinculo': obj.employment_relationship.name if obj.employment_relationship else '',
                    'procedencia': obj.social_origin.name if obj.social_origin else '',
                    'sector': obj.laboral_sector.name if obj.laboral_sector else '',
                    'centro_tabajo': obj.workplace,
                    'formalized': 'Si' if obj.formalized else 'No'} for obj in tutores]

        # tramitators data
        _tramitador_data = {'centro': {'structura':'CENTRO', 'tramitador':procedure_education_change.made_by_person.full_name if procedure_education_change.made_by_person else '',
                             'orden':procedure_education_change.center_order,'fecha':procedure_education_change.center_date },
                            'dme':{'structura':'DME', 'tramitador':procedure_education_change.municipality_approval_person.full_name if procedure_education_change.municipality_approval_person else '',
                             'orden':procedure_education_change.municipality_order,'fecha':procedure_education_change.municipality_date_change },
                            'dpe':{'structura':'DPE', 'tramitador':procedure_education_change.province_approval_person.full_name if procedure_education_change.province_approval_person else '',
                             'orden':procedure_education_change.province_order,'fecha':procedure_education_change.province_date_change },
                            }

        education_level = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name').annotate(
            level=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name')).first()
        education_type = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name').annotate(
            education=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name')).first()
        activity = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name').annotate(
            activity=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name')).first()

        pdf_data = {
            'estudiante': person_obj.full_name,
            'ci': person_obj.ci,
            'race': person_obj.race.name,
            'gender': person_obj.gender.name,
            'edad': _years_old if _years_old else '',
            'direccion': person_obj.address+', '+ person_obj.address_municipality.name +', '+ person_obj.address_province.name,
            'tutors': _tutors,
            'tramitador': _tramitador_data,
            'descripcion': procedure_education_change.description,
            'especialidad_code': student_registration_obj.speciality.code if student_registration_obj.speciality else '',
            'especialidad': student_registration_obj.speciality.speciality.name if student_registration_obj.speciality else '',
            'school_period': student_registration_obj.school_period.name if student_registration_obj.school_period else '',

            'nivel_educativo': education_level['level'] if education_level else '',
            'educacion': education_type['education'] if education_type else '',
            'tipificacion': activity['activity'] if activity else '',

            'academico': student_registration_obj.academic_year.name if student_registration_obj.academic_year else '',
            'fecha_matricula': fecha_matricula['end_date'] if fecha_matricula else '',
            'motivo': procedure_education_change.procedure_reason.name if procedure_education_change.procedure_reason else '',
            'tramite': CONST_PROCEDURE_CHANGE_OF_EDUCATION,
            'course': student_registration_obj.course_type.name if student_registration_obj.course_type else '',
            'centro_origen': centro_origen,
            'address_origen': address_origen,
            'centro_destino': student_registration_obj.school_center.name if student_registration_obj.school_center else '',
            'centro_destino_telefono': student_registration_obj.school_center.main_phone if student_registration_obj.school_center else '',
            'centro_destino_code': student_registration_obj.school_center.code if student_registration_obj.school_center else '',
            'centro_destino_tipo': student_registration_obj.school_center.educational_center_type.name if student_registration_obj.school_center.educational_center_type else '',
            'centro_destino_composicion': 'Mixto' if student_registration_obj.school_center.is_mixed else 'Puro',
            'centro_destino_plan_turquino': 'Si' if student_registration_obj.school_center.plan_turquino else 'No',
            'address_destino': centro_destino_address+', '+centro_destino_municipality+', '+centro_destino_province,
            'tipo_movimiento': 'Cambio de educación',
            'date_time_now': now.strftime("%d-%m-%Y %H:%M:%S"),
            'date_time': now.strftime("%d-%m-%Y"),
            'time_now': now.strftime("%H:%M:%S"),
        }

        template = 'procedure/export/student-movement-report.html'
        file_name = slugify(f"{pdf_data['estudiante']}_{date_time_now}") + '.pdf'
        instance = procedure_education_change

        # generate pdf
        procedure_generate_doc(template, pdf_data, file_name, instance)

    except Exception as ex:
        send_sentry_error(ex)



@app.task(bind=True)
def async_moving_student_pdf_transfer(self, person_obj, student_registration_obj, procedure_transfer, centro_origen, address_origen):
    try:
        hoy = date.today()
        date_of_birth = person_obj.date_of_birth

        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

        centro_destino_address = student_registration_obj.school_center.address if student_registration_obj.school_center else ''
        centro_destino_province = student_registration_obj.school_center.province.name if student_registration_obj.school_center else ''
        centro_destino_municipality = student_registration_obj.school_center.municipality.name if student_registration_obj.school_center else ''


        fecha_matricula = StudentProcedure.objects.filter(student_registration__student__person=person_obj.id,
                                                          student_registration__speciality__speciality=student_registration_obj.speciality.speciality.id,
                                                          student_registration__procedure_type=CONST_PROCEDURE_ENROLLMENT).order_by('end_date').values('end_date').first()

        # years old
        _years_old = hoy.year - date_of_birth.year - ((hoy.month, hoy.day) < (date_of_birth.month, date_of_birth.day))

        tutores = student_registration_obj.student.legal_tutors.all()

        # tutors data
        _tutors = [{'nombre': obj.legal_tutor.full_name,
                    'parentesco': obj.relationship.name if obj.relationship else '',
                    'vinculo': obj.employment_relationship.name if obj.employment_relationship else '',
                    'procedencia': obj.social_origin.name if obj.social_origin else '',
                    'sector': obj.laboral_sector.name if obj.laboral_sector else '',
                    'centro_tabajo': obj.workplace,
                    'formalized': 'Si' if obj.formalized else 'No'} for obj in tutores]


        # tramitators data
        _tramitator_data =  {'centro': {'structura':'CENTRO', 'tramitador':procedure_transfer.center_approval_person.full_name if procedure_transfer.center_approval_person else '',
                             'orden':procedure_transfer.center_order_number,'fecha':procedure_transfer.center_date },
                            'dme': {'structura':'DME', 'tramitador':procedure_transfer.municipality_approval_person.full_name if procedure_transfer.municipality_approval_person else '',
                             'orden':procedure_transfer.municipality_order_number,'fecha':procedure_transfer.municipality_date },
                            'dpe': {'structura':'DPE', 'tramitador':procedure_transfer.province_approval_person.full_name if procedure_transfer.province_approval_person else '',
                             'orden':procedure_transfer.province_order_number,'fecha':procedure_transfer.province_date },
                             }

        education_level = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name').annotate(
            level=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name')).first()
        education_type = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name').annotate(
            education=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name')).first()
        activity = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name').annotate(
            activity=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name')).first()

        pdf_data = {
            'estudiante': person_obj.full_name,
            'ci': person_obj.ci,
            'gender': person_obj.gender.name,
            'edad': _years_old if _years_old else '',
            'direccion': person_obj.address + ', ' + person_obj.address_municipality.name + ', ' + person_obj.address_province.name,
            'tutors': _tutors,
            'tramitador': _tramitator_data,
            'descripcion': procedure_transfer.description,
            'especialidad_code': student_registration_obj.speciality.code if student_registration_obj.speciality else '',
            'especialidad': student_registration_obj.speciality.speciality.name if student_registration_obj.speciality else '',
            'school_period': student_registration_obj.school_period.name if student_registration_obj.school_period else '',

            'nivel_educativo': education_level['level'] if education_level else '',
            'educacion': education_type['education'] if education_type else '',
            'tipificacion': activity['activity'] if activity else '',

            'academico': student_registration_obj.academic_year.name if student_registration_obj.academic_year else '',
            'fecha_matricula': fecha_matricula['end_date'] if fecha_matricula['end_date'] else '',
            'motivo': procedure_transfer.procedure_reason.name,
            'tramite': CONST_PROCEDURE_TRANSFER,
            'course': student_registration_obj.course_type.name,
            'centro_origen': centro_origen,
            'address_origen': address_origen,
            'centro_destino': student_registration_obj.school_center.name if student_registration_obj.school_center else '',
            'centro_destino_telefono': student_registration_obj.school_center.main_phone if student_registration_obj.school_center else '',
            'centro_destino_code': student_registration_obj.school_center.code if student_registration_obj.school_center else '',
            'centro_destino_tipo': student_registration_obj.school_center.educational_center_type.name if student_registration_obj.school_center else '',
            'centro_destino_composicion': 'Mixto' if student_registration_obj.school_center.is_mixed else 'Puro',
            'centro_destino_plan_turquino': 'Si' if student_registration_obj.school_center.plan_turquino else 'No',
            'address_destino': centro_destino_address + ', ' + centro_destino_municipality + ', ' + centro_destino_province,
            'tipo_movimiento': 'Traslado',
            'date_time_now': now.strftime("%d-%m-%Y %H:%M:%S"),
            'date_time': now.strftime("%d-%m-%Y"),
            'time_now': now.strftime("%H:%M:%S"),
        }

        template = 'procedure/export/student-movement-report.html'
        file_name = slugify(f"{pdf_data['estudiante']}_{date_time_now}") + '.pdf'
        instance = procedure_transfer

        # generate pdf
        procedure_generate_doc(template, pdf_data, file_name, instance)

    except Exception as ex:
        send_sentry_error(ex)



def async_moving_student_pdf_unsubscribement(self, person_obj, student_registration_obj,procedure_student_unsubscribement_obj,centro_origen,address_origen):
    try:
        hoy = date.today()
        date_of_birth=person_obj.date_of_birth

        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

        # years old
        _years_old = hoy.year - date_of_birth.year - ((hoy.month, hoy.day) < (date_of_birth.month, date_of_birth.day))


        centro_destino_address=student_registration_obj.school_center.address if student_registration_obj.school_center else ''
        centro_destino_province=student_registration_obj.school_center.province.name if student_registration_obj.school_center else ''
        centro_destino_municipality=student_registration_obj.school_center.municipality.name if student_registration_obj.school_center else ''

        fecha_matricula = StudentProcedure.objects.filter(student_registration__student__person=person_obj.id,
                                                          student_registration__speciality__speciality=student_registration_obj.speciality.speciality.id,
                                                          student_registration__procedure_type=CONST_PROCEDURE_ENROLLMENT).order_by('end_date').values('end_date').first()

        tutores = student_registration_obj.student.legal_tutors.all()

        # tutors data
        _tutors = [{'nombre': obj.legal_tutor.full_name,
                    'parentesco': obj.relationship.name if obj.relationship else '',
                    'vinculo': obj.employment_relationship.name if obj.employment_relationship else '',
                    'procedencia': obj.social_origin.name if obj.social_origin else '',
                    'sector': obj.laboral_sector.name if obj.laboral_sector else '',
                    'centro_tabajo': obj.workplace,
                    'formalized': 'Si' if obj.formalized else 'No'} for obj in tutores]

        # tramitators data
        _tramitators_data = [{'structura':'CENTRO', 'tramitador':procedure_student_unsubscribement_obj.made.full_name if procedure_student_unsubscribement_obj.made else '',
                              'orden':procedure_student_unsubscribement_obj.center_order,'fecha':procedure_student_unsubscribement_obj.center_date },
                            {'structura':'DME', 'tramitador':procedure_student_unsubscribement_obj.approved_municipality.full_name if procedure_student_unsubscribement_obj.approved_municipality else '',
                             'orden':procedure_student_unsubscribement_obj.municipality_order,'fecha':procedure_student_unsubscribement_obj.municipality_date },
                            {'structura':'DPE', 'tramitador':procedure_student_unsubscribement_obj.approved_province.full_name if procedure_student_unsubscribement_obj.approved_province else '',
                             'orden':procedure_student_unsubscribement_obj.province_order,'fecha':procedure_student_unsubscribement_obj.province_date },
                            ]

        education_level = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name').annotate(
            level=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name')).first()
        education_type = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name').annotate(
            education=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name')).first()
        activity = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name').annotate(
            activity=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name')).first()

        pdf_data = {
            'estudiante': person_obj.full_name,
            'ci': person_obj.ci,
            'gender': person_obj.gender.name,
            'edad': _years_old if _years_old else '',
            'direccion': person_obj.address + ', ' + person_obj.address_municipality.name + ', ' + person_obj.address_province.name,
            'tutors': _tutors,
            'tramitador': _tramitators_data,
            'descripcion': procedure_student_unsubscribement_obj.description,
            'especialidad_code': student_registration_obj.speciality.code if student_registration_obj.speciality else '',
            'especialidad': student_registration_obj.speciality.speciality.name if student_registration_obj.speciality else '',
            'school_period': student_registration_obj.school_period.name if student_registration_obj.school_period else '',

            'nivel_educativo': education_level['level'] if education_level else '',
            'educacion': education_type['education'] if education_type else '',
            'tipificacion': activity['activity'] if activity else '',

            'academico': student_registration_obj.academic_year.name if student_registration_obj.academic_year else '',
            'fecha_matricula': fecha_matricula['end_date'] if fecha_matricula['end_date'] else '',
            'motivo':procedure_student_unsubscribement_obj.procedure_reason.name,
            'course': student_registration_obj.course_type.name if student_registration_obj.course_type else '',
            'centro_origen': centro_origen,
            'address_origen': address_origen,
            'centro_destino': student_registration_obj.school_center.name if student_registration_obj.school_center else '',
            'centro_destino_telefono': student_registration_obj.school_center.main_phone if student_registration_obj.school_center else '',
            'centro_destino_code': student_registration_obj.school_center.code if student_registration_obj.school_center else '',
            'centro_destino_tipo': student_registration_obj.school_center.educational_center_type.name if student_registration_obj.school_center else '',
            'centro_destino_composicion': 'Mixto' if student_registration_obj.school_center.is_mixed else 'Puro',
            'centro_destino_plan_turquino': 'Si' if student_registration_obj.school_center.plan_turquino else 'No',
            'address_destino': centro_destino_address + ', ' + centro_destino_municipality + ', ' + centro_destino_province,
            'tipo_movimiento': 'Baja',
            'date_time_now': now.strftime("%d-%m-%Y %H:%M:%S"),
            'date_time': now.strftime("%d-%m-%Y"),
            'time_now': now.strftime("%H:%M:%S"),
        }

        template = 'procedure/export/student-movement-report.html'
        file_name = slugify(f"{pdf_data['estudiante']}_{date_time_now}") + '.pdf'
        instance = procedure_student_unsubscribement_obj

        # generate pdf
        procedure_generate_doc(template, pdf_data, file_name, instance)

    except Exception as ex:
        send_sentry_error(ex)





@app.task(bind=True)
def async_student_data_register_pdf(self, person_obj, student_registration_obj, student_procedure_obj, student_procedure_register_obj):

    try:
        tramitador='Administrador'
        current_user = None
        model_request = ModelRequestMiddleware.get_request()
        if model_request and model_request.user:
            current_user = model_request.user

        try:
            tramitador_obj = Person.objects.get(pk=student_procedure_obj.processor_person_id)
            tramitador = tramitador_obj.full_name
        except Exception as ex:
            tramitador = current_user.first_name + ' ' + current_user.last_name
            pass

        hoy = date.today()
        date_of_birth=person_obj.date_of_birth

        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

        tutores = student_registration_obj.student.legal_tutors.all()

        _tutors = [{'nombre': obj.legal_tutor.full_name,
                    'parentesco': obj.relationship.name if obj.relationship else '',
                    'vinculo': obj.employment_relationship.name if obj.employment_relationship else '',
                    'procedencia': obj.social_origin.name if obj.social_origin else '',
                    'sector': obj.laboral_sector.name if obj.laboral_sector else '',
                    'centro_tabajo': obj.workplace,
                    'formalized': 'Si' if obj.formalized else 'No'} for obj in tutores]


        pdf_data = {
            'estudiante': person_obj.full_name,
            'ci': person_obj.ci,
            'gender': person_obj.gender.name,
            'edad': hoy.year-date_of_birth.year-((hoy.month, hoy.day) < (date_of_birth.month, date_of_birth.day)),
            'direccion': person_obj.address+', '+ person_obj.address_municipality.name +', '+ person_obj.address_province.name,
            'tutors': _tutors,
            'tramitador': tramitador if tramitador else '',
            'fecha': student_procedure_obj.end_date,
            'date_of_birth': date_of_birth,
            'course': student_registration_obj.current_school_course.name if student_registration_obj.current_school_course else '',
            'nationality': student_registration_obj.nationality.name if student_registration_obj.nationality else '',
            'date_time_now': now.strftime("%d-%m-%Y %H:%M:%S"),
            'date_time': now.strftime("%d-%m-%Y"),
            'time_now': now.strftime("%H:%M:%S"),
        }

        template='procedure/export/student-data-report.html'
        file_name = slugify(f"{pdf_data['estudiante']}_{date_time_now}") + '.pdf'
        instance = student_procedure_register_obj

        # generate pdf
        procedure_generate_doc(template, pdf_data, file_name, instance)


    except Exception as ex:
        send_sentry_error(ex)


@app.task(bind=True)
def async_control_enrollment_pdf(self, person_obj, student_registration_obj, student_procedure_obj, procedure_enrollment_obj):
    try:
        hoy = date.today()
        date_of_birth=person_obj.date_of_birth

        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")


        # years old
        _years_old = hoy.year-date_of_birth.year-((hoy.month, hoy.day) < (date_of_birth.month, date_of_birth.day))

        centro_destino_address = student_registration_obj.school_center.address if student_registration_obj.school_center else ''
        centro_destino_province = student_registration_obj.school_center.province.name if student_registration_obj.school_center else ''
        centro_destino_municipality = student_registration_obj.school_center.municipality.name if student_registration_obj.school_center else ''

        tutores = student_registration_obj.student.legal_tutors.all()

        _tutors = [{'nombre': obj.legal_tutor.full_name,
                    'parentesco': obj.relationship.name if obj.relationship else '',
                    'vinculo': obj.employment_relationship.name if obj.employment_relationship else '',
                    'procedencia': obj.social_origin.name if obj.social_origin else '',
                    'sector': obj.laboral_sector.name if obj.laboral_sector else '',
                    'centro_tabajo': obj.workplace,
                    'formalized': 'Si' if obj.formalized else 'No'} for obj in tutores]

        education_level = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name').annotate(
            level=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name')).first()
        education_type = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name').annotate(
            education=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name')).first()
        activity = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name').annotate(
            activity=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name')).first()

        pdf_data={
            'estudiante': person_obj.full_name,
            'ci': person_obj.ci,
            'gender': person_obj.gender.name,
            'edad': _years_old if _years_old else '',
            'direccion': person_obj.address+', '+ person_obj.address_municipality.name +', '+ person_obj.address_province.name,
            'tutors': _tutors,
            
            'especialidad_code': student_registration_obj.speciality.code if student_registration_obj.speciality else '',
            'especialidad': student_registration_obj.speciality.speciality.name if student_registration_obj.speciality else '',
            'academico': student_registration_obj.academic_year.name if student_registration_obj.academic_year else '',

            'nivel_educativo': education_level['level'] if education_level else '',
            'educacion': education_type['education'] if education_type else '',
            'tipificacion': activity['activity'] if activity else '',

            'no_matricula': student_registration_obj.enrollment_number,
            'condicion_matricula': student_registration_obj.enrollment_condition.name if student_registration_obj.enrollment_condition else '',
            'situación_escolar': student_registration_obj.school_situation.name if student_registration_obj.school_situation else '',
            #'sesion': procedure_enrollment_obj.session.name if procedure_enrollment_obj.session else '',
            'via_ingreso': student_registration_obj.way_entry.name if student_registration_obj.way_entry else '',
            
            'center_code':student_registration_obj.school_center.code if student_registration_obj.school_center else '',
            'tipo_centro': student_registration_obj.school_center.educational_center_type.name if student_registration_obj.school_center else '',
            'composicion': 'Si' if student_registration_obj.school_center.is_mixed else 'No',
            'sector': 'Si' if student_registration_obj.school_center.is_rural else 'No',
            'plan_turquino': 'Si' if student_registration_obj.school_center.plan_turquino else 'No',
            'center_name': student_registration_obj.school_center.name if student_registration_obj.school_center else '',
            'center_province': student_registration_obj.school_center.province.name if student_registration_obj.school_center else '',
            'center_municipality': student_registration_obj.school_center.municipality.name if student_registration_obj.school_center else '',
            'fecha_fin': student_procedure_obj.end_date,
            'date_time_now': now.strftime("%d-%m-%Y %H:%M:%S"),
            'date_time': now.strftime("%d-%m-%Y"),
            'time_now': now.strftime("%H:%M:%S"),
        }

        template = 'procedure/export/student-permanent-control-report.html'
        file_name = slugify(f"{pdf_data['estudiante']}_{date_time_now}") + '.pdf'
        instance = procedure_enrollment_obj

        # generate pdf
        procedure_generate_doc(template, pdf_data, file_name, instance)

    except Exception as ex:
        send_sentry_error(ex)


@app.task(bind=True)
def async_student_placement_pdf(self, person_obj, student_registration_obj, student_procedure_obj, student_placement_procedure_obj):
    try:

        tramitador = None
        current_user = None
        model_request = ModelRequestMiddleware.get_request()
        if model_request and model_request.user:
            current_user = model_request.user

        try:
            tramitador_obj = Person.objects.get(pk=student_procedure_obj.processor_person_id)
            if tramitador_obj:
                tramitador = tramitador_obj.full_name if tramitador_obj else ''
            else:
                user_obj = User.objects.get(pk=student_procedure_obj.processor_person_id)
                tramitador = user_obj.first_name + ' ' + user_obj.last_name if user_obj else ''
        except Exception as ex:
            tramitador = current_user.first_name + ' ' + current_user.last_name if current_user else ''
            pass


        hoy = date.today()
        date_of_birth=person_obj.date_of_birth

        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

        centro_destino_name = student_registration_obj.school_center.name
        centro_destino_address = student_registration_obj.school_center.address
        centro_destino_province = student_registration_obj.school_center.province.name
        centro_destino_municipality = student_registration_obj.school_center.municipality.name

        tutores = student_registration_obj.student.legal_tutors.all()

        _tutors = [{'nombre': obj.legal_tutor.full_name,
                    'parentesco': obj.relationship.name if obj.relationship else '',
                    'vinculo': obj.employment_relationship.name if obj.employment_relationship else '',
                    'procedencia': obj.social_origin.name if obj.social_origin else '',
                    'sector': obj.laboral_sector.name if obj.laboral_sector else '',
                    'centro_tabajo': obj.workplace,
                    'formalized': 'Si' if obj.formalized else 'No'} for obj in tutores]

        education_level = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name').annotate(
            level=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_level_type__name')).first()
        education_type = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name').annotate(
            education=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__education_type__name')).first()
        activity = StudentRegistration.objects.filter(pk=student_registration_obj.id, is_disable=False).values(
            'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name').annotate(
            activity=F(
                'speciality__activity_education_level__specialitymodalityavtivityeducation__activity__name')).first()

        pdf_data = {
            'estudiante': person_obj.full_name,
            'ci': person_obj.ci,
            'gender': person_obj.gender.name,
            'edad': hoy.year-date_of_birth.year-((hoy.month, hoy.day) < (date_of_birth.month, date_of_birth.day)),
            'direccion': person_obj.address+', '+ person_obj.address_municipality.name +', '+ person_obj.address_province.name,
            'tutors': _tutors,
            'especialidad_code': student_registration_obj.speciality.code if student_registration_obj.speciality else '',
            'especialidad': student_registration_obj.speciality.speciality.name if student_registration_obj.speciality else '',
            'academico': student_registration_obj.academic_year.name if student_registration_obj.academic_year else '',

            'nivel_educativo': education_level['level'] if education_level else '',
            'educacion': education_type['education'] if education_type else '',
            'tipificacion': activity['activity'] if activity else '',

            'center_code': student_registration_obj.school_center.code if student_registration_obj.school_center else '',
            'tipo_centro': student_registration_obj.school_center.educational_center_type.name if student_registration_obj.school_center else '',
            'composicion': 'Si' if student_registration_obj.school_center.is_mixed else 'No',
            'sector': 'Si' if student_registration_obj.school_center.is_rural else 'No',
            'plan_turquino': 'Si' if student_registration_obj.school_center.plan_turquino else 'No',
            'center_name': centro_destino_name,
            'address_destino': centro_destino_address+', '+centro_destino_municipality+', '+centro_destino_province,
            'fecha_fin': student_procedure_obj.end_date,
            'tramitador': tramitador,
            'date_time_now': now.strftime("%d-%m-%Y %H:%M:%S"),
            'date_time': now.strftime("%d-%m-%Y"),
            'time_now': now.strftime("%H:%M:%S"),
        }

        template = 'procedure/export/student-placement-report.html'
        file_name = slugify(f"{pdf_data['estudiante']}_{date_time_now}") + '.pdf'
        instance = student_placement_procedure_obj

        # generate pdf
        procedure_generate_doc(template, pdf_data, file_name, instance)

    except Exception as ex:
        send_sentry_error(ex)
        