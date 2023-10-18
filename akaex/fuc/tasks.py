from base.celery import app
from core.middleware import ModelRequestMiddleware
from core.utils import send_sentry_error
import os
from datetime import date, datetime, timezone
from os import path
from django.db.models import F
from django.conf import settings
from django.core.files import File
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from fuc.models import *
from fuc.api.serializers import *


@app.task(bind=True)
def async_fuc_validate_user(self, fuc_user, data):
    try:
        hoy = date.today()
        now = datetime.now()  # current date and time
        date_time_now = now.strftime("%Y-%m-%d_%H:%M:%S")

        list_data = []

        if isinstance(data, dict):
            for row in data:
                row_data = {
                    'tomo': row.tomo,
                    'folio': row.folio,
                    'ci': row.ci
                }
                list_data.append(row_data)

        return list_data

    except Exception as ex:
        send_sentry_error(ex)

