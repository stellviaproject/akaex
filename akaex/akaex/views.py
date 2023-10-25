import io
import json
from tablib import Dataset
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from structure.models import Structure
from rest_framework.views import APIView
from .model_res import MD_RES
from .query_data import query_struct
from .zip import zip_files, unzip_files
from .jsonapi import structure_to_school

# Vista para renderizar la pagina principal
class HomeView(APIView):
    def get(self, request):#renderiza la pagina principal
        return render(request, 'index.html')

# Vista para importar los datos de una escuela
class ImporterView(APIView):
    def post(self, request):
        #descomprimir el zip y obtener los archivos excels de cada modelo
        all_datasets = unzip_files(request.body)
        has_err = False #variable para determinar si hay un error
        #recorrer archivos excel junto con los nombres de su modelo
        for model_name, xlsl_file in all_datasets.items():
            #obtener el nombre del modelo a partir del nombre del archivo
            model_name = model_name[:len(model_name)-5]
            #obtener el recurso que serializa un modelo a excel
            resource = MD_RES[model_name]()
            dataset = Dataset()#crear un dataset para guardar los datos
            #cargar los datos del archivo excel dentro del dataset
            imported_data = dataset.load(io.BytesIO(xlsl_file), 'xlsx')
            #si el modelo es structure
            if model_name == 'structure':
                #recorrer los datos de structure
                for item in imported_data.dict:
                    #obtener el id de structure
                    id = item['id']
                    #obtener el objeto a actualizar
                    object = MD_RES[model_name].Meta.model.objects.get(id=id)
                    for key, value in item.items():
                        #recorrer los campos de structure a actualizar
                        if value is None:#ignorar si es None
                            continue
                        try:
                            #obtener el tipo de dato del atributo
                            attr_type = type(getattr(object, key))
                            #castear el valor al tipo de dato
                            casted_value = attr_type(value)
                            #establecer el atributo
                            setattr(object, key, casted_value)
                        except Exception:#el error solo será si es una ForeignKey
                            pass
                    object.save()#guardar el objeto
            else:
                #si no es structure es un QuerySet
                result = resource.import_data(dataset, dry_run=True)#importar datos
                has_err |= result.has_errors()#comprobar errores
        #enviar al cliente los datos de si ocurre un error
        return JsonResponse({
            'has_err': has_err,
            }, safe=False)
        
# vista para obtener un listado de todas las escuelas disponibles
class ListerView(APIView):
    def get(self, request):
        #listar todas las escuelas
        structures = Structure.objects.all()
        #generar el serializador a json de las escuelas
        schools = [structure_to_school(structure) for structure in structures]
        #obtener una lista con cada escuela en dict[str,any]
        json_schools = [school.to_dict() for school in schools]
        #serializar las escuelas a json y enviar al cliente
        return JsonResponse(json.dumps(json_schools), safe=False)

# vista para exportar los datos a un archivo comprimido con tablas excel
class ExporterView(APIView):
    def get(self, request, *args, **kwargs):
        #la url es: /export?id=***
        id_param = request.query_params.get('id') #obtener el id de la escuela a exportar
        data_dict = query_struct(id_param) #obtener los datos desde el modelo
        all_datasets = {} #variable para guardar los bytes de los archivos excel
        for model_name, obj in data_dict.items(): #recorrer el diccionario con los datos dic[str,QuerySet]
            resource = MD_RES[model_name]()#obtener el recurso de un modelo e inicializarlo
            dataset = resource.export(obj)#exportar el QuerySet o Model a un dataset
            all_datasets[f"{model_name}.xlsx"] = dataset.xlsx#obtener el dataset en formato xlsx
        zip_data = zip_files(all_datasets)#comprimir todos los archivos xlsx en un zip
        #enviar los datos al cliente
        response = HttpResponse(zip_data, content_type='application/zip')
        response['Content-Disposition'] = 'inline; filename=akademos.zip'
        return response