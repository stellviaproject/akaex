from core.generics.generic import BaseAkModel
from django.db import models
from datetime import datetime

# Model for release administration

# List of release types and env
TYPES_LIST = [
    ("DES", "Aplicación de escritorio"),
    ("MOV", "Aplicación móvil"),
    ("OTH", "Otro"),
]

ENV_LIST = [
    ("PRO", "Producción"),
    ("DEV", "Desarrollo"),
]

# Return the path where release will be saved
def release_storage_path(instance, filename):
    """
    Release will be uploaded to:
    MEDIA_ROOT/releases>/<current_date>/<filename>
    """
    date = datetime.now().strftime("%Y/%m/%d")
    path = f"releases/{date}/{filename}"
    return path

# Model to save release information (name, version, type, env, file)
class ReleaseModel(BaseAkModel):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=30)

    rel_type = models.CharField(max_length=3, choices=TYPES_LIST, default=TYPES_LIST[0])
    env = models.CharField(max_length=3, choices=ENV_LIST, default=ENV_LIST[0])

    file = models.FileField(upload_to=release_storage_path)
