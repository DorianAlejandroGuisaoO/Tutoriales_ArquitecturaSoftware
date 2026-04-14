from django.urls import path
from .api.views import CompraAPIView, ProductoListAPIView
from .views import CompraView, InventarioView

urlpatterns = [
    # Usamos .as_view() para habilitar la CBV
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('inventario/', InventarioView.as_view(), name='inventario'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='compra-v1'),
    path('api/v1/productos/', ProductoListAPIView.as_view(), name='productos-v1'),
] 