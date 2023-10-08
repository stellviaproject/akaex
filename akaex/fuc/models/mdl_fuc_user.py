from enum import unique
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.db import models
from django.core.validators import MaxValueValidator
from .mdl_fuc_user_manager import FUCUserManager
from user.models import User


class FUCUser(AbstractBaseUser):
    """
        Custom django FUC User model.
    """
    temporary_user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True
    )
    
    password = None
    
    ci = models.CharField(max_length=11, unique=True, db_column="ci")

    tome = models.IntegerField(validators=[MaxValueValidator(9999)],
        db_column="tome")
    
    folio = models.IntegerField(validators=[MaxValueValidator(99)],
        db_column="folio")

    USERNAME_FIELD = 'ci'
    REQUIRED_FIELDS = ['tome', 'folio']
    
    objects = FUCUserManager()

    def check_ci(self, ci: str) -> bool:
        """
        Return a boolean of whether the ci is correct.
        """
        return self.ci == ci
    
    def check_tome(self, tome: int) -> bool:
        """
        Return a boolean of whether the tome is correct.
        """
        return self.tome == tome
    
    def check_folio(self, folio: int) -> bool:
        """
        Return a boolean of whether the tome is correct.
        """
        return self.folio == folio