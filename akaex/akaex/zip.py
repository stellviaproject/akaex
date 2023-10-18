import io
import zipfile


def zip_files(files):
    # Crea un objeto BytesIO para almacenar los bytes del archivo ZIP
    zip_bytes = io.BytesIO()
    
    # Crea un objeto ZipFile en modo escritura
    zip_file = zipfile.ZipFile(zip_bytes, 'w', zipfile.ZIP_DEFLATED)
    
    # Escribe los datos del diccionario en el archivo ZIP
    for name, bytes in files.items():
        zip_file.writestr(name, bytes)
    
    # Cierra el objeto ZipFile
    zip_file.close()
    
    # Obtiene los bytes del archivo ZIP
    zip_bytes.seek(0)
    zip_data = zip_bytes.getvalue()
    
    return zip_data

def unzip_files(zip_bytes):
    # Crea un objeto BytesIO con los bytes del archivo ZIP
    zip_file = zipfile.ZipFile(io.BytesIO(zip_bytes))

    # Crea un diccionario para almacenar los nombres de los archivos y sus bytes
    files = {}

    # Lee cada archivo en el archivo ZIP y añade su nombre y bytes al diccionario
    for name in zip_file.namelist():
        with zip_file.open(name) as file:
            files[name] = file.read()

    return files