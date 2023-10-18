# from django.db import models
# from django.core.serializers import serialize, deserialize
# import json

# def serialize_json(obj:models.Model):
#     output = {obj._meta.model_name:[obj]}
#     queue = []
#     fields = obj._meta.get_fields(include_parents=False, include_hidden=False)
#     graph = []
#     for field in fields:
#         if hasattr(field, "get_accessor_name"):
#             items = getattr(obj, field.get_accessor_name()).all()
#             model_name = items.model._meta.model_name
#             output[model_name] = items
#             queue.append(items.model)
#     while len(queue) > 0:
#         curr = queue[0]
#         queue = queue[1:]
    
#     # while len(queue) > 0:
#     #     curr = queue[0]
#     #     model:models.Model = curr.model
#     #     fields = model._meta.get_fields(include_parents=False, include_hidden=False)
#     #     for field in fields:
#     #         if field.
#     #         field.model.objects.filter(**{})

#     return json.dumps(json.loads(json.dumps(output)),indent=4)