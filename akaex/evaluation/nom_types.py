from django.utils.translation import gettext_lazy as _

APP_LABEL = 'EVALUACION'

CONST_GROUP_TYPES_ARRASTRE = 'Arrastre'
CONST_GROUP_TYPES_ADELANTO = 'Adelanto'
CONST_GROUP_TYPES_NORMAL = 'Normal'

GROUP_TYPES = (
    (CONST_GROUP_TYPES_ARRASTRE, _(CONST_GROUP_TYPES_ARRASTRE)),
    (CONST_GROUP_TYPES_ADELANTO, _(CONST_GROUP_TYPES_ADELANTO)),
    (CONST_GROUP_TYPES_NORMAL, _(CONST_GROUP_TYPES_NORMAL)),
)

GROUP_TYPES_DEFAULT = 'Normal'

CLOSED_GROUP_STATE = 'Cerrado'
OPEN_GROUP_STATE = 'Abierto'
GROUP_STATES_DEFAULT = OPEN_GROUP_STATE

GROUP_STATES = (
    (OPEN_GROUP_STATE, OPEN_GROUP_STATE),
    (CLOSED_GROUP_STATE, CLOSED_GROUP_STATE)
)

VERBOSE_NAMES = {
    "SIEnrollmentCut": "Statistical Information Enrollment Cut",
    "atomic_total" : "Atomic Total",
    "EnrollmentCutEducativeCenter": "Enrollment cut educative center"
}

VERBOSE_NAMES_PLURAL = {
    
}
GROUP_STATES_DEFAULT = 'Abierto'

EVALUATION_FINAL_TYPE = 'EVALUATIONTYPE_FINAL'

ENROLL_PLACEMENT_CONCEPT = "Matriculado"
ACCREDIT_PLACEMENT_CONCEPT = "Abonado"

PLACEMENT_CONCEPTS = (
    (ENROLL_PLACEMENT_CONCEPT, ENROLL_PLACEMENT_CONCEPT),
    (ACCREDIT_PLACEMENT_CONCEPT, ACCREDIT_PLACEMENT_CONCEPT),
)

PLACEMENT_CONCEPTS_DEFAULT = 'Matriculado'