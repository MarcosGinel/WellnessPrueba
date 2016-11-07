from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()  # Sólo queremos que sea de lectura (nunca escribir)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.ReadOnlyField()

    def create(self, validated_data):
        '''
        Crea una instancia de User a partir de los datos de validated_data que contiene valores deserializados

        :param validated_data:
        :return:
        '''
        instance = User()

        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        '''
        Actualiza una instance de User a partir de los datos del diccionario
        validated_data que contiene valores deserializados
        :param instance:
        :param validated_data:
        :return:
        '''
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        #instance.set_password(validated_data.get('password'))
        # Se guarda en la base de datos
        instance.save()
        return instance

    def validate_username(self, data):
        '''
        Valida el username
        :param data: nombre de usuario
        :return: si el usuario existe, devuelve data, si no, lanzamos excepción "ValidationError"
        '''
        user = User.objects.filter(username=data)
        if not self.instance and len(user) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        #elif self.instance.username != data and len(user) != 0:
        #    raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data

class UserSerializerConPassword(serializers.Serializer):
    id = serializers.ReadOnlyField()  # Sólo queremos que sea de lectura (nunca escribir)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        '''
        Crea una instancia de User a partir de los datos de validated_data que contiene valores deserializados

        :param validated_data:
        :return:
        '''
        instance = User()

        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        '''
        Actualiza una instance de User a partir de los datos del diccionario
        validated_data que contiene valores deserializados
        :param instance:
        :param validated_data:
        :return:
        '''
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        # Se guarda en la base de datos
        instance.save()
        return instance

    def validate_username(self, data):
        '''
        Valida el username
        :param data: nombre de usuario
        :return: si el usuario existe, devuelve data, si no, lanzamos excepción "ValidationError"
        '''
        user = User.objects.filter(username=data)
        if not self.instance and len(user) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        #elif self.instance.username != data and len(user) != 0:
        #    raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data