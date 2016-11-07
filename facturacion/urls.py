from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from facturacion.api import ConsumoDiarioSet, PrecioDiarioSet

router = DefaultRouter()
router.register(r'api/v1/consumodiario', ConsumoDiarioSet)
router.register(r'api/v1/preciodiario', PrecioDiarioSet, base_name="preciodiario")
urlpatterns = [
    url(r'', include(router.urls))
]

