from base.celery import app
from core.utils import send_sentry_error
from structure.models import Structure


@app.task(bind=True)
def async_update_tree_node(self):
    try:
        Structure.internal_update_tree()
    except Exception as ex:
        send_sentry_error(ex)


# @app.task(bind=True)
# def async_structure_update(self, instance_id, data):
#     try:
#         Structure.objects.filter(pk=instance_id).update(**data)
#     except Exception as ex:
#         send_sentry_error(ex)
#
#
# @app.task(bind=True)
# def async_structure_delete(self, instance_id):
#     try:
#         instance = Structure.objects.get(pk=instance_id)
#         instance.delete()
#     except Exception as ex:
#         send_sentry_error(ex)


