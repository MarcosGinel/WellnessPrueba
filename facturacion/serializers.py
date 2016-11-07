from rest_framework import serializers

from facturacion.models import ConsumoDiario, PrecioDiario


class PrecioDiarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrecioDiario
        fields = "__all__"


class ConsumoDiarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsumoDiario
        fields = "__all__"


