from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from users.permissions import UserPermission
from users.serializers import UserSerializer, UserSerializerConPassword
from rest_framework.response import Response

class UserViewSet(GenericViewSet):
    permission_classes = [UserPermission]
    #pagination_class = PageNumberPagination
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return User.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return UserSerializerConPassword
        else:
            return UserSerializer

    def list(self, request):
        self.check_permissions(request)
        self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        '''
        Crea un usuario validandolo primero
        :param request:
        :return:
        '''
        self.check_permissions(request)
        # Creamos un serializer con los datos del POST / data
        serializer = self.get_serializer(data=request.data)
        # Validamos el serializador como si fuese un form...
        if serializer.is_valid():
            # Guardamos el newUser
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user) # compruebo si el usuario autenticado puede hacer GET en este user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer GET en este user
        serializer = self.get_serializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer GET en este user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)