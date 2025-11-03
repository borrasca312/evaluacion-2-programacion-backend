from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from inventario.auth_views import registro_view
from django.shortcuts import redirect

def redirect_to_solicitudes(request):
    return redirect('inventario:lista_solicitudes')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de autenticación
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/registro/', registro_view, name='registro'),
    # Ruta principal redirige a las solicitudes
    path('', redirect_to_solicitudes, name='home'),
    # Rutas de la aplicación
    path('solicitudes/', include('inventario.urls')),
]
    