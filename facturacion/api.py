from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from facturacion.models import ConsumoDiario, PrecioDiario
from facturacion.permissions import PrecioUserPermissions
from facturacion.serializers import ConsumoDiarioSerializer, PrecioDiarioSerializer


class PrecioDiarioSet(ModelViewSet):
    '''
    Clase para la API de Precio diario, permite ordenar por fecha y buscar
    '''
    permission_classes = [PrecioUserPermissions]
    #pagination_class = PageNumberPagination
    serializer_class = PrecioDiarioSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['fecha']
    ordering_fields = ['fecha']


    def get_queryset(self):
        '''
        Query set especial en función de si queremos buscar entre rangos de fechas o no
        '''
        if self.request.query_params.get('fecha_inicio') and self.request.query_params.get('fecha_fin'):
            fecha_inicio = self.request.query_params.get('fecha_inicio')
            fecha_fin = self.request.query_params.get('fecha_fin')
            return PrecioDiario.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
        else:
            return PrecioDiario.objects.all()

    def perform_create(self, serializer):
        '''
        Realiza la creación/edición de la entidad
        :param serializer:
        :return: none
        '''
        # cada vez que vaya a crear un objeto con el serializer que se seleccione... el owner será self.request.user
        serializer.save()


class ConsumoDiarioSet(ModelViewSet):
    '''
    Clase API que serializará y mostrará los datos de los consumos de un usuario
    '''
    queryset = ConsumoDiario.objects.all()
    permission_classes = [PrecioUserPermissions]
    #pagination_class = PageNumberPagination
    serializer_class = ConsumoDiarioSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    #search_fields = ['fecha__fecha', 'usuario__first_name']
    search_fields = ['usuario__id']
    ordering_fields = ['fecha__fecha']

    def perform_create(self, serializer):
        '''
        Realiza la creación/edición de la entidad
        :param serializer:
        :return: None
        '''
        # cada vez que vaya a crear un objeto con el serializer que se seleccione... el owner será self.request.user
        serializer.save()