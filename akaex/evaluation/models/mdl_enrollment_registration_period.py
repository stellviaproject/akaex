from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL

from planning.models import Course


class EnrollmentRegistrationPeriod(BaseAkModel):
    """
    Collect the periods for the registration of initial enrollment that are defined in each school year.
    """
    enrollment_cut = models.CharField(_('enrollment cut'), max_length=50, db_column='corte_matricula')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                               verbose_name=_('course'), db_column='curso')
    closing_date = models.DateField(null=True, blank=True, db_column='fecha_cierre', verbose_name=_('closing date'))

    class Meta:
        verbose_name = _('Enrollment Registration Period')
        verbose_name_plural = _('Enrollment Registration Periods')
        db_table = f'{APP_LABEL.lower()}_tbd_enrollment_registration_period'

    def __str__(self):
        return f'{self.enrollment_cut} {self.course}'