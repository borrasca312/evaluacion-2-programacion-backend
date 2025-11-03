from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.lista_solicitudes, name='lista_solicitudes'),
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('<int:pk>/editar/', views.editar_solicitud, name='editar_solicitud'),
    path('<int:pk>/cerrar/', views.cerrar_solicitud, name='cerrar_solicitud'),
    path('<int:pk>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
]
