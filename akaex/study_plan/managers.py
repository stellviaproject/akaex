from django.db import models
from core.models import Nomenclator, NOM_TYPE

from django.utils.translation import gettext_lazy as _

from .models import *


class RatingScaleManager(models.Manager):
    

    def getRatingScaleById(id):
        return RatingScale.objects.get(pk=id)


    def getRatingScaleValueByPercent(rating_scale_id, percent):
        rating_scale_max_value = self.getRatingScaleById(rating_scale_id).max()
        return round(((percent * rating_scale_max_value) / 100), 2)


    def getCalificationNoteByPercent (rating_scale_id, percent, acronym):
        rating_scale = self.getRatingScaleById(rating_scale_id)
        scale_ranges = rating_scale.scale_ranges()
        cant_ranges = len(scale_ranges)

        if (cant_ranges > 0):
            value = self.getRatingScaleValueByPercent(rating_scale_id, percent)
            nom_qualitative_scale_type = Nomenclator.objects.get(name='Cualitativa')

            for sc_range in scale_ranges:
                if (sc_range.min() <= value and value <= sc_range.max()):
                    if (rating_scale.type() == nom_qualitative_scale_type):

                        if (acronym):
                            return sc_range.acronym()

                        return sc_range.qualification_type()

                    else:
                        return sc_range.value()
                    
        else:
            return None

