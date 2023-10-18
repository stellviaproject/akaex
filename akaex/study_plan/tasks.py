from base.celery import app
from core.utils import send_sentry_error
from study_plan.models import Theme, StudyPlan


#@app.task(bind=True)
#def async_update_tree_node(self):
#    try:
#        StudyProgram.internal_update_tree()
#    except Exception as ex:
#        send_sentry_error(ex)


@app.task(bind=True)
def async_theme_update_tree_node(self):
    try:
        Theme.internal_update_tree()
    except Exception as ex:
        send_sentry_error(ex)


@app.task(bind=True)
def async_study_plan_update_tree_node(self):
    try:
        StudyPlan.internal_update_tree()
    except Exception as ex:
        send_sentry_error(ex)
