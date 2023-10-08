from django.contrib.auth.models import BaseUserManager


class FUCUserManager(BaseUserManager):
    
    def create_user(self, ci, tome, folio, password=None):
        from .mdl_fuc_user import FUCUser
        return FUCUser.objects.create(*locals)

    def create_superuser(self, ):
        raise NotImplementedError()