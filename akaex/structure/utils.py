from guardian.shortcuts import get_objects_for_user
from core.middleware import ModelRequestMiddleware

APP_LABEL = 'ESTRUCTURA'


def get_objects_user_permission(qs,perm_list,user=None):
    """
    Get objects for user.
    """
    if user is None:
        model_request = ModelRequestMiddleware.get_request()
        if model_request and model_request.user:
            user = model_request.user

    objects_list = get_objects_for_user(user, perm_list, klass=qs, any_perm=True, with_superuser=True, accept_global_perms=False)
    return objects_list
