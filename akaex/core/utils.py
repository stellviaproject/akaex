from sentry_sdk import capture_exception, capture_message
from django.conf import settings

APP_LABEL = 'CORE'

def send_sentry_error(exception):
    if settings.SENTRY_ENVIRONMENT == 'production' or settings.SENTRY_ENVIRONMENT == 'staging':
        capture_exception(exception)
    else:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(str(exception))
        raise exception


def send_sentry_message(message, level):
    if settings.SENTRY_ENVIRONMENT == 'production' or settings.SENTRY_ENVIRONMENT == 'staging':
        capture_message(message=message, level=level)
    else:
        import logging
        logger = logging.getLogger(__name__)
        logger.info(str(message))


def paginate_function(queryset, value, paginate):
    pag_total = value + 1
    pag_top = pag_total * paginate
    pag_low = pag_top - paginate

    if value == 0:
        queryset = queryset[0:pag_top]
    if value > 0:
        queryset = queryset[pag_low:pag_top]
    return queryset

