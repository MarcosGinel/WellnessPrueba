from rest_framework.permissions import BasePermission

class PrecioUserPermissions(BasePermission):

    def has_permission(self, request, view):
        '''
        Define si el usuario autenticado en request.user tiene permiso para realizar la acción PUT, GET, POST o DELETE
        :param request:
        :param view:
        :return:
        '''

        #if view.action == "create":
        #    return True
        if request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'list']:
            return True
        else:
            # GET a /api/2.0/users/
            return False

    def has_object_permission(self, request, view, obj):
        '''
        Define si el usuario autenticado en request.user puede hacer GET, PUT, DELETE sobre el objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        '''
        return request.user.is_superuser or request.user == obj