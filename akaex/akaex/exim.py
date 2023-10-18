from .excel import excel_bytes_to_queryset, queryset_to_excel_bytes
from .zip import zip_files, unzip_files

def export_zip(data):
    files = {}
    for name, bytes in data.items():
        files[name] = queryset_to_excel_bytes(bytes)
    return zip_files(files)

def import_zip(data):
    pass